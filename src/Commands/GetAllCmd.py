from __future__ import annotations
from typing import List, Optional

from Commands.AbstractClasses.HasReturn import HasReturn
from Commands.AbstractClasses.NeedsData import NeedsData


class GetAllCmd(HasReturn, NeedsData):
    """ A command to get all the entries of a MarkBookObject

    === Attributes ===
    :ivar entries_list: The list of entries in the MarkBookObject
    """
    entries_list: Optional[List[str]]

    def __init__(self) -> None:
        """ Initializer """
        HasReturn.__init__(self)
        self.entries_list = None

    def run(self) -> None:
        """ Run the command and gets all the entries of the MarkBookObject

        :return: Nothing
        """
        self.entries_list = self.data.get_list_entry_names()

    def get_print_data(self) -> str:
        """ Print the responses of the

        :return: Prints the entries of the MarkBook
        """
        return ",".join(self.entries_list)
