from __future__ import annotations
from typing import Dict

from Entities import MarkBookObject
from Commands.AbstractClasses import RequirePrompt, NeedsData
from src.constants import *


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


class DataInputCmd(RequirePrompt, NeedsData):
    """ An object for adding to the DataObject """

    def generate_prompt(self, data: MarkBookObject) -> Dict[str, str]:
        """ Generate the prompts for the data inputs

        :param data: The MarkBookObject needed to generate the prompt
        :return: The dictionary of the responses in the form:
            {CONSTANT_PROMPT: response}
        """
        print(f"Available groups: {', '.join(data.get_list_entry_names())}")
        entry = input("Group: ").strip()
        desc = input("Description: ").strip()
        mark = input("Mark: ").strip()
        return {GROUP: entry, DESCRIPTION: desc, MARK: mark}

    def run(self):
        """ The main body that adds the input """
        assert self._raw_data is not None
        entry, mark_description, mark_input = self._raw_data[GROUP], self._raw_data[DESCRIPTION], self._raw_data[MARK]

        mark_value = _format_mark(mark_input)
        filtered_data = _filter_description(mark_description)

        self.data.add_entry(entry, filtered_data, mark_value)
