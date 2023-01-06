from tkinter import *
# from src.GUI.AnalysisScreen import AnalysisScreen
from src.GUI.CourseInfoScreen import CourseInfoScreen
from src.GUI.GUIController import GUIController
from src.GUI.AbstractScreen import AbstractScreen
from src.GUI.ErrorScreen import ErrorScreen
from src.GUI.TotalsScreen import TotalsScreen
from src.GUI.CreateCourseScreen import CreateCourseScreen
import tkinter.font as font


class MainScreen(AbstractScreen):
    """ The main screen for the MarkBook GUI

    === Attributes ===
    :ivar controller: The GUI controller of the system
    :ivar _welcome: The label for the screen to welcome
    :ivar _entry_button: The button to move to the CourseInfoScreen
    :ivar _totals_button: The button to move to the TotalsScreen
    :ivar _exit_button: The button to exit the program
    :ivar _creation_button: The button to move to the CreateCourseScreen
    """
    controller: GUIController
    _welcome: Label
    _entry_button: Button
    _totals_button: Button
    _exit_button: Button
    _creation_button: Button

    def __init__(self) -> None:
        """ Initializer """
        AbstractScreen.__init__(self)

        self.controller = GUIController()

        # =========================== Labels and Entries =======================
        self._welcome = \
            Label(self.window,
                  text="Welcome to the Mark book!\nPlease Select your action.",
                  font=('Helvetica', 18, 'bold'))

        self._entry_button = \
            Button(self.window, text="Add Entry", font=font.Font(size=16),
                   command=self.launch_course_info_screen)

        self._totals_button = \
            Button(self.window, text="Show Totals", font=font.Font(size=16),
                   command=self.launch_totals_screen)

        self._exit_button = \
            Button(self.window, text="Exit", font=font.Font(size=16),
                   command=self.process_exit)

        self._creation_button = \
            Button(self.window, text="Create", font=font.Font(size=16),
                   command=self.launch_create_course_screen)

        # =============================== Placements ===========================
        self._welcome.grid(row=1, column=1)
        self._entry_button.grid(row=4, column=0)
        self._totals_button.grid(row=4, column=1)
        self._creation_button.grid(row=4, column=2)
        self._exit_button.grid(row=5, column=0)

    def launch_course_info_screen(self) -> None:
        """ Launch the course information screen

        :return: Nothing. Launches the course info screen
        """
        screen = CourseInfoScreen(self.controller)
        screen.display()

    def launch_totals_screen(self) -> None:
        """ Launch the totals screen

        :return: Nothing. Launch the totals screen
        """
        try:
            screen = TotalsScreen(self.controller)
            screen.display()
        except FileNotFoundError:
            ErrorScreen("File Not Found. Try again!").display()

    def launch_create_course_screen(self) -> None:
        """ Launch the create course screen

        :return: Nothing. Launches the create course screen
        """
        screen = CreateCourseScreen(self.controller)
        screen.display()

    def process_exit(self):
        self.controller.commit_changes()
        self.window.destroy()


if __name__ == "__main__":
    app = MainScreen()
    app.display()
