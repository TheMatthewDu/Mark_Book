from __future__ import annotations
from typing import List, Dict, Tuple, Optional
import json
from src.Backend.Entities.MarkBookObject import MarkBookObject

from src.Backend.Commands.AbstractClasses.Command import Command

DESCRIPTION = 'DESCRIPTION'
CURRENT_MARK = "CURRENT MARK"
GOAL = 'GOAL'
NON_DATA_VALUES = [DESCRIPTION, CURRENT_MARK, GOAL]


def _backup(name: str, dict_type: str) -> None:
    """ Quick Backup

    :param name: The name of the course to back up
    :param dict_type: The type of backup. A weight or data file
    :return: Nothing
    """
    backup = open(f"src\\BACKUPS\\{name}_BACKUP.json", 'w')
    file = open(f"src\\DataFiles\\{dict_type}\\{name}.json", 'r')

    backup_read = json.load(file)
    json.dump(backup_read, backup)

    file.close()
    backup.close()


class DataReaderCmd(Command):
    """ A command to read data

    :ivar filename
    :ivar storage
    :ivar weights
    :ivar goal
    :ivar current
    """
    filename: str
    storage: Dict[str, List[Tuple[str, float]]]
    weights: Dict[str, float]
    goal: Optional[float]
    current: Optional[float]

    def __init__(self, filename: str) -> None:
        """ Initializer """
        self.filename = filename
        self.weights = {}
        self.storage = {}
        self.current = None
        self.goal = None

    def get_storage_json(self) -> None:
        """ Get the storage JSON

        :return: None
        """
        _backup(self.filename, "Data")
        storage_file = open(f"src\\DataFiles\\Data\\{self.filename}.json")
        self.storage = json.load(storage_file)

        self.goal = self.storage.get(GOAL)
        self.current = self.storage.get(CURRENT_MARK)

        self.storage.pop(GOAL)
        self.storage.pop(CURRENT_MARK)

    def get_weights_json(self) -> None:
        """ Get the storage JSON

        :return: None
        """
        _backup(f"{self.filename}_weights", "Weights")
        weights_file = open(f"src\\DataFiles\\Weights\\{self.filename}_weights.json")
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
        return MarkBookObject(self.filename, self.storage, self.weights, self.current, self.goal)
