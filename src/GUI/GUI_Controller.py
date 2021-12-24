from typing import Tuple, Any
from src.Backend import Markbook


class GUIController:
    def __init__(self):
        self.name = None
        self.data = None

    def calibrate(self, name: str):
        self.name = name
        filename = Markbook.check_course_code(name)
        self.data = Markbook.read(filename)

    def get_data(self):
        return self.data

    def enter_data(self, data: Tuple[Any, Any, Any]):
        data_input = Markbook.DataInput(self.data)
        return data_input.gui_input_data(data)

    def generate_analysis(self):
        return [(self.name, "")] + self.data.to_gui()

    def write_data(self):
        Markbook.write_data(self.data, self.name)

    def get_totals(self):
        file = open("Backend\\Overall Averages.txt")
        return file.read()
