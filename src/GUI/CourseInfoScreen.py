from __future__ import annotations
from tkinter import *
import tkinter.font as font
from src.GUI.AnalysisScreen import AnalysisScreen
from src.GUI.SelectionScreen import SelectionScreen
from src.GUI.GUIController import GUIController
from src.GUI.AbstractScreen import AbstractScreen
from src.GUI.ErrorScreen import ErrorScreen
from src.GUI.TotalsScreen import TotalsScreen


class CourseInfoScreen(AbstractScreen):
    """ The course information screen. Selects a course from those available

    === Attributes ===
    :ivar controller: The GUI controller
    :ivar _course_name_label: The label for the course name
    :ivar _course_name_entry: The entry bar for the course name
    :ivar _entry_button: The button to move to the SelectionScreen
    :ivar _analysis_button: The button to move to the AnalysisScreen
    :ivar _exit_button: The button to exit this screen
    """
    controller: GUIController
    _course_name_label: Label
    _course_name_entry: Entry
    _entry_button: Button
    _analysis_button: Button
    _exit_button: Button

    def __init__(self, controller: GUIController) -> None:
        """ Initializer.

        :param controller: The GUI controller that is being passed around
        """
        AbstractScreen.__init__(self)

        self.controller = controller

        # =========================== Labels and Entries =======================
        self._course_name_label = \
            Label(self.window, text="Course Name", font=font.Font(size=18))

        self._course_name_entry = Entry(self.window, font=font.Font(size=18))

        # ============================== Buttons ===============================
        self._entry_button = \
            Button(self.window, text="Add Entry", font=font.Font(size=16),
                   command=self.launch_selection_screen)

        self._analysis_button = \
            Button(self.window, text="Show Analysis", font=font.Font(size=16),
                   command=self.launch_analysis_screen)

        self._exit_button = \
            Button(self.window, text="Exit", font=font.Font(size=16),
                   command=self.window.destroy)

        # =============================== Placements ===========================
        self._course_name_label.grid(row=0, column=0)
        self._course_name_entry.grid(row=0, column=1)
        self._entry_button.grid(row=4, column=0)
        self._analysis_button.grid(row=4, column=1)
        self._exit_button.grid(row=5, column=0)

    def launch_selection_screen(self) -> None:
        """ Launch the course selection screen

        :return: None. Launches the selection screen
        """
        try:
            self.controller.set_course(self._course_name_entry.get())
            SelectionScreen(self.controller).display()
        except FileNotFoundError:
            ErrorScreen("Course Not Found. Try again!").display()

    def launch_analysis_screen(self) -> None:
        """ Launch the analysis screen

        :return: Nothing. Launches the analysis screen
        """
        try:
            self.controller.set_course(self._course_name_entry.get())
            screen = AnalysisScreen(self.controller)
            screen.display()
        except FileNotFoundError:
            ErrorScreen("Course Not Found. Try again!").display()

    def launch_totals_screen(self) -> None:
        """ Launch the totals screen

        :return: Nothing. Launches the totals screen
        """
        try:
            screen = TotalsScreen(self.controller)
            screen.display()
        except FileNotFoundError:
            ErrorScreen("File Not Found. Try again!").display()


if __name__ == "__main__":
    app = CourseInfoScreen(GUIController())
    app.display()
