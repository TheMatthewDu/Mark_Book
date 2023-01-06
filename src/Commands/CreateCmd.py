from __future__ import annotations
from typing import Dict, Union, Optional
import json
import re

from Commands.AbstractClasses import RequirePrompt
from Entities import MarkBookObject
from src.constants import *


def load_json(data: dict, course_name: str) -> None:
    """ Loads data into a file named course_name

    :param data: The dict to load to a file
    :param course_name: The name of the course to load the data to
    :return: None
    """
    file = open(f"{course_name}.json", "w+")
    json.dump(data, file)
    file.close()


def check_course_code(code: str) -> str:
    """ Check if the code is valid. Fix if not

    :param: code: the code entered by the user

    :return: a correctly formatted course code
    """
    if not re.match("([A-Z]|[a-z]){3}\\d{3}(H|h|)(1|3|5|)$", code):
        raise FileNotFoundError

    copy_of_code = code
    if copy_of_code[:3].islower():
        copy_of_code = copy_of_code[:3].upper() + copy_of_code[3:]
    if len(copy_of_code) == 6:
        copy_of_code = copy_of_code + 'H1'
    if copy_of_code[:-2] == 'h1':
        copy_of_code = copy_of_code[:-2] + 'H1'
    return copy_of_code


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
            COURSE_NAME: input("Enter Course Name: "),
            GOAL: input("Enter goal: "),
            DATA: [],
            WEIGHT: []
        }

        total_weight = 0.0
        n = 0
        while True:
            print(f"Percentage remaining {round(total_weight, 2)}")

            include_name = input("Enter the category (e.g, Test, Assignment). Enter 'exit' to exit: ")
            if include_name == "exit":
                break

            include_weight = input("Enter the weight (as a percentage. e,g, 50 for 50%). Enter 'exit' to exit: ")
            while not include_weight.isdecimal() and include_weight != "exit":
                print("Invalid Input. Try again!")
                include_weight = input("Enter the weight (as a percentage. e,g, 50 for 50%). Enter 'exit' to exit: ")

            if include_weight == "exit":
                break

            prompt_data[DATA].append(include_name)
            prompt_data[WEIGHT].append(include_weight)

            n += 1
            total_weight += float(include_weight)

        return prompt_data

    def run(self) -> None:
        """ Generates the new file

        Creates a storage and weight dictionary
        """
        assert self._raw_data is not None

        self.storage_dict = {CURRENT_MARK: 100.0, GOAL: float(self._raw_data[GOAL])}
        self.weights_dict = {}

        data_lst = self._raw_data[DATA]
        weight_lst = self._raw_data[WEIGHT]
        for n in range(len(data_lst)):
            entry_name = data_lst[n]

            self.storage_dict[entry_name] = []
            self.weights_dict[entry_name] = float(weight_lst[n])

        course_name = check_course_code(self._raw_data[COURSE_NAME])
        load_json(self.storage_dict, f"data\\Data\\{course_name}")
        load_json(self.weights_dict, f"data\\Weights\\{course_name}_weights")

    def set_mark_book_object(self) -> MarkBookObject:
        return MarkBookObject(self._raw_data[COURSE_NAME], self.storage_dict, self.weights_dict)