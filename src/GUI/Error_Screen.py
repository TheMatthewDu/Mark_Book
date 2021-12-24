from __future__ import annotations
from tkinter import *
from src.GUI.AbstractScreen import AbstractScreen


class ErrorScreen(AbstractScreen):
    def __init__(self, message: str):
        AbstractScreen.__init__(self)
        self._message = Label(self.window, text=message, font=self.font)

        self._confirmation = \
            Button(self.window, text="Ok", font=self.button_font,
                   command=self.window.destroy)

        self._message.grid(row=0, column=0)
        self._confirmation.grid(row=1, column=0)


if __name__ == "__main__":
    screen = ErrorScreen("Hello")
    screen.display()
