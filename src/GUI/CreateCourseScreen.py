from tkinter import *
from typing import List, Tuple

from src.GUI.GUIController import GUIController
from src.GUI.AbstractScreen import AbstractScreen


class CreateCourseScreen(AbstractScreen):
    """ A screen to create a new course entry
    
    === Attributes ===
    :ivar controller: The GUI Controller
    :ivar _names: The list of entries of the names of the new entry
    :ivar _weights: The list of entries of the weights of the new entry
    :ivar _course_name_label: The label for the entry bar for the course name
    :ivar _goal_label: The label for the entry bar for the course goal
    :ivar _group_name_header_label: The label of the header of the left column of the form; specifies the name of the 
        groups
    :ivar _weights_header_label: The label of the header of the right column of the form; specifies the weight of the 
        groups
    :ivar _course_name_entry: The entry bar for the course name
    :ivar _goal_entry: The entry bar for the goal
    :ivar _current_row: The current last row of the new entry
    :ivar _submit_button: The button to confirm all changes and submit the form
    :ivar _exit_button: The button to exit the screen
    :ivar _add_button: The button to create a new row in the form
    """
    controller: GUIController
    _names: List[Entry]
    _weights: List[Entry]
    _course_name_label: Label
    _goal_label: Label
    _group_name_header_label: Label
    _weights_header_label: Label
    _course_name_entry: Entry
    _goal_entry: Entry
    _current_row: int
    _submit_button: Button
    _exit_button: Button
    _add_button: Button

    def __init__(self, controller: GUIController) -> None:
        """ Initializer

        :param controller: The GUI controllers
        """
        AbstractScreen.__init__(self)
        self.controller = controller

        # =============================== Labels ===============================
        self._names = []
        self._weights = []

        self._course_name_label = Label(self.window, text="Course Name", font=self.font)
        self._goal_label = Label(self.window, text="Goal", font=self.font)
        self._group_name_header_label = Label(self.window, text="Group Name", font=self.font)
        self._weights_header_label = Label(self.window, text="Weight", font=self.font)

        self._course_name_entry = Entry(self.window, font=self.font)
        self._goal_entry = Entry(self.window, font=self.font)

        self._current_row = 3
        for _ in range(6):
            self.create_new_rows()

        self._course_name_label.grid(row=0, column=0)
        self._course_name_entry.grid(row=0, column=1)
        self._goal_label.grid(row=1, column=0)
        self._goal_entry.grid(row=1, column=1)
        self._group_name_header_label.grid(row=2, column=0)
        self._weights_header_label.grid(row=2, column=1)

        # ================================ Buttons =============================
        self._submit_button = \
            Button(self.window, text="Submit", font=self.button_font,
                   command=self.send_response)

        self._exit_button = \
            Button(self.window, text="Exit", font=self.button_font,
                   command=self.window.destroy)

        self._add_button = \
            Button(self.window, text="Add", font=self.button_font,
                   command=self.readjust_screen)

        self._submit_button.grid(row=self._current_row + 2, column=0)
        self._exit_button.grid(row=self._current_row + 2, column=1)
        self._add_button.grid(row=self._current_row + 1, column=0)

    def readjust_screen(self) -> None:
        """ Readjust the screen after creating new rows

        :return: Nothing
        """
        self.create_new_rows()
        self._submit_button.grid(row=self._current_row + 2, column=0)
        self._exit_button.grid(row=self._current_row + 2, column=1)
        self._add_button.grid(row=self._current_row + 1, column=0)

    def create_new_rows(self) -> None:
        """ Create a new row in the form

        :return: Nothing
        """
        new_name_entry = Entry(self.window, font=self.font)
        new_desc_entry = Entry(self.window, font=self.font)

        new_name_entry.grid(row=self._current_row, column=0)
        new_desc_entry.grid(row=self._current_row, column=1)

        self._current_row += 1

        self._names.append(new_name_entry)
        self._weights.append(new_desc_entry)

    def _get_inputs_list(self) -> List[Tuple[str, str]]:
        """ Generates the input dictionary based on the form data

        :return: THe input dictionary, which is a dictionary of the entry name to the weight
        """
        input_list = []
        for i in range(len(self._names)):
            curr_name = self._names[i].get()
            curr_weight = self._weights[i].get()

            if curr_weight != '':
                input_list.append((curr_name, curr_weight))

        return input_list

    def send_response(self) -> None:
        """ Processes the form and creates the .json file

        :return: Nothing
        """
        info = self._get_inputs_list()
        self.controller.create_course(info, self._course_name_entry.get(), self._goal_entry.get())
        self.window.destroy()


if __name__ == "__main__":
    screen = CreateCourseScreen(GUIController())
    screen.display()
