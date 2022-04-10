import helpers
from game import Wordle
from player import Player


def main():
        player = Player()
        while True:
            game = Wordle(helpers.read_word_list("wordle-answers-alphabetical.txt"), player)
            game.play()


if __name__ == "__main__":
    main()