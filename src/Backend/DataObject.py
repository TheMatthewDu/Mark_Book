from __future__ import annotations
from typing import Dict, List, Tuple, Optional, Union
import numpy as np

DESCRIPTION = 'DESCRIPTION'
CURRENT_MARK = "CURRENT MARK"
GOAL = 'GOAL'
NON_DATA_VALUES = [DESCRIPTION, CURRENT_MARK, GOAL]

COURSE_NAME = 'COURSE NAME'
MARK = 'MARK'
WEIGHTS = 'WEIGHTS'


def calculate_mark(data: List[Tuple[str, float]], weight: float) -> float:
    """ Returns the average of all the marks in data with weights

    :param: data: the List of entries of data. Each entry is in the form
        (description, mark)
    :weight: the weight of the category of data
    """
    grade_list = [item[1] for item in data]
    average = np.average(grade_list)
    weight_percent = weight / 100
    return round(average * weight_percent, 2)


class DataObject:
    """ A Data Object.

    === Private Attributes ===
    _storage: a dict of entries of the mark book. In the form:
        {group name: [(description, mark), ...]}
    _weights: a dict of all the weights of each group
        {group name: weight}
    _current_mark: the current mark
    _goal: the goal
    _pseudo_weights: the dict of weights of the current state of the storage
    """
    _storage: Dict[str, List[Tuple[str, float]]]
    _weights: Dict[str, float]
    _current_mark: Optional[float]
    _goal: float
    _pseudo_weights: Dict[str, float]

    def __init__(self, storage_dict: Dict[str, List[Tuple[str, float]]],
                 weight_dict: Dict[str, float], curr_mark: Optional[float],
                 goal: Optional[float]) -> None:
        """ Initializer

        :param: storage_dict: A dict of the storage information
        :param: weight_dict: A dict of the weight information
        :param: curr_mark: the current mark
        :param: goal: the goal
        """
        self._storage = storage_dict
        self._weights = weight_dict
        self._pseudo_weights = self._weights.copy()
        self._current_mark = curr_mark
        self._goal = goal

    def add_entry(self, group_name: str, description: str, new_mark: float) \
            -> None:
        """ Add the entry to the storage list

        :param: group_name: the name of the group where the information will be stored
        :param: description: the description of the mark
        :param: new_mark: the new mark to be entered
        """
        # Adding the entry to the storage
        self._storage[group_name].append((description, new_mark))

        # Redistribute the weights adding in the new weights
        self._distribute_weights()

        # Calculating the new mark
        total = 0
        for entry_group in self._storage:
            if self._storage[entry_group]:
                total += calculate_mark(self._storage[entry_group],
                                        self._pseudo_weights[entry_group])
        self._current_mark = total

    def sort_for_writing(self, file_name: str) -> List[Tuple[str, str]]:
        """ Sort Storage For writing """
        to_write_data_list = [
            (COURSE_NAME, file_name),
            (CURRENT_MARK, self._current_mark),
            (GOAL, self._goal),
            (DESCRIPTION, MARK, WEIGHTS)
        ]

        for item in self._storage:
            if item.isupper() and item not in NON_DATA_VALUES:
                to_write_data_list.append([item, '', str(self._weights[item])])
            if isinstance(self._storage[item], list) \
                    and item not in NON_DATA_VALUES:
                for it in self._storage[item]:
                    to_write_data_list.append(it)

        return to_write_data_list

    def generate_analysis(self) -> str:
        """ Generate an analysis of the data stored

        :return: a string representation of the analysis of the data
        """
        analysis = ''
        for group_name in self._storage:
            analysis += f"{group_name} \t {self._storage[group_name]}\n"

        analysis += '\n'

        return analysis + self._analyze()

    def generate_numbered_data_dict(self) -> Dict[str, str]:
        """ Generate a dict of data, where each data value is of a different
        numeric key

        :return: the dict of the items described above
        """
        data_dict = {}
        index_of_entry = 0
        for item in self._storage:
            if item not in NON_DATA_VALUES:
                data_dict[str(index_of_entry)] = item
                index_of_entry += 1
        return data_dict

    def to_list(self) -> List[str]:
        data_lst = []
        for item in self._storage:
            if item not in NON_DATA_VALUES:
                data_lst.append(item)
        return data_lst

    def to_gui(self) -> List[Tuple[str, str]]:
        ret = [("CURRENT MARK", self._current_mark),
               ("GOAL", self._goal)]
        for item in self._storage:
            ret.append((item, ""))
            ret.extend(self._storage[item])
        return ret

    def _analyze(self) -> str:
        """ Provide the analysis of the data

        :return: the analysis of the data
        """
        analysis = ""
        mark_difference = self._current_mark - self._goal
        if mark_difference >= 10:
            analysis += f'The mark is safe. Keep up the good work! Above by ' \
                        f'{mark_difference}'
        elif 0 <= mark_difference < 10:
            analysis += f'The mark is good. Above by {mark_difference}'
        else:
            analysis += f'DANGER. MARK BELOW GOAL BY {mark_difference}'
        return analysis

    def _distribute_weights(self) -> None:
        """ Distribute the weights if there are empty items in the weights

        Precondition: all entries in w add up to 100
        """
        new_weights = {}
        # Getting all the non-empty keys
        non_empty_items = [item for item in self._storage if self._storage[item]]

        # Getting the total percentage applicable
        total_usable_weights = 0
        for entry_item in non_empty_items:
            total_usable_weights += self._weights[entry_item]

        for weight in self._weights:
            if weight in non_empty_items:
                new_weights[weight] = round((self._weights[weight] * 100) / total_usable_weights)
            else:
                new_weights[weight] = 0

        self._pseudo_weights = new_weights

    def get_storage(self) -> Dict[str, Union[List[Tuple[str, float]], float]]:
        """ Get the storage dict

        :return: the storage dict
        """
        temp = self._storage.copy()
        temp[GOAL] = self._goal
        temp[CURRENT_MARK] = self._current_mark
        return temp

    def get_weights(self) -> Dict[str, float]:
        """ Get the weight dict

        :return: the weight dict
        """
        return self._weights
