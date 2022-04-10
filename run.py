import helpers
from game import Wordle
from player import Player


def main():
        player = Player()
        print("Welcome to Python Wordle")
        while True:
            game = Wordle(helpers.read_word_list("wordle-answers-alphabetical.txt"), player)
            game.play()
            print("Starting another game")
            print()


if __name__ == "__main__":
    main()