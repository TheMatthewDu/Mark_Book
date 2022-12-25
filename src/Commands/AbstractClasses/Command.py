class Command:
    """ An Abstract Command Class for all Commands"""
    def run(self) -> None:
        """ An abstract interface to run the command

        :raises NotImplementedError if not implemented
        :return Nothing
        """
        raise NotImplementedError

