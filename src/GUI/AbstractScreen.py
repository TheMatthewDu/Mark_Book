from tkinter import *
import tkinter.font as font


class AbstractScreen():
    def __init__(self):
        self.window = Tk()
        self.window.title(self.__class__.__name__)
        self.font = font.Font(size=18)
        self.button_font = font.Font(size=16)

    def display(self) -> None:
        self.window.mainloop()
