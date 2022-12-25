import unittest

from Controllers.Controller import *


class ControllerTest(unittest.TestCase):
    def test_process_null_command(self):
        controller = Controller()
        self.assertEqual(controller.process_command("cat"), "cat not found. Try again")


if __name__ == '__main__':
    unittest.main()
