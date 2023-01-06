from typing import Optional, List, Tuple
from Controllers.Controller import Controller

from src.constants import *


class GUIController:
    controller: Controller

    def __init__(self) -> None:
        """ Initializer """
        self.controller = Controller()

    def set_course(self, name: str) -> Optional[str]:
        """ Set a course into the Controller

        :param name: The name of the course
        :return: Nothing
        """
        return self.controller.process_command(CMD_SET, [name])

    def enter_data(self, group: str, desc: str, mark: str) -> Optional[str]:
        """ Enter a new entry into the MarkBook

        :param group: The group of the entry.
        :param desc: The description of the mark
        :param mark: The mark being inputted
        :return: Nothing
        """
        data = {GROUP: group, DESCRIPTION: desc, MARK: mark}
        return self.controller.process_command(CMD_INPUT, [], data)

    def generate_analysis(self) -> Optional[str]:
        """ Generates the analysis and data in the MarkBook

        :return: The analysis
        """
        return self.controller.process_command(CMD_PRINT, [])

    def create_course(self, data: List[Tuple[str, str]], filename: str, goal: str) -> Optional[str]:
        """ Create a new MarkBook course entry

        :param data: The dict of the course information
        :param filename: The name of the new course
        :param goal: The goal of the course
        :return: Nothing. Error message if error occurs.
        """
        clone_data = {
            COURSE_NAME: filename,
            GOAL: goal,
            DATA: [item[0] for item in data],
            WEIGHT: [item[1] for item in data]
        }  # (Assuming small input sizes, so time difference is negligible)

        return self.controller.process_command(CMD_CREATE, [], clone_data)

    def get_list_elements(self) -> Optional[str]:
        """ Get a list of all entry names in the MarkBook

        :return: The string representation of the items in MarkBook. Error Message if they occur
        """
        return self.controller.process_command(CMD_LIST, [])

    def get_totals(self) -> Optional[str]:
        """ Returns the information of all the totals from all entries in the MarkBook

        :return: The totals information
        """
        return self.controller.process_command(CMD_TOTALS, [])

    def commit_changes(self) -> Optional[str]:
        """ Commit changes made in app """
        return self.controller.process_command(CMD_COMMIT, [])
