from src.Backend.Commands.AbstractClasses.Command import Command


class ExitCmd(Command):
    """ A command for the purpose of exiting the program. It is essentially empty as the object is only needed to
    indicate exiting """

    def run(self) -> None:
        """ Emptiness """
        pass
