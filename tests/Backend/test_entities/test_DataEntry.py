import unittest
from Entities.DataEntry import *

entry = DataEntry("entry", 20.0)


class TestDataEntry(unittest.TestCase):
    def test_calculate_mark(self):
        entry_clone = entry.copy()
        self.assertEqual(0.0, entry_clone.calculate_mark())

        entry_clone.add_entry("lab 1", 95.0)
        self.assertEqual(95.0 * 0.2, entry_clone.calculate_mark())


if __name__ == '__main__':
    unittest.main()
