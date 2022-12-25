from typing import Optional, Dict

from Commands.AbstractClasses.Command import Command
from Entities import MarkBookObject


class RequirePrompt(Command):
    """ An abstract Command object that generates a numbered prompt that requires user's input

    :ivar _raw_data A dict of corresponding data. The key is the response; the value is the prompt to request.
    """
    _raw_data: Optional[Dict[str, str]]

    def __init__(self) -> None:
        """ Initializer """
        self._raw_data = None

    def generate_prompt(self, data: MarkBookObject) -> Dict[str, str]:
        """ Generates a prompt based on a MarkBookObject

        :param data: The MarkBookObject
        :return: The dict of correspondences
        """
        raise NotImplementedError

    def set_raw_data(self, data: Dict[str, str]) -> None:
        """ Set a correspondence dictionary to the command

        :param data: The correspondence dictionary
        :return: Nothing
        """
        self._raw_data = data.copy()

    def run(self):
        """ An abstract interface to run the command

        :raises NotImplementedError if not implemented
        :return Nothing
        """
        raise NotImplementedError
