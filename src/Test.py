import json

a = {"CURRENT MARK": 100.0,
     "GOAL": 80.0,
     "TESTS": [("test 1", 100.0)],
     "QUIZZES": [["quiz 1", 100.0]]
     }


file = open("DataFiles\\CSC207H1.json", "w")

json.dump(a, file)
