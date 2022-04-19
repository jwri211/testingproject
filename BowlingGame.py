class BowlingGame:
    """
    Class used to play and score a bowling game

    Contains a list of rolls made during a game of bowling, and contains the code to calculate the score
    based on the value of the rolls made during the game. It can tell if a score is a strike, spare or gutter ball
    and calculate the score according to bowling rules.

    Attributes:
    ----------
    rolls : [int]
        an array of integers that stores the scores of each roll in each frame

    Methods:
    -------
    roll(pins)
        Knocks down the given number of pins, creating a score for that roll and appending it to the rolls list.

    score()
        Calculates the final score of the game by iterating the rolls list. Returns an integer value as the result.

    isStrike(rollIndex)
        Looks at the given rollIndex of the rolls list, and returns true if that roll was a strike.

    isSpare(rollIndex)
        Looks at the given rollIndex of the rolls list, and returns true if that roll and the following combine
        for a score of ten, thus being a spare.

    strikeScore(rollIndex)
        Looks at the given rollIndex of the rolls list, and calculates the score based on that index being a strike.

    spareScore(rollIndex)
        Looks at the given rollIndex of the rolls list, and calculates the score based on that index being a spare.

    frameScore(rollIndex)
        Looks at the given rollIndex of the rolls list, and calculates the score of that frame (that roll and the next
        one along - no special bonus rules apply.)
    """


    def __init__(self):
        """Set up an empty list for the score."""

        self.rolls=[]  # score array, contains the number of pins knocked for each roll

    def roll(self,pins):
        """Add the number of pins knocked down to the score array"""

        self.rolls.append(pins)

    def score(self):
        """
        Function for calculating score based on the rolls list.

        Returns
        -------
        result : int
            The final score of the game.
        """

        result = 0  # variable to hold result
        rollIndex=0 # track which roll
        for frameIndex in range(10): # Each game contains ten frames, each with 1 or 2 rolls.
            if frameIndex in range(10):  #if it is in the first ten frames (trying to calculate strike for last two wont work)
                #REFACTORED: ADD FOLLOWING LINE: if self.isStrike(rollIndex)
                if self.isStrike(rollIndex):
                    result += self.strikeScore(rollIndex) #calculate the strike score and add to result.
                    rollIndex +=1 # move to next
                elif self.isSpare(rollIndex): # checks if the frame is a spare - if so, calculates the score accordingly
                    result += self.spareScore(rollIndex)
                    rollIndex +=2
                else: # cacluclate the games score as normal - i.e 3 + 3 = 6, 1 frame.
                    result += self.frameScore(rollIndex)
                    rollIndex +=2
        return result

    def isStrike(self, rollIndex):
        """Checks for a strike - returns true if the score at this index is 10."""

        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        """Checks for a spare. Returns true if the score at this index and the following index sum to 10"""

        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10

    def strikeScore(self,rollIndex):  # REFACTORED: INCORRECT METHOD NAME: CHANGE TO def strikeScore from stickeScore
        """Calculates the strike score. Returns ten, Plus the sum of the next two scores"""

        return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]

    def spareScore(self,rollIndex):
        """Calculates the score from a spare."""

        return  10+ self.rolls[rollIndex+2] # returns the total of all three frames, 1st, 2nd, 3rd.

    def frameScore(self, rollIndex):
        """Calculates the score based on a frame, which is 2 rolls. I.e 4 + 3 = 7"""

        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]