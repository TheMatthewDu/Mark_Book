from __future__ import annotations
from typing import List, Dict, Tuple, Optional
import json
import re

from Commands.AbstractClasses.Command import Command
from Entities.MarkBookObject import MarkBookObject


def _backup(name: str, dict_type: str) -> None:
    """ Quick Backup

    :param name: The name of the course to back up
    :param dict_type: The type of backup. A weight or data file
    :return: Nothing
    """
    backup = open(f"backup\\{name}_BACKUP.json", 'w')
    file = open(f"data\\{dict_type}\\{name}.json", 'r')

    backup_read = json.load(file)
    json.dump(backup_read, backup)

    file.close()
    backup.close()


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


class DataReaderCmd(Command):
    """ A command to read data

    :ivar course_name
    :ivar storage
    :ivar weights
    """
    course_name: str
    storage: Dict[str, List[Tuple[str, float]]]
    weights: Dict[str, float]

    def __init__(self, course_name: str) -> None:
        """ Initializer """
        self.course_name = check_course_code(course_name)
        self.weights = {}
        self.storage = {}

    def get_storage_json(self) -> None:
        """ Get the storage JSON

        :return: None
        """
        _backup(self.course_name, "Data")
        storage_file = open(f"data\\Data\\{self.course_name}.json")
        self.storage = json.load(storage_file)

    def get_weights_json(self) -> None:
        """ Get the storage JSON

        :return: None
        """
        _backup(f"{self.course_name}_weights", "Weights")
        weights_file = open(f"data\\Weights\\{self.course_name}_weights.json")
        temp = json.load(weights_file)
        self.weights = temp

    def run(self) -> None:
        """ Run this command """
        self.get_storage_json()
        self.get_weights_json()

    def get_mark_book_object(self) -> MarkBookObject:
        """ Get the stored MarkBookObject

        :return: the MarkBookObject
        """
        return MarkBookObject(self.course_name, self.storage, self.weights)


if __name__ == "__main__":
    print(check_course_code("mie100"))
