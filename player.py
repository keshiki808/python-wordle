class Player:
    def __init__(self):
        self.__guesses_remaining = 6
        self.__win_count = 0
        self.__game_count = 0
        self.__win_rate = self.determine_win_rate()
        self.__guess = ""

    @property
    def win_count(self):
        return self.__win_count

    @win_count.setter
    def win_count(self, new_win_count):
        self.__win_count = new_win_count

    @property
    def game_count(self):
        return self.__game_count

    @game_count.setter
    def game_count(self, new_game_count):
        self.__game_count = new_game_count

    @property
    def win_rate(self):
        return self.__win_rate

    @property
    def guesses_remaining(self):
        return self.__guesses_remaining

    @guesses_remaining.setter
    def guesses_remaining(self, new_guess_remaining_count):
        self.__guesses_remaining = new_guess_remaining_count

    @property
    def guess(self):
        return self.__guess

    @guess.setter
    def guess(self, guess):
        self.__guess = guess

    def determine_win_rate(self):
        if self.__game_count == 0:
            return 0
        return self.__win_count / self.__game_count * 100

    def make_guess(self):
        self.__guess = input()
