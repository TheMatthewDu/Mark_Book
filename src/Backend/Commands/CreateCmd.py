from __future__ import annotations
from typing import Dict, Union, Optional
import json

from src.Backend.Commands.AbstractClasses import RequirePrompt
from src.Backend.Entities import MarkBookObject


GOAL = "GOAL"
FILENAME = "COURSE NAME"
DATA = "DATA"
WEIGHT = "WEIGHT"
CURRENT_MARK = "CURRENT MARK"


def load_json(data: dict, course_name: str) -> None:
    """ Loads data into a file named course_name

    :param data: The dict to load to a file
    :param course_name: The name of the course to load the data to
    :return: None
    """
    file = open(f"{course_name}.json", "w+")
    json.dump(data, file)
    file.close()


class CreateCmd(RequirePrompt):
    """ A Command object to create a new MarkBook File

    === Attributes ===
    :ivar storage_dict: Storage dictionary
    :ivar weights_dict: Weights dictionary
    """
    storage_dict: Optional[Dict[str, Union[float, list]]]
    weights_dict: Optional[Dict[str, float]]

    def __init__(self) -> None:
        """ Initializer """
        super().__init__()
        self.storage_dict = None
        self.weights = None

    def generate_prompt(self, data: MarkBookObject) -> Dict[str, str]:
        """ Generates a prompt based on a MarkBookObject

        :param data: The MarkBookObject
        :return: The dict of correspondences
        """
        prompt_data = {
            FILENAME: input("Enter Course Name: "),
            GOAL: input("Enter goal: ")
        }

        n = 0
        while True:
            include_name = input("Enter the category (e.g, Test, Assignment). Enter 'exit' to exit: ")
            if include_name == "exit":
                break

            include_weight = input("Enter the weight (as a percentage. e,g, 50 for 50%). Enter 'exit' to exit: ")
            if include_weight == "exit":
                break

            prompt_data[f"{DATA}{n}"] = include_name
            prompt_data[f"{WEIGHT}{n}"] = include_weight

            n += 1
        return prompt_data

    def run(self) -> None:
        """ Generates the new file

        Creates a storage and weight dictionary
        """
        assert self._raw_data is not None

        self.storage_dict = {CURRENT_MARK: 100.0, GOAL: float(self._raw_data[GOAL])}
        self.weights_dict = {}
        for n in range((len(self._raw_data.keys()) - 4) // 2 + 1):
            entry_name = self._raw_data[f"{DATA}{n}"]

            self.storage_dict[entry_name] = []
            self.weights_dict[entry_name] = float(self._raw_data[f"{WEIGHT}{n}"])

        load_json(self.storage_dict, f"src\\Datafiles\\Data\\{self._raw_data[FILENAME]}")
        load_json(self.weights_dict, f"src\\Datafiles\\Weights\\{self._raw_data[FILENAME]}_weights")

    def set_mark_book_object(self) -> MarkBookObject:
        curr_mark = self.storage_dict.pop(CURRENT_MARK)
        goal = self.storage_dict.pop(GOAL)

        return MarkBookObject(self._raw_data[FILENAME], self.storage_dict, self.weights_dict, curr_mark, goal)