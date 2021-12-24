from __future__ import annotations
from tkinter import *
from src.GUI.AbstractScreen import AbstractScreen


class TotalsScreen(AbstractScreen):
    def __init__(self, text: str):
        AbstractScreen.__init__(self)

        self._totals_label = Label(self.window, text=text, font=self.font)

        self._exit_button = \
            Button(self.window, text="Exit", font=self.button_font,
                   command=self.window.destroy)

        self._totals_label.grid(row=0, column=0)
        self._exit_button.grid(row=1, column=0)


if __name__ == "__main__":
    screen = TotalsScreen("Hi")
    screen.display()
