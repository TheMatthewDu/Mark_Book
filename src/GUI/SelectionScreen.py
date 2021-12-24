from tkinter import *
from src.Backend.DataObject import DataObject
from src.GUI.GUI_Controller import GUIController
from src.GUI.AnalysisScreen import AnalysisScreen
from src.GUI.AbstractScreen import AbstractScreen


class SelectionScreen(AbstractScreen):
    def __init__(self, data_obj: DataObject, controller: GUIController) -> None:
        AbstractScreen.__init__(self)

        # ===================== Things passed on ===============================
        self.data_obj = data_obj
        self.controller = controller

        # =============================== Labels ===============================
        self._assignment_type_label = \
            Label(self.window, text="Assignment Type", font=self.font)

        self._description_label = \
            Label(self.window, text="Description", font=self.font)

        self._mark_label = Label(self.window, text="Mark", font=self.font)

        # ============================= Entries ================================
        self.assignment_type_entry = StringVar(name="Select")

        list_of_entries = self.data_obj.to_list()
        self._drop_down = \
            OptionMenu(self.window, self.assignment_type_entry,
                       *list_of_entries)

        self._description_entry = Entry(self.window, font=self.font)

        self._mark_entry = Entry(self.window, font=self.font)

        # ================================ Buttons =============================
        self._submit_button = \
            Button(self.window, text="Submit", font=self.button_font,
                   command=self.send_response)

        self._exit_button = \
            Button(self.window, text="Exit", font=self.button_font,
                   command=self.window.destroy)

        # =========================== Placements ===============================
        self._assignment_type_label.grid(row=0, column=0)
        self._drop_down.grid(row=0, column=1)
        self._description_label.grid(row=1, column=0)
        self._description_entry.grid(row=1, column=1)
        self._mark_label.grid(row=2, column=0)
        self._mark_entry.grid(row=2, column=1)
        self._submit_button.grid(row=4, column=0)
        self._exit_button.grid(row=4, column=1)

    def send_response(self):
        response = (self.assignment_type_entry.get(),
                    self._description_entry.get(),
                    self._mark_entry.get())

        # Get and display the response data
        value = self.controller.enter_data(response)
        confirm_message = Label(self.window, text=value, font=self.font)

        # Display a confirm button
        confirm_button = \
            Button(self.window, text="Ok", font=self.button_font,
                   command=self.generate_analysis)

        confirm_message.grid(row=5, column=0)
        confirm_button.grid(row=6, column=0)

    def generate_analysis(self):
        self.controller.write_data()
        analysis = self.controller.generate_analysis()
        analysis_screen = AnalysisScreen(analysis)
        analysis_screen.display()


if __name__ == "__main__":
    pass
