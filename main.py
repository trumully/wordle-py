"""
Wordle in Python.

by: Truman
"""

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure root window
        self.title("Wordle")
        self.geometry("1280x720")

        # label
        self._label = ttk.Label(self, text="Hello, Wordle!")
        self._label.pack()

        # button
        self._button = ttk.Button(self, text="Click me")
        self._button["command"] = self.__button_clicked
        self._button.pack()

    def __button_clicked(self):
        showinfo(title="Information", message="Hello, Wordle!")


def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()

