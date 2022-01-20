from __future__ import annotations
from typing import List, Dict, Tuple, Optional
import json
from src.Backend.DataObject import DataObject


DESCRIPTION = 'DESCRIPTION'
CURRENT_MARK = "CURRENT MARK"
GOAL = 'GOAL'
NON_DATA_VALUES = [DESCRIPTION, CURRENT_MARK, GOAL]


class DataReader:
    storage: Dict[str, List[Tuple[str, float]]]
    weights: Dict[str, float]
    goal: Optional[float]
    current: Optional[float]
    contents: List[List[str]]

    def __init__(self, filename: str) -> None:
        """ Initializer """
        self.filename = filename
        self.weights = {}
        self.storage = {}

    def get_storage_json(self) -> None:
        """ Get the storage JSON

        :return: None
        """
        storage_file = open(f"DataFiles\\Data\\{self.filename}.json")
        self.storage = json.load(storage_file)
        self.goal = self.storage.get(GOAL)
        self.current = self.storage.get(CURRENT_MARK)
        self.storage.pop(GOAL)
        self.storage.pop(CURRENT_MARK)

    def get_weights_json(self) -> None:
        """ Get the storage JSON

        :return: None
        """
        weights_file = open(f"DataFiles\\Weights\\{self.filename}_weights.json")
        temp = json.load(weights_file)
        self.weights = temp

    def get_data(self) -> DataObject:
        self.get_storage_json()
        self.get_weights_json()
        return DataObject(self.storage, self.weights, self.current, self.goal)
