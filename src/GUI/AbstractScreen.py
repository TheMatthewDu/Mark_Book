from tkinter import *
import tkinter.font as ft


class AbstractScreen:
    """ An Abstract Tkinter screen

    === Attributes ===
    :ivar window: The Tkinter window
    :ivar font: The font of the labels
    """
    window: Tk
    font: ft.Font
    button_font: ft.Font

    def __init__(self) -> None:
        """ Initializer """
        self.window = Tk()
        self.font = ft.Font(size=18)
        self.button_font = ft.Font(size=16)

        self.window.title(self.__class__.__name__)

    def display(self) -> None:
        """ Display the screen

        :return: Nothing
        """
        self.window.mainloop()
