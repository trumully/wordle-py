"""
Wordle in Python.

by: Truman
"""
from game import Game
from enum import Enum, auto


class WordleState(Enum):
    IDLE = auto()
    PLAYING = auto()
    COMPLETED = auto()


class Wordle(Game):
    WINDOW_TITLE = "Wordle"
    WINDOW_SIZE = 500

    def __init__(self):
        super().__init__(Wordle.WINDOW_TITLE, Wordle.WINDOW_SIZE, 
                         Wordle.WINDOW_SIZE,
                        )
        self.state = WordleState.IDLE

    def set_state(self, state: WordleState):
        self.state = state

    def update(self):
        super().update()

    def paint(self):
        super().paint()


def main():
    game = Wordle()
    game.run()


if __name__ == "__main__":
    main()
