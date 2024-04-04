"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
         {
        "input": [[1, 2, 3, 4, 5], 6],
        "answer": [-1, 3]
    },
    {
        "input": [[1, 3, 4, 5, 7, 8, 9], 5],
        "answer": [3, 1]
    },
    {
        "input": [[10, 20, 30, 40, 50], 40],
        "answer": [3, 2]
    },
    {
        "input": [[10, 20, 30, 40, 50, 60], 25],
        "answer": [-1, 3]
    },
    {
        "input": [[1, 3, 5, 7, 9, 11, 13, 15], 14],
        "answer": [-1, 3]
    }
    ]
}
