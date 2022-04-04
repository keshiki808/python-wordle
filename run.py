import helpers
from game import Wordle
from termcolor import colored, cprint

def main():
    random_word = helpers.read_word_list("wordle-answers-alphabetical.txt")
    print(random_word)
    # cprint("Testing", f'{letter}', 'on_yellow')
    # cprint("Testing", "white", 'on_red')
    testy = Wordle("sweet")
    testy.check_guess("shave")
    testy.display_results()
    print()
    print(testy.found_letters)
    # print(testy.display_results)
    print(testy.exact_position_letters)


if __name__ == "__main__":
    main()