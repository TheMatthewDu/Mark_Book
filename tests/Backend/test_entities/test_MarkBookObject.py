import unittest

from Entities.MarkBookObject import *

test_storage = {
    "Labs": [],
    "Midterm": [],
    "Quizzes": [],
    "Project": [],
    "Final": [],
    "GOAL": 80,
    "CURRENT MARK": 100
}

test_storage2 = {
    "Labs": [["lab 1", 95.0]],
    "Midterm": [["midterm", 85.0]],
    "Quizzes": [],
    "Project": [["project part 1", 85.0]],
    "Final": [],
    "GOAL": 80,
    "CURRENT MARK": 87
}

test_weights = {
    "Labs": 10.0,
    "Midterm": 20.0,
    "Quizzes": 20.0,
    "Project": 20.0,
    "Final": 30.0
}


object1 = MarkBookObject("test_name", test_storage, test_weights)
object2 = MarkBookObject("", test_storage2, test_weights)


class TestMarkBookObject(unittest.TestCase):
    def test_initialization(self):
        object1_clone = object1.copy()
        object2_clone = object2.copy()

        # Dataset 1
        for name, entry in object1_clone._data.items():
            self.assertIsInstance(name, str)
            self.assertIsInstance(entry, DataEntry)

        self.assertEqual(object1_clone.name, "test_name")
        self.assertEqual(object1_clone._goal, 80)
        self.assertEqual(object1_clone._current_mark, 0.0)

        # Dataset 2
        for name, entry in object2_clone._data.items():
            self.assertIsInstance(name, str)
            self.assertIsInstance(entry, DataEntry)

        self.assertEqual(object2_clone.name, "")
        self.assertEqual(object2_clone._goal, 80)
        self.assertEqual(object2_clone._current_mark, 87)

        # Dataset 3
        object3 = MarkBookObject("name", {GOAL: 0.0, CURRENT_MARK: 0.0}, {})
        for name, entry in object3._data.items():
            self.assertIsInstance(name, str)
            self.assertIsInstance(entry, DataEntry)

        self.assertEqual(object3.name, "name")
        self.assertEqual(object3._goal, 0.0)
        self.assertEqual(object3._current_mark, 0.0)

    def test_add_entry(self):
        object1_clone = object1.copy()
        object1_clone.add_entry("Labs", "lab 1", 95.0)

        entry = DataEntry("Labs", 10.0)
        entry.add_entry("lab 1", 95.0)
        entry._pseudo_weight = 100

        self.assertEqual(entry, object1_clone._data["Labs"])

        object1_clone = object1

        with self.assertRaises(ValueError):
            object1_clone.add_entry("Assignments", "assignment 1", 95.0)

    def test_analyze(self):
        object1_clone = object1.copy()
        object1_clone.add_entry("Labs", "lab 1", 94.0)
        self.assertEqual('Current Mark: 94.0%\nThe mark is safe. Keep up the good work! Above by 14.0%', object1_clone._analyze())

        object1_clone = object1.copy()
        object1_clone.add_entry("Labs", "lab 1", 84.0)
        self.assertEqual('Current Mark: 84.0%\nThe mark is good. Above by 4.0%', object1_clone._analyze())

        object1_clone = object1.copy()
        object1_clone.add_entry("Labs", "lab 1", 76.0)
        self.assertEqual('Current Mark: 76.0%\nDANGER. MARK BELOW GOAL BY -4.0%', object1_clone._analyze())

    def test_distribute_weights(self):
        object1_clone = object1.copy()
        object1_clone.add_entry("Labs", "lab 1", 95.0)
        self.assertEqual(100.0, object1_clone._data["Labs"]._pseudo_weight)

        object1_clone.add_entry("Final", "Final", 100.0)
        self.assertEqual(25.0, object1_clone._data["Labs"]._pseudo_weight)
        self.assertEqual(75.0, object1_clone._data["Final"]._pseudo_weight)
        self.assertEqual(0.0, object1_clone._data["Midterm"]._pseudo_weight)

        object2_clone = object2.copy()
        self.assertEqual(20.0, object2_clone._data["Labs"]._pseudo_weight)
        self.assertEqual(40.0, object2_clone._data["Midterm"]._pseudo_weight)
        self.assertEqual(40.0, object2_clone._data["Project"]._pseudo_weight)


if __name__ == '__main__':
    unittest.main()
