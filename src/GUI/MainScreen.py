from tkinter import *
from src.GUI.AnalysisScreen import AnalysisScreen
from src.GUI.SelectionScreen import SelectionScreen
from src.GUI.GUI_Controller import GUIController
from src.GUI.AbstractScreen import AbstractScreen
from src.GUI.Error_Screen import ErrorScreen
from src.GUI.TotalsScreen import TotalsScreen
from src.GUI.CreateCourseScreen import CreateCourseScreen


class MainScreen(AbstractScreen):
    def __init__(self) -> None:
        AbstractScreen.__init__(self)

        self.controller = GUIController()

        # =========================== Labels and Entries =======================
        self._course_name_label = \
            Label(self.window, text="Course Name", font=self.font)

        self._course_name_entry = Entry(self.window, font=self.font)

        # ============================== Buttons ===============================
        self._entry_button = \
            Button(self.window, text="Add Entry", font=self.button_font,
                   command=self.add_entry_to_mark_book)

        self._analysis_button = \
            Button(self.window, text="Show Analysis", font=self.button_font,
                   command=self.display_analysis)

        self._totals_button = \
            Button(self.window, text="Show Totals", font=self.button_font,
                   command=self.show_totals)

        self._exit_button = \
            Button(self.window, text="Exit", font=self.button_font,
                   command=self.window.destroy)

        self._creation_button = \
            Button(self.window, text="Create", font=self.button_font,
                   command=self.create_all)

        # =============================== Placements ===========================
        self._course_name_label.grid(row=0, column=0)
        self._course_name_entry.grid(row=0, column=1)
        self._entry_button.grid(row=4, column=0)
        self._totals_button.grid(row=4, column=1)
        self._analysis_button.grid(row=5, column=0)
        self._creation_button.grid(row=5, column=1)
        self._exit_button.grid(row=6, column=0)

    def add_entry_to_mark_book(self):
        try:
            self.controller.calibrate(self._course_name_entry.get())
            data = self.controller.get_data()
            SelectionScreen(data, self.controller).display()
        except FileNotFoundError:
            ErrorScreen("Course Not Found. Try again!").display()

    def display_analysis(self):
        try:
            self.controller.calibrate(self._course_name_entry.get())
            analysis = self.controller.generate_analysis()
            screen = AnalysisScreen(analysis)
            screen.display()
        except FileNotFoundError:
            ErrorScreen("Course Not Found. Try again!").display()

    def show_totals(self):
        try:
            analysis = self.controller.get_totals()
            screen = TotalsScreen(analysis)
            screen.display()
        except FileNotFoundError:
            ErrorScreen("File Not Found. Try again!").display()

    def create_all(self):
        screen = CreateCourseScreen(self.controller)
        screen.display()


if __name__ == "__main__":
    app = MainScreen()
    app.display()
