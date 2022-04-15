class BowlingGame:

    # when object is initialised, set up an empty array for the score
    def __init__(self):
        self.rolls=[]  # score array, contains the number of pins knocked for each roll
        # Note that rolls are not frames, and may vary in number from game to game.

    # add the number of pins knocked down to the score array
    def roll(self,pins):
        self.rolls.append(pins)

    # function for calculating score based on pins knocked down.
    # Tracks a frameIndex and a rollIndex seperately.
    def score(self):
        result = 0  # variable to hold result
        rollIndex=0 # track which roll
        for frameIndex in range(10): # Each game contains ten frames, each with 1 or 2 frames.
            if frameIndex in range(10):  #if it is in the first ten frames (trying to calculate strike for last two wont work)
                #REFACTOR: ADD FOLLOWING LINE: if self.isStrike(rollIndex)
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

    # checks for a strike - returns true if the score at this index is 10.
    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10

    # Checks for a spare. Returns true if the score at this index and the following index sum to 10
    def isSpare(self, rollIndex):
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10

    # Calculates the strike score. Returns ten, Plus the sum of the next two scores
    # REFACTORED: INCORRECT METHOD NAME: CHANGE TO def strikeScore
    def strikeScore(self,rollIndex):
        # REFACTOR: INCORRECT CALCULATION. SHOULD BE 10 + [i+1] + [i+2] + ([i+1] + [i+2])
        return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]

    # Calculates the score from a spare.
    def spareScore(self,rollIndex):
        return  10+ self.rolls[rollIndex+2] # returns the total of all three frames, 1st, 2nd, 3rd.

    # Calculates the score based on a frame, which is 2 rolls. I.e 4 + 3 = 7
    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]