from __future__ import annotations
from typing import Optional, List

from Commands.AbstractClasses.HasReturn import HasReturn
from Commands.AbstractClasses.NeedsData import NeedsData


class PrintDataCmd(HasReturn, NeedsData):
    """ A command to print the data found within a MarkBookObject

    === Attributes ===
    :ivar data_dict: A list of the entry dictionaries in the MarkBook object
    :ivar analysis: The string analysis of the MarkBookObject
    """
    data_dict: Optional[List[str]]
    analysis: str

    def __init__(self) -> None:
        """ Initializer """
        HasReturn.__init__(self)
        self.data_dict = None
        self.analysis = ""

    def run(self):
        """ Populates the data_dict and the analysis """
        assert self.data is not None
        self.data_dict, self.analysis = self.data.get_list_entry()

    def get_print_data(self) -> str:
        """ Print the elements in the data dictionary

        :return: A string of the response of the dict
        """
        response = ''
        for group in self.data_dict:
            response += f"{group}\n"
        response += '\n'
        return response + self.analysis

