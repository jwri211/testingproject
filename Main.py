import BowlingGame
from TestBowlingGame import TestBowlingGame

#create a test object to call and run all tests.
tester = TestBowlingGame()

def runTests():
    print("Testing...")
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

runTests()