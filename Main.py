import BowlingGame
from TestBowlingGame import TestBowlingGame

tester = TestBowlingGame()

def runTests():
    print("Testing...")
    #sets up the bowling game
    tester.setUp()
    #apply first test: gutter game, all 0s.
    tester.testGutterGame()
    #apply second test: all ones.
    tester.testAllOnes()
    #apply third test: one spare
    tester.testOneSpare()
    #apply fourth test: one strike
    tester.testOneStrike()
    #apply fith test: perfect score
    tester.testPerfectGame()
    #apply sixth test: all spares
    tester.testAllSpares()

runTests()