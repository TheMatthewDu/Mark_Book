from tkinter import *
from src.GUI.GUIController import GUIController
from src.GUI.AnalysisScreen import AnalysisScreen
from src.GUI.AbstractScreen import AbstractScreen


class SelectionScreen(AbstractScreen):
    """ The course Selection Screen

    === Attributes ===
    :ivar controller: The GUI controller
    :ivar _assignment_type_label: The label for the assignment type dropdown
    :ivar _description_label: The label for the description of the mark entry
    :ivar _mark_label: The label for the mark entry bar
    :ivar _assignment_type_entry: The dropdown bar for the assignment type
    :ivar _drop_down: The dropdown menu object for the assignment type
    :ivar _description_entry: The entry bar for the description of the mark
    :ivar _mark_entry: The entry bar for the mark
    :ivar _submit_button: The button to submit the form
    :ivar _exit_button: The button to exit the screen
    """
    controller: GUIController
    _assignment_type_label: Label
    _description_label: Label
    _mark_label: Label
    _assignment_type_entry: StringVar
    _drop_down: OptionMenu
    _description_entry: Entry
    _mark_entry: Entry
    _submit_button: Button
    _exit_button: Button

    def __init__(self, controller: GUIController) -> None:
        AbstractScreen.__init__(self)

        # ===================== Things passed on ===============================
        self.controller = controller

        # =============================== Labels ===============================
        self._assignment_type_label = \
            Label(self.window, text="Assignment Type", font=self.font)

        self._description_label = \
            Label(self.window, text="Description", font=self.font)

        self._mark_label = Label(self.window, text="Mark", font=self.font)

        # ============================= Entries ================================
        self._assignment_type_entry = StringVar(name="Select")

        list_of_entries = self.controller.get_list_elements().split(sep=',')
        self._drop_down = \
            OptionMenu(self.window, self._assignment_type_entry,
                       *list_of_entries)

        self._description_entry = Entry(self.window, font=self.font)

        self._mark_entry = Entry(self.window, font=self.font)

        # ================================ Buttons =============================
        self._submit_button = \
            Button(self.window, text="Submit", font=self.button_font,
                   command=self.submit_button_callback)

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

    def submit_button_callback(self) -> None:
        """ The callback function for the actions after the submit button is pressed

        :return: Nothing
        """
        # Get and display the response data
        self.controller.enter_data(self._assignment_type_entry.get(), self._description_entry.get(), self._mark_entry.get())
        confirm_message = Label(self.window, text=f"Now inputting {self._mark_entry.get()}%", font=self.font)

        # Display a confirm button
        confirm_button = \
            Button(self.window, text="Ok", font=self.button_font,
                   command=self.launch_analysis_screen)

        # Position the new buttons and labels
        confirm_message.grid(row=5, column=0)
        confirm_button.grid(row=6, column=0)

    def launch_analysis_screen(self) -> None:
        """ Launch the analysis screen

        :return: Nothing. Launch the analysis screen
        """
        analysis_screen = AnalysisScreen(self.controller)
        analysis_screen.display()


if __name__ == "__main__":
    screen = SelectionScreen(GUIController())
    screen.display()
