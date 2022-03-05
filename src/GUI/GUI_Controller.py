from typing import Tuple, Any, List, Dict
from src.Backend import Markbook
from src.Backend import Calculate_Overall
from src.Backend.DataInput import DataInput


class GUIController:
    def __init__(self):
        self.name = None
        self.data = None

    def clear(self):
        self.name = None
        self.data = None

    def calibrate(self, name: str):
        if not self.is_calibrated():
            self.name = name
            filename = Markbook.check_course_code(name)
            self.data = Markbook.read(filename)

    def is_calibrated(self):
        return self.data is not None and self.name is not None

    def get_data(self):
        return self.data

    def enter_data(self, data: Tuple[Any, Any, Any]):
        data_input = DataInput(self.data)
        return data_input.gui_input_data(data)

    def generate_analysis(self):
        return [(self.name, "")] + self.data.to_gui()

    def write_data(self):
        Markbook.write_data(self.data, self.name)

    def get_totals(self):
        Calculate_Overall.main()
        file = open("Backend\\Overall Averages.txt")
        return file.read()

    def create_object(self, keys: Dict[str, float], filename: str, goal: float):
        data = {"CURRENT MARK": 100.0, "GOAL": float(goal)}
        weights = {}
        for item in keys:
            data[item] = []
            weights[item] = keys[item]

        Markbook.load_json(data, f"Datafiles\\Data\\{filename}")
        Markbook.load_json(weights, f"Datafiles\\Weights\\{filename}_weights")
