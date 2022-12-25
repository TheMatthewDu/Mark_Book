from typing import Optional

from Commands.AbstractClasses.Command import Command
from Entities.MarkBookObject import MarkBookObject


class NeedsData(Command):
    """ An abstract command class that modifies or requires a MarkBookObject

    :ivar data The MarkBookObject being modified. Is `None` if not set
    """
    data: Optional[MarkBookObject]

    def __init__(self) -> None:
        """ Initializer """
        self.data = None

    def set_data(self, storage: MarkBookObject) -> None:
        """ Set a MarkBookObject to a data

        :param storage: The MarkBookObject to set
        :return: Nothing
        """
        self.data = storage

    def get_data(self) -> MarkBookObject:
        """ Get the MarkBookObject

        :raises AssertionError if data is not set
        :return: The MarkBookObject
        """
        assert self.data is not None
        return self.data

    def run(self) -> None:
        """ An abstract interface (from Command) to run the command

        :raises NotImplementedError if not implemented
        :return Nothing
        """
        raise NotImplementedError
