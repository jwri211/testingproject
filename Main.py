import BowlingGame
from TestBowlingGame import TestBowlingGame

"""
Main class for creating a bowling game and calling the tests on it.

Attributes
----------
tester : TestBowlingGame
    The bowling game test object which is used to run the tests.

Methods
-------
runTestss()
    Calls each test defined in the TestBowlinGame.py file in order. Tests that fail will cause an assertion error.
"""

def runTests():
    """Method that runs each test. Will print a message to the console when each game test passes."""

    print("Testing...\n")
    #sets up the bowling game
    tester.setUp()

    #Test 1: gutter game, all 0s.
    tester.testGutterGame()
    print("Gutter game passes")
    tester.resetGame()

    #Test 2: all ones.
    tester.testAllOnes()
    print("All ones passes")
    tester.resetGame()

    #Test 3: one spare
    tester.testOneSpare()
    print("One spare passes")
    tester.resetGame()

    #Test 4: one strike
    tester.testOneStrike()
    print("One strike passes")
    tester.resetGame()

    #Test 5: perfect score
    tester.testPerfectGame()
    print("Perfect game passes")
    tester.resetGame()

    #Test 6: all spares
    tester.testAllSpares()
    print("All spares passes")
    tester.resetGame()

    print("\n...testing complete")

tester = TestBowlingGame()  # Initialise the bowling game

runTests()  # Run the tests in the above method.

