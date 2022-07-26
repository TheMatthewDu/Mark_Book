from src.Backend.Commands.AbstractClasses.HasReturn import HasReturn


class TotalsCmd(HasReturn):
    """ Print the help manual of the MarkBook

    === Attributes ===
    :ivar text: The text of the manual
    """
    text: str

    def __init__(self) -> None:
        """ Initializer """
        self.text = ""

    def run(self) -> None:
        """ Print the totals

        :return: None
        """
        file = open("src\\Backend\\Overall Averages.txt")
        self.text = file.read()
        file.close()

    def get_print_data(self) -> str:
        """ Get the responses to display to stdout

        :return: The string response to display to stdout
        """
        return self.text
