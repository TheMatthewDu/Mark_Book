from __future__ import annotations
from typing import Optional, List, Dict

from Entities import MarkBookObject
from Commands import *
from Commands.AbstractClasses import *
from src.constants import *


def _create_command(command: str, args: Optional[List[str]] = None) -> Command:
    """ A factory function to get the command object based on the input command and the command line arguments

    :param command: The name of the command
    :param args: The command line arguments (if applicable)
    :return: The command objects
    """
    arg_less_commands = {
        CMD_PRINT: PrintDataCmd,
        CMD_INPUT: DataInputCmd,
        CMD_CREATE: CreateCmd,
        CMD_LIST: GetAllCmd,
        CMD_COMMIT: CommitCmd,
        CMD_EXIT: ExitCmd,
        CMD_TOTALS: TotalsCmd,
        CMD_HELP: PrintManualCmd
    }

    args_commands = {
        CMD_SET: (DataReaderCmd, 1, "usage: setup <filename>.json")
    }

    if command in arg_less_commands:
        return arg_less_commands[command]()
    elif command in args_commands:
        info = args_commands[command]
        if args is None or len(args) != info[1]:
            print(info[2])  # TODO Remove dependency on print for gui
            raise ValueError
        else:
            return info[0](*args)
    else:
        raise ValueError


class Controller:
    """ A controller class to control the flow of actions in the MarkBook

    === Attributes ===
    :ivar data: The MarkBookObject that stores the information and the current state of the MarkBook. Is None if it is
        not set
    """
    data: Optional[MarkBookObject]

    def __init__(self) -> None:
        """ Initializer """
        self.data = None
    
    def process_command(self, cmd_str: str, args: Optional[List[str]] = None, inputs: Optional[Dict[str, str]] = None) \
            -> Optional[str]:
        """ Process the command `cmd_str` with command line arguments args or input dictionary `inputs`

        :param cmd_str: The command to be executed
        :param args: The argument list inputted in commands (if applicable)
        :param inputs: The input dictionary. Used for GUI or other non-command line devices
        :return: A string response that is to be displayed or nothing.
        """
        # Get a command based on inputs
        try:
            command = _create_command(cmd_str, args)
        except ValueError:
            return f"{cmd_str} not found. Try again"

        # If the command is exit command, then exit
        if isinstance(command, ExitCmd):
            return self._process_exit()

        if isinstance(command, RequirePrompt):
            response = self._process_get_prompt(command, inputs)
            if isinstance(response, str):
                return response

        if isinstance(command, NeedsData):
            response = self._process_needs_data(command)
            if isinstance(response, str):
                return response

        command.run()

        # Needs to set a command to a markbook object
        if isinstance(command, CreateCmd):
            self.data = command.set_mark_book_object()

        if isinstance(command, DataReaderCmd):
            self.data = command.get_mark_book_object()
            return "Data set"

        if isinstance(command, CommitCmd):
            self.data = None
            return "Committed"

        if isinstance(command, HasReturn):
            return str(command.get_print_data())

    def _process_exit(self) -> str:
        """ Processes the exit command. Exits the program.

        :return: Error message
        """
        if self.data is None:
            exit(0)
        else:
            return "Currently not committed"

    def _process_get_prompt(self, command: RequirePrompt, inputs: Optional[Dict[str, str]]) -> Optional[str]:
        """ Process all commands that requires a prompt

        `inputs` is the dictionary of the inputs of the commands for anything that does not accept command line inputs
            (i.e., GUI form)

        :param command: The RequirePrompt object that will be processed
        :param inputs: The dictionary of inputs if the caller cannot take command line inputs
        :return: An error message if one occurs. Else, returns none
        """
        if isinstance(command, CreateCmd):
            self.data = MarkBookObject("", {GOAL: 0.0, CURRENT_MARK: 0.0}, {})
            if inputs is None:
                cmd_input = command.generate_prompt(self.data)
            else:
                cmd_input = inputs
        elif self.data is None:
            return "Data not set"
        elif inputs is None:
            cmd_input = command.generate_prompt(self.data)
        else:
            cmd_input = inputs
        command.set_raw_data(cmd_input)

    def _process_needs_data(self, command: NeedsData) -> Optional[str]:
        """ Process a command that needs data

        :param command: The command object
        :return: The return message
        """
        if self.data is None:
            return "Data not set"
        else:
            command.set_data(self.data)
