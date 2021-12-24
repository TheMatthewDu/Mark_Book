from __future__ import annotations
from typing import List, TextIO, Dict, Tuple, Optional
from src.Backend.DataObject import DataObject


DESCRIPTION = 'DESCRIPTION'
CURRENT_MARK = "CURRENT MARK"
GOAL = 'GOAL'
NON_DATA_VALUES = [DESCRIPTION, CURRENT_MARK, GOAL]


def is_number(value: str) -> bool:
    """Return True if and only if value represents a decimal number.

    >>> is_number('csc108')
    False
    >>> is_number('  108 ')
    True
    >>> is_number('+3.14159')
    True
    """

    return value.strip().lstrip('-+').replace('.', '', 1).isnumeric()


def clean_data(data: List[list]) -> None:
    """Convert each string in data to an int if and only if it represents a
    whole number, and a float if and only if it represents a number that is not
    a whole number.

    >>> d = [['abc', '123', '45.6', 'car', 'Bike']]
    >>> clean_data(d)
    >>> d
    [['abc', 123, 45.6, 'car', 'Bike']]
    >>> d = [['ab2'], ['-123'], ['BIKES', '3.2'], ['3.0', '+4', '-5.0']]
    >>> clean_data(d)
    >>> d
    [['ab2'], [-123], ['BIKES', 3.2], [3, 4, -5]]
    """

    new_data = []
    for item in data:
        sub_new_data = []
        for it in item:
            signlog = False
            sign = ''
            if is_number(it):
                if it[0] == '+' or it[0] == '-':
                    signlog = True
                    sign += it[0]
                    a = it[1:]
                else:
                    a = it

                if float(a) % 1 == 0:
                    if signlog:
                        sub_new_data.append(int(float(sign + a)))
                    else:
                        sub_new_data.append(int(float(a)))
                else:
                    if signlog:
                        sub_new_data.append(float(sign + a))
                    else:
                        sub_new_data.append(float(a))

            else:
                sub_new_data.append(it)

        new_data.append(sub_new_data)

    data.clear()

    data += new_data


def csv_to_list(csv_file: TextIO) -> List[List[str]]:
    """Read and return the contents of the open CSV file csv_file as a list of
    lists, where each inner list contains the values from one line of csv_file.

    Docstring examples not given since results depend on data to be input.
    """

    # Read and discard header.
    csv_file.readline()

    data = []
    for line in csv_file:
        data.append(line.strip().split(','))
    return data


def remove_empty(removal_list: List[Tuple[str, str]]):
    # Filter the empty sub-lists
    for entry in removal_list:
        if entry == ('', ''):
            removal_list.remove(entry)


class DataReader:
    storage: Dict[str, List[Tuple[str, float]]]
    weights: Dict[str, float]
    goal: Optional[float]
    current: Optional[float]
    contents: List[List[str]]

    def __init__(self, filename: str) -> None:
        """ Initializer """
        file = open(filename)
        self.contents = csv_to_list(file)
        clean_data(self.contents)
        file.close()

        self.weights = {}
        self.storage = {}

    def get_weight_dict(self) -> None:
        """ Get the weight dict """
        # Sorting the contents
        for item in self.contents:

            # If it is a divider point
            if item[0].isupper() and item[0] not in NON_DATA_VALUES:
                if item[0] != CURRENT_MARK:
                    self.weights[item[0]] = item[2]

    def _add_to_storage(self, filtered_data: List[Tuple[str, str]]):
        # Get the individual entries and the mark
        name = ''
        for data_entry in filtered_data:

            # If the enter is a divider
            if data_entry[0].isupper() and data_entry[0] not in NON_DATA_VALUES:
                self.storage[data_entry[0]] = []
                name = data_entry[0]

            # Append all the individual entries
            if not (data_entry[0].isupper()) and data_entry[1] != '':
                self.storage[name].append(data_entry)

    def get_storage_dict(self) -> None:
        """ Get the storage dict """
        self.goal = None
        self.current = None
        for item in self.contents:
            # Getting the goal
            if item[0] == GOAL:
                self.goal = float(item[1])

            # Getting the current mark
            if item[0] == CURRENT_MARK:
                self.current = float(item[1])

        # Get a sublist of all the data in contents
        filtered_data = [(content_line[0], content_line[1]) for content_line in self.contents]

        remove_empty(filtered_data)

        self._add_to_storage(filtered_data)

    def get_data(self) -> DataObject:
        self.get_storage_dict()
        self.get_weight_dict()
        return DataObject(self.storage, self.weights, self.current, self.goal)
