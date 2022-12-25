from __future__ import annotations
from typing import Dict, List, Tuple, Optional, Union

from Entities.DataEntry import DataEntry
from src.constants import *


class MarkBookObject:
    """ A Data Object. Stores the elements and data of the MarkBook

    === Private Attributes ===
    :ivar name: The name of the entry
    :ivar _data: a dict of entries of the mark book. In the form:
        {group name: [(description, mark), ...]}
    :ivar _current_mark: the current mark
    :ivar _goal: the goal
    """
    name: str
    _data: Dict[str, DataEntry]
    _current_mark: Optional[float]
    _goal: float

    def __init__(self, name: str, storage_dict: Dict[str, Union[List[Tuple[str, float]], float]], weight_dict: Dict[str, float]) -> \
            None:
        """ Initializer

        :param name: The name of the MarkBook Object
        :param storage_dict: A dict of the storage information
        :param weight_dict: A dict of the weight information
        """
        assert len(storage_dict) == len(weight_dict) + 2  # Sanity check

        storage_copy = storage_dict.copy()

        self.name = name
        self._data = {}

        storage_copy.pop(CURRENT_MARK)  # Get rid of current mark -> used for getting totals, so won't be needed here

        goal = storage_copy.pop(GOAL)
        assert isinstance(goal, float) or isinstance(goal, int)
        self._goal = goal

        for category_name in storage_copy:
            obj = DataEntry(category_name, weight_dict[category_name])
            obj.add_entries_list(storage_copy[category_name])

            self._data[category_name] = obj

        self._distribute_weights()
        self._current_mark = sum([self._data[obj].calculate_mark() for obj in self._data])

    def add_entry(self, group_name: str, description: str, new_mark: float) -> None:
        """ Add the entry to the storage list

        :param: group_name: the name of the group where the information will be stored
        :param: description: the description of the mark
        :param: new_mark: the new mark to be entered

        :raises ValueError if `group_name` does not exist
        """
        if group_name not in self._data:
            raise ValueError

        # Adding the entry to the storage
        self._data[group_name].add_entry(description, new_mark)

        # Redistribute the weights adding in the new weights
        self._distribute_weights()

        # Calculating the new mark
        self._current_mark = 0
        for entry_group in self._data.values():
            if not entry_group.is_empty():
                self._current_mark += entry_group.calculate_mark()

    def get_list_entry_names(self) -> List[str]:
        """ Gets a list of the names of the entries in the MarkBook Object

        :return: A list of entry names in the MarkBookObject
        """
        return list(self._data.keys())

    def get_data_dict(self) -> Dict[str, Union[List[Tuple[str, float]], float]]:
        """ Get the data dictionary

        :return: A dictionary of the storage elements:
            name -> [List of name-mark pairs || mark information]
        """
        name_to_info_dict = {entry_name: self._data[entry_name]._data for entry_name in self._data}
        name_to_info_dict[GOAL] = self._goal
        name_to_info_dict[CURRENT_MARK] = self._current_mark
        return name_to_info_dict

    def get_weights_dict(self) -> Dict[str, float]:
        """ Get the weight dict

        :return: A dictionary of the entry and the weight of that entry
        """
        return {name: self._data[name].weight for name in self._data.keys()}

    def get_current_mark(self) -> float:
        """ Get the current mark stored in the MarkBookObject

        :return: The current mark
        """
        return self._current_mark

    def get_list_entry(self) -> Tuple[List[str], str]:
        """ Get two things:
            A list of all the entry dicts of each entry and the analysis information of the entry

        :return: The tuple in the form:
            List of entry dicts, the string analysis of the entry
        """
        return [str(self._data[item]) for item in self._data], self._analyze()

    def copy(self):
        clone_storage: Dict[str, Union[List[Tuple[str, float]], float]] = {entry: data._data[:] for entry, data in self._data.items()}
        clone_storage[GOAL] = self._goal
        clone_storage[CURRENT_MARK] = self._current_mark
        clone = MarkBookObject(self.name, clone_storage, self.get_weights_dict())
        return clone

    def __str__(self) -> str:
        """ Generate an analysis of the data stored

        :return: a string representation of the analysis of the data
        """
        analysis = ''
        for group_name in self._data:
            analysis += f"{self._data[group_name]}\n"
        analysis += '\n'

        return analysis + self._analyze()

    def _analyze(self) -> str:
        """ Provide the analysis of the data

        :return: the analysis of the data
        """
        analysis = f"Current Mark: {self._current_mark}%\n"
        mark_difference = round(self._current_mark - self._goal, 2)
        if mark_difference >= 10:
            analysis += f'The mark is safe. Keep up the good work! Above by {mark_difference}%'
        elif 0 <= mark_difference < 10:
            analysis += f'The mark is good. Above by {mark_difference}%'
        else:
            analysis += f'DANGER. MARK BELOW GOAL BY {mark_difference}%'
        return analysis

    def _distribute_weights(self) -> None:
        """ Distribute the weights if there are empty items in the weights

        Precondition: all entries in weights add up to 100
        """
        # Getting the total percentage applicable
        total_usable_weights = sum([self._data[entry].get_weight() for entry in self._data if not self._data[entry].is_empty()])

        # Distributing them to the pseudo_weights
        for item in self._data:
            if not self._data[item].is_empty():
                new_weight = round((self._data[item].weight * 100) / total_usable_weights)

                self._data[item].set_pseudo_weight(new_weight)
            else:
                self._data[item].set_pseudo_weight(0.0)
