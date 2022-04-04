from termcolor import colored, cprint
class Wordle:
    def __init__(self, word):
        self.word = word
        self.__guesses_remaining = 6
        self.found_letters = ["", "", "", "", ""]
        self.exact_position_letters = ["", "", "", "", ""]
        # self.display_results =  ["", "", "", "", ""]



    def check_guess(self, guess):
        for index, letter in enumerate(guess):
            print(index)
            if letter == self.word[index]:
                print("Index:" + letter)
                self.exact_position_letters[index] = letter
        for index, letter in enumerate(guess):
            if letter in self.word and (self.exact_position_letters.count(letter) + self.found_letters.count(letter))  < self.word.count(letter):
                print("exact letter count:" + str(self.exact_position_letters.count(letter)) + " " + letter)
                print("letter in word count: " + str(self.word.count(letter)) + " " + letter)
                self.found_letters[index] = letter

    def display_results(self):
        for i in range(5):
            if self.found_letters[i] != "":
                cprint(self.found_letters[i], 'white', 'on_yellow', end=" ")
                continue
            if self.exact_position_letters[i] != "":
                cprint(self.exact_position_letters[i], 'white', 'on_green', end=" ")
                continue
            cprint(" ", "white", 'on_white', end=" ")












