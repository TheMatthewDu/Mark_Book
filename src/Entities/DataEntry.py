from __future__ import annotations
from typing import List, Tuple, Dict, Union
import numpy as np
from src.constants import *


class DataEntry:
    """ The data entry

    === Attributes ===
    :ivar name: The name of the data entry
    :ivar weight: The weight of this entry

    === Private Attributes ===
    :ivar _pseudo_weight: The weight adjusted weight of the entry based on the information currently provided
    :ivar _data: The list of all data elements in the entry
    """
    name: str
    weight: float
    _pseudo_weight: float
    _data: List[Tuple[str, float]]

    def __init__(self, name: str, weight: float) -> None:
        """ Initializer

        :param name: The name of the entry
        :param weight: The weight of the entry
        """
        self.name = name
        self.weight = weight
        self._pseudo_weight = weight
        self._data = []

    def add_entry(self, description: str, mark: float) -> None:
        """ Add a new data entry to the MarkBook Entry

        :param description: The description of the data
        :param mark: The mark entered
        :return: Nothing
        """
        self._data.append((description, mark))

    def add_entries_list(self, entries: List[Tuple[str, float]]) -> None:
        """ Add a list of elements to the entry

        :param entries: THe list of elements to be added
        :return: Nothing
        """
        self._data.extend(entries)

    def is_empty(self) -> bool:
        """ Check if the Entry is empty

        :return: True if the entry is empty
        """
        return self._data == []

    def calculate_mark(self) -> float:
        """ Returns the average of all the marks in data with weights

        :return: The mark in this entry
        """
        grade_list = [item[1] for item in self._data]

        # If there is no entries in the grade list, return 0.0
        if not grade_list:
            return 0.0

        average = np.average(grade_list)
        weight_percent = self._pseudo_weight / 100
        return round(average * weight_percent, 2)

    def set_pseudo_weight(self, weight: float) -> None:
        """ Set the pseudo weight of the MarkBook

        :param weight: the new pseudo-weight
        :return: Nothing
        """
        self._pseudo_weight = weight

    def get_weight(self) -> float:
        """ Get the weight of the Entry

        :return: The weight
        """
        return self.weight

    def __str__(self) -> str:
        """ Get a string representation of the entry

        :return: The string representation
        """
        ret = f"{self.name}: weight = {self.weight}\n"
        for item in self._data:
            ret += f"\t{item[0]}: {item[1]}\n"
        return ret

    def __eq__(self, other: DataEntry) -> bool:
        """ Returns true iff self == other. Mainly for testing purposes """
        return self.name == other.name and self.weight == other.weight and self._pseudo_weight == other._pseudo_weight \
               and self._data == other._data

    def get_data_dict(self) -> Dict[str, Union[Union[float, str], Tuple[float, float]]]:
        """ Get a dictionary of the data in the entry

        :return: The data dict in the form:
            name -> [identifier (either float or string) || entry list]
        """
        entries_list = [(item[0], item[1]) for item in self._data]
        return {NAME: self.name, WEIGHT: self.weight, ENTRIES: entries_list}

    def copy(self) -> DataEntry:
        """Creates a copy of the current DataEntry object """
        clone = DataEntry(self.name, self.weight)
        clone._data = self._data
        clone._pseudo_weight = self._pseudo_weight
        return clone
