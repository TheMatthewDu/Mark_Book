from Commands.AbstractClasses.Command import Command


class HasReturn(Command):
    """ An abstract command object that has a return value that needs to be printed """

    def run(self) -> None:
        """ Inherited from Command """
        raise NotImplementedError

    def get_print_data(self) -> str:
        """ Print the return value of the command """
        raise NotImplementedError
