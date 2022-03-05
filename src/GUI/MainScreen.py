from tkinter import *
from src.GUI.AnalysisScreen import AnalysisScreen
from src.GUI.Course_Info_Screen import CourseInfoScreen
from src.GUI.GUI_Controller import GUIController
from src.GUI.AbstractScreen import AbstractScreen
from src.GUI.Error_Screen import ErrorScreen
from src.GUI.TotalsScreen import TotalsScreen
from src.GUI.CreateCourseScreen import CreateCourseScreen
import tkinter.font as font


class MainScreen(AbstractScreen):
    def __init__(self) -> None:
        AbstractScreen.__init__(self)

        self.controller = GUIController()

        # =========================== Labels and Entries =======================
        self.welcome = \
            Label(self.window,
                  text="Welcome to the Mark book!\nPlease Select your action.",
                  font=('Helvetica', 18, 'bold'))

        self._entry_button = \
            Button(self.window, text="Add Entry", font=font.Font(size=16),
                   command=self.add_entry_to_mark_book)

        self._totals_button = \
            Button(self.window, text="Show Totals", font=font.Font(size=16),
                   command=self.show_totals)

        self._exit_button = \
            Button(self.window, text="Exit", font=font.Font(size=16),
                   command=self.window.destroy)

        self._creation_button = \
            Button(self.window, text="Create", font=font.Font(size=16),
                   command=self.create_all)

        # =============================== Placements ===========================
        self.welcome.grid(row=1, column=1)
        self._entry_button.grid(row=4, column=0)
        self._totals_button.grid(row=4, column=1)
        self._creation_button.grid(row=4, column=2)
        self._exit_button.grid(row=5, column=0)

    def add_entry_to_mark_book(self):
        self.controller.clear()
        screen = CourseInfoScreen(self.controller)
        screen.display()

    # def display_analysis(self):
    #     self.controller.clear()
    #     try:
    #         self.controller.calibrate(self._course_name_entry.get())
    #         analysis = self.controller.generate_analysis()
    #         screen = AnalysisScreen(analysis)
    #         screen.display()
    #     except FileNotFoundError:
    #         ErrorScreen("Course Not Found. Try again!").display()

    def show_totals(self):
        try:
            analysis = self.controller.get_totals()
            screen = TotalsScreen(analysis)
            screen.display()
        except FileNotFoundError:
            ErrorScreen("File Not Found. Try again!").display()

    def create_all(self):
        self.controller.clear()
        screen = CreateCourseScreen(self.controller)
        screen.display()


if __name__ == "__main__":
    app = MainScreen()
    app.display()
