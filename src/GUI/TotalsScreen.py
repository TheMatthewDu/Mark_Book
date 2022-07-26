from __future__ import annotations
from tkinter import *
from src.GUI.AbstractScreen import AbstractScreen
from src.GUI.GUIController import GUIController


class TotalsScreen(AbstractScreen):
    """ The screen to display the screens of the totals of all entries

    === Attributes ===
    :ivar controller: The GUI controller
    :ivar _totals_label: The label for the totals
    :ivar _exit_button: The button to exit the totals screen
    """
    controller: GUIController
    _totals_label: Label
    _exit_button: Button

    def __init__(self, controller: GUIController) -> None:
        """ Initializer

        :param controller: The GUI Controller
        """
        AbstractScreen.__init__(self)
        self.controller = controller

        self._totals_label = Label(self.window, text=self.controller.get_totals(), font=self.font)

        self._exit_button = \
            Button(self.window, text="Exit", font=self.button_font,
                   command=self.window.destroy)

        self._totals_label.grid(row=0, column=0)
        self._exit_button.grid(row=1, column=0)


if __name__ == "__main__":
    screen = TotalsScreen(GUIController())
    screen.display()
