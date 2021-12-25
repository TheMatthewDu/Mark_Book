from tkinter import *
from src.Backend.DataObject import DataObject
from src.GUI.GUI_Controller import GUIController
from src.GUI.AnalysisScreen import AnalysisScreen
from src.GUI.AbstractScreen import AbstractScreen


class CreateCourseScreen(AbstractScreen):
    def __init__(self, controller: GUIController) -> None:
        AbstractScreen.__init__(self)
        self.controller = controller

        # =============================== Labels ===============================
        self._names = []
        self._weights = []

        course_name_label = Label(self.window, text="Course Name", font=self.font)
        course_name_label.grid(row=0, column=0)

        self.course_name_entry = Entry(self.window, font=self.font)
        self.course_name_entry.grid(row=0, column=1)

        goal_label = Label(self.window, text="Goal", font=self.font)
        goal_label.grid(row=1, column=0)

        self.goal_entry = Entry(self.window, font=self.font)
        self.goal_entry.grid(row=1, column=1)

        self._curr_name_pos = 3

        header_left = Label(self.window, text="Group Name", font=self.font)
        header_left.grid(row=2, column=0)

        header_right = Label(self.window, text="Weight", font=self.font)
        header_right.grid(row=2, column=1)

        for _ in range(6):
            self.add_more()

        # ================================ Buttons =============================
        self._submit_button = \
            Button(self.window, text="Submit", font=self.button_font,
                   command=self.send_response)

        self._exit_button = \
            Button(self.window, text="Exit", font=self.button_font,
                   command=self.window.destroy)

        self._add_button = \
            Button(self.window, text="Add", font=self.button_font,
                   command=self.add_row)

        self._submit_button.grid(row=self._curr_name_pos + 2, column=0)
        self._exit_button.grid(row=self._curr_name_pos + 2, column=1)
        self._add_button.grid(row=self._curr_name_pos + 1, column=0)

    def add_row(self):
        self.add_more()
        self._submit_button.grid(row=self._curr_name_pos + 2, column=0)
        self._exit_button.grid(row=self._curr_name_pos + 2, column=1)
        self._add_button.grid(row=self._curr_name_pos + 1, column=0)

    def add_more(self):
        new_name_entry = Entry(self.window, font=self.font)
        new_desc_entry = Entry(self.window, font=self.font)

        new_name_entry.grid(row=self._curr_name_pos, column=0)
        new_desc_entry.grid(row=self._curr_name_pos, column=1)

        self._curr_name_pos += 1

        self._names.append(new_name_entry)
        self._weights.append(new_desc_entry)

    def _organize_data(self):
        data = {}
        for i in range(len(self._names)):
            item = self._weights[i].get()
            if item != '':
                data[self._names[i].get()] = float(item)
        return data

    def send_response(self):
        info = self._organize_data()
        self.controller.create_object(info, self.course_name_entry.get(),
                                      self.goal_entry.get())
        self.window.destroy()


if __name__ == "__main__":
    screen = CreateCourseScreen(GUIController())
    screen.display()
