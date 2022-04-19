import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):
    """
    Class used to test BowlingGame.py

    This contains several methods that create a bowling game and tests different types of
    outcomes against expected scores. Test scores range from a zero score gutter game to
    a full roll of strikes for a score of 300. Uses the Assertion methods from the unittest
    library to test the code.

    Methods:
    --------
    setUp()
        Creates a bowling game object on which to perfrom the tests.

    resetGame()
        Resets the score array of the bowling game, designed to be called after each test.

    testGutterGame()
        Tests a game where each roll is 0 against an expected score of 0.

    testAllOnes
        Tests a game where each roll is a 1 against an expected score of 20.

    testOneSpare
        Tests a game where one spare is rolled at the start, followed by a bonus score
        and then all zeros. Expects a score of 16.

    testOneStrike
        Tests a game where the first roll is a strike, followed by scores in the next
        two rolls to calculate a bonus. Expects a score of 24.

    testPerfectGame
        Tests a game where each roll is a strike. Expects a score of 300.

    testAllSpares
        Tests a game where each frame is a spare. Expects a score of 150.

    rollMany(pins, rolls)
        Rolls a score of the given amount of *pins* the amount of times defined by *rolls*
    """

    def setUp(self):
        """Sets up  by creating a new instance of the bowling class."""

        self.game = BowlingGame.BowlingGame()

    def resetGame(self):
        """Reset the rolls list, ideally called after each test game"""

        self.game.rolls = []

    def testGutterGame(self):
        """Tests a gutter game by rolling no score for all 20 rolls."""

        self.rollMany(0, 20) # REFACTORED: changed this from the for loop to use the inbuilt method.
        assert self.game.score()==0  # expected score is 0

    def testAllOnes(self):
        """Tests a game of all ones by rolling 1 each time"""

        self.rollMany(1, 20)
        assert self.game.score()==20  # expected score is 20

    def testOneSpare(self):
        """Tests one spare at the start of the game, followed by 17 gutter balls."""

        self.game.roll(5)  # knock down 5
        self.game.roll(5)  # knock down remaining 5 (spare - get 1 bonus round)
        self.game.roll(3)  # knock down 3 in bonus round (double points for score here)
        self.rollMany(0,17)  # Finish the game by rolling gutter balls to ensure score stays 17??
        assert self.game.score()==16  # expected score is 16 (10 + 3 + 3)

    def testOneStrike(self):
        """Test the score after scoring one strike at the start of the game."""

        self.game.roll(10) # roll first strike -
        self.game.roll(4)  # added to bonus score
        self.game.roll(3)  # added to bonus score
        self.rollMany(0,16) # finish game with another 16 rolls of gutter balls.
        assert self.game.score()==24 # expected score of 24 (10 + 7 + 7)

    def testPerfectGame(self):
        """Tests a game where each roll is a strike."""

        self.rollMany(10,12)  # knock down 10 balls 12 times
        assert self.game.score()==300  # expected score is 300

    def testAllSpares(self): # INCORRECT NAME: REFACTORED TO testAllSpares
        """Tests a game where each roll knocks down 5 pins - 100% spares"""

        self.rollMany(5,21)
        assert self.game.score()==150


    def rollMany(self, pins,rolls):
        """
        Designed to loop the necessary number of times to finish a game.
        Knock down x pins y times to get a result.
        For example, rollMany(10,12) means knock down 10 pins 12 times

        Parameters
        ----------
        pins : int
            the score, or amount of pins to be knocked down, each roll
        rolls: int
            the amount of times to roll the set amount of pins
        """

        for i in range(rolls):
            # REFACTOR - INCORRECT SYNTAX FOR APPLYING SCORE TO ARRAY
            # CHANGE: -  self.game.rolls(pins) to self.game.roll(pins)
            self.game.roll(pins)

