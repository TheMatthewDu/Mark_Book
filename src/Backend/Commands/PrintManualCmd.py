from src.Backend.Commands.AbstractClasses.HasReturn import HasReturn


class PrintManualCmd(HasReturn):
    """ Print the help manual of the MarkBook

    === Attributes ===
    :ivar text: The text of the manual
    """
    text: str

    def __init__(self) -> None:
        """ Initializer """
        self.text = ""

    def run(self) -> None:
        """ Print the manual for the MarkBook

        :return: None
        """
        file = open("src\\manual.txt", 'r')
        self.text = file.read()
        file.close()

    def get_print_data(self) -> str:
        """ Get the responses to display to stdout

        :return: The string response to display to stdout
        """
        return self.text
