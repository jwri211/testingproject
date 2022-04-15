import BowlingGame
from TestBowlingGame import TestBowlingGame

#create a test object to call and run all tests.
tester = TestBowlingGame()

def runTests():
    print("Testing...")
    #sets up the bowling game
    tester.setUp()
    #apply first test: gutter game, all 0s.
    tester.testGutterGame()
    print("gutter game passes")
    tester.resetGame()
    #apply second test: all ones.
    tester.testAllOnes()
    print("All ones passes")
    tester.resetGame()
    #apply third test: one spare
    tester.testOneSpare()
    tester.resetGame()
    #apply fourth test: one strike
    tester.testOneStrike()
    tester.resetGame()
    #apply fith test: perfect score
    tester.testPerfectGame()
    tester.resetGame()
    #apply sixth test: all spares
    tester.testAllSpares()
    tester.resetGame()

runTests()