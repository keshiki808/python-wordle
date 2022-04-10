from termcolor import cprint


class Wordle:
    def __init__(self, word, player):
        self.__word = word
        self.__player = player
        self.__found_letters = ["", "", "", "", ""]
        self.__exact_position_letters = ["", "", "", "", ""]
        self.__compiled_results = []
        self.__word_guessed_correctly = False

    @property
    def player(self):
        return self.__player

    @property
    def word_guessed_correctly(self):
        return self.__word_guessed_correctly

    def game_over(self):
        correct_letter_count = 0
        for letter in self.__exact_position_letters:
            if letter.isalpha():
                correct_letter_count += 1
        if correct_letter_count == 5:
            self.__word_guessed_correctly = True
        self.player.guesses_remaining -= 1
        self.__exact_position_letters = ["", "", "", "", ""]
        self.__found_letters = ["", "", "", "", ""]
        return self.__word_guessed_correctly or self.player.guesses_remaining < 0

    def play(self):
        self.display_game_stats()
        while not self.game_over():
            guess_entered_correctly = False
            while not guess_entered_correctly:
                guess_entered_correctly = self.receive_a_guess()
            self.check_guess(self.player.guess)
            self.display_results()
        self.determine_result()
        self.game_cleanup()


    def determine_result(self):
        self.player.game_count += 1
        if self.__word_guessed_correctly:
            print("Congrats you got the word")
            self.player.win_count += 1
        else:
            print(f'Unfortunately you didn\'t get the word, it was: {self.__word}')

    def game_cleanup(self):
        self.player.guesses_remaining = 6
        self.player.guess = ""

    def receive_a_guess(self):
        try:
            print("Make a guess: ")
            self.player.make_guess()
            if not self.valid_guess(self.player.guess):
                raise ValueError
            else:
                return True
        except ValueError:
            print("The guess must be 5 letters")

    def valid_guess(self, guess):
        split_guess = [letter for letter in guess]
        if len(split_guess) != 5:
            return False
        for character in split_guess:
            if not character.isalpha():
                return False
        return True

    def display_game_stats(self):
        print('The player\'s current record is:')
        print("{:20}{:3}".format("Games played: ", self.player.game_count))
        print("{:20}{:3}".format("Games Won: ", self.player.win_count))
        print("{:20}{:3}".format("Win rate: ", self.player.determine_win_rate()))
        print()

    def check_guess(self, guess):
        turn_results = ["", "", "", "", ""]
        for index, letter in enumerate(guess):
            if letter == self.__word[index]:
                self.__exact_position_letters[index] = letter
                turn_results[index] = (letter, "g")
        for index, letter in enumerate(guess):
            if letter in self.__word and (
                    self.__exact_position_letters.count(letter) + self.__found_letters.count(letter)) < self.__word.count(
                letter):
                self.__found_letters[index] = letter
                turn_results[index] = (letter, "y")
            elif turn_results[index] == "":
                turn_results[index] = (" ", "b")
        self.__compiled_results.append(turn_results)

    def display_results(self):
        for row in self.__compiled_results:
            print()
            for letter_index in row:
                if letter_index[1] == "g":
                    cprint(letter_index[0], 'white', 'on_green', end=" ")
                    continue
                if letter_index[1] == "y":
                    cprint(letter_index[0], 'white', 'on_yellow', end=" ")
                    continue
                cprint("_", "grey", 'on_white', end=" ")
        self.create_filler()

    def create_filler(self):
        print()
        remaining_rows = 6 - len(self.__compiled_results)
        for row in range(remaining_rows):
            for i in range(5):
                cprint("_", "grey", 'on_white', end=" ")
            print()
