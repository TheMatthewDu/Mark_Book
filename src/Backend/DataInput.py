from __future__ import annotations
from typing import Dict
from src.Backend.DataObject import DataObject


def _format_mark(mark_input: str) -> float:
    """ Format the mark into the correct format. The mark is in the form x%,
    where x / 100 <= 1.

    :param: mark_input: the input of the user
    :return: the value of the mark.
    """
    evaluated_mark = eval(mark_input)
    if evaluated_mark <= 1:
        return round(evaluated_mark * 100, 2)
    else:
        return evaluated_mark


def _filter_description(description: str) -> str:
    """ Convert all the description to lower case. If numeric, keep numeric

    :param: description: the description that the user inputted
    :return: the correctly formatted description
    """
    filtered_data = ''
    for char in description:
        if char.isupper():
            filtered_data += char.lower()
        else:
            filtered_data += char
    return filtered_data


class DataInput:
    """ An object for adding to the DataObject

    === Private Attributes ===
    data: the data Object to which the entries will be added to
    """
    _data: DataObject

    def __init__(self, data: DataObject):
        """ Initializer

        :param: data: the DataObject that items will be added to
        """
        self._data = data

    def input_data(self) -> None:
        """ The main body that adds the input """
        running = True
        while running:
            collection = self._get_numbered_entries()

            entry, mark_description, mark_input = \
                input('Please enter the number of assignment type: '), \
                input('Please enter the description of mark: '), \
                input('Please enter mark: ')

            mark_value = _format_mark(mark_input)

            # Confirmation message
            print(f'Now Inputting {mark_value}%')

            filtered_data = _filter_description(mark_description)

            self._data.add_entry(collection[entry], filtered_data, mark_value)

            check = input('Any more entries? (Y/N): ')
            if check == 'N':
                running = False

    def gui_input_data(self, data) -> str:
        """ The main body that adds the input """
        entry, mark_description, mark_input = data

        mark_value = _format_mark(mark_input)

        filtered_data = _filter_description(mark_description)

        self._data.add_entry(entry, filtered_data, mark_value)

        return f'Now Inputting {mark_value}%'

    def _get_numbered_entries(self) -> Dict[str, str]:
        """ Generate and prompt a dict of data to the user

        :return: a dict where the keys are numeric and values are corresponding
            groups
        """
        print('HERE ARE THE IDENTIFIED CATEGORIES \n')

        # Get all the data in data_dict
        numeric_data_dict = self._data.generate_numbered_data_dict()

        for entry_index in numeric_data_dict:
            print(entry_index, numeric_data_dict[entry_index])

        return numeric_data_dict
