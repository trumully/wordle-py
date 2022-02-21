"""
Wordle in Python.

by: Truman
"""
import tkinter as tk

from game import Game
from enum import Enum, auto


class WordleState(Enum):
    IDLE = auto()
    PLAYING = auto()
    COMPLETED = auto()


class TileState(Enum):
    BASE = auto()
    UNCERTAIN = auto()
    CERTAIN = auto()


class Wordle(Game):
    WINDOW_SIZE = 500

    def __init__(self, title: str = "Wordle", width: int = WINDOW_SIZE, 
                 height: int = WINDOW_SIZE):
        super().__init__(title, width, height)
        self.state = WordleState.IDLE

    def initialize(self):
        self.keyboard = Keyboard()

    def set_state(self, state: WordleState):
        self.state = state

    def update(self):
        super().update()

    def paint(self):
        super().paint()
        self.keyboard.paint(self.canvas)



class Keyboard:
    """The keyboard the player interacts with."""
    QWERTY_KEYBOARD = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    DVORAK_KEYBOARD = ["pyfgcrl", "aoeuidhtns", "qjkxbmvz"]
    BASE_SIZE = 50

    def __init__(self, keyboard_layout: list = QWERTY_KEYBOARD):
        self.keyboard_layout = keyboard_layout

    def update(self):
        pass

    def paint(self, canvas: tk.Canvas):
        padding = Keyboard.BASE_SIZE

        x = 0
        y = -padding

        for row in self.keyboard_layout:
            x = 0
            y += padding

            for letter in row:
                canvas.create_rectangle(x, y, 
                                        x+padding, y+padding, 
                                        outline="black")

                canvas.create_text(x + (padding / 2), y + (padding / 2), 
                                   text=letter)
                x += padding
            

def main():
    game = Wordle()
    game.initialize()
    game.run()


if __name__ == "__main__":
    main()
