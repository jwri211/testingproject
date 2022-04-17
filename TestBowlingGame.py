import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    # Sets up  by creating a new instance of the bowling class.
    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    #A method to reset the rolls list after each test game
    def resetGame(self):
        self.game.rolls = []

    # tests a gutter game by rolling no pins for all 20 frames.
    def testGutterGame(self):
        self.rollMany(0, 20) # changed this from the for loop to use the inbuilt method.
        assert self.game.score()==0  # expected score is 0

    # tests a game of all ones by rolling 1 each time
    def testAllOnes(self):
        self.rollMany(1, 20)
        assert self.game.score()==20  # expected score is 20

    # tests one spare at the start of the game, followed by 17 gutter balls.
    def testOneSpare(self):
        self.game.roll(5)  # knock down 5
        self.game.roll(5)  # knock down remaining 5 (spare - get 1 bonus round)
        self.game.roll(3)  # knock down 3 in bonus round (double points for score here)
        self.rollMany(0,17)  # Finish the game by rolling gutter balls to ensure score stays 17??
        assert self.game.score()==16  # expected score is 16 (10 + 3 + 3)

    # test the score after scoring one strike at the start of the game
    def testOneStrike(self):
        self.game.roll(10) # roll first strike -
        self.game.roll(4)  # added to bonus score
        self.game.roll(3)  # added to bonus score
        self.rollMany(0,16) # finish game with another 16 rolls of gutter balls.
        assert self.game.score()==24 # expected score of 24 (10 + 7 + 7)

    # Tests a game of strikes each time
    def testPerfectGame(self):
        self.rollMany(10,12)  # knock down 10 balls 12 times
        assert self.game.score()==300  # expected score is 300

    # INCORRECT NAME: REFACTORED TO testAllSpares
    # tests a game where each roll knocks down 5 pins, - 100% spares
    def testAllSpares(self):
        self.rollMany(5,21)
        assert self.game.score()==150

    # designed to loop the necessary number of times to finish a game.
    # knock down x pins y times to get a result.
    # For example, rollMany(10,12) means knock down 10 pins 12 times
    def rollMany(self, pins,rolls):
        for i in range(rolls):
            # REFACTOR - INCORRECT SYNTAX FOR APPLYING SCORE TO ARRAY
            # CHANGE: -  self.game.rolls(pins) to self.game.roll(pins)
            self.game.roll(pins)

