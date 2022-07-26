from typing import Optional, Dict
from src.Backend.Controller import Controller

GROUP = "Group"
DESCRIPTION = "Description"
MARK = "Mark"

GOAL = "GOAL"
FILENAME = "COURSE NAME"


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
        return self.controller.process_command("set", [name])

    def enter_data(self, group: str, desc: str, mark: str) -> Optional[str]:
        """ Enter a new entry into the MarkBook

        :param group: The group of the entry.
        :param desc: The description of the mark
        :param mark: The mark being inputted
        :return: Nothing
        """
        data = {GROUP: group, DESCRIPTION: desc, MARK: mark}
        return self.controller.process_command("input", [], data)

    def generate_analysis(self) -> Optional[str]:
        """ Generates the analysis and data in the MarkBook

        :return: The analysis
        """
        return self.controller.process_command("print", [])

    def create_course(self, data: Dict[str, str], filename: str, goal: str) -> Optional[str]:
        """ Create a new MarkBook course entry

        :param data: The dict of the course information
        :param filename: The name of the new course
        :param goal: The goal of the course
        :return: Nothing. Error message if error occurs.
        """
        clone_data = data.copy()
        clone_data[FILENAME] = filename
        clone_data[GOAL] = goal
        return self.controller.process_command("create", [], data)

    def get_list_elements(self) -> Optional[str]:
        """ Get a list of all entry names in the MarkBook

        :return: The string representation of the items in MarkBook. Error Message if they occur
        """
        return self.controller.process_command("list", [])

    def get_totals(self) -> Optional[str]:
        """ Returns the information of all the totals from all entries in the MarkBook

        :return: The totals information
        """
        return self.controller.process_command("totals", [])
