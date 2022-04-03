class Wordle:
    def __init__(self, word):
        self.__word = word
        self.__guesses_remaining = 6
        self.__found_letters = ["","","","",""]
        self.__exact_position_letters = ["","","","",""]
        self.__display_results =  ["","","","",""]



    def check_guess(self, guess):
        for index, letter in enumerate(guess):
            if letter == self.__word[index]:
                self.__exact_position_letters[index] = letter
            elif letter in guess:
                self.__found_letters[index] = letter





