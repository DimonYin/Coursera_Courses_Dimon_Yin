import random

# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []

    def addMoney(self, amt):
        self.prizeMoney = self.prizeMoney + amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return self.name + " ($" + str(self.prizeMoney)+")"

# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscuredPhrase, guessed):
        print(self.name + " has $" + str(self.prizeMoney) + "\n\n" +
              "Category: " + category + "\n"
              "Phrase: " + obscuredPhrase + "\n"
              "Guessed: " + ", ".join(guessed) + "\n\n")
        uInput = input("Guess a letter, phrase, or type 'exit' or 'pass': ")
        return uInput

# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        self.name = name
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty

    def smartCoinFlip(self):
        rn = random.randint(1, 10)
        if rn > self.difficulty:
            return True
        else:
            return False

    def getPossibleLetters(self, guessed):
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        vowels = ["A", "E", "I", "O", "U"]
        possibleLetters = []

        for w in letters:
            if w not in guessed:
                if self.prizeMoney < 250:
                    if w not in vowels:
                        possibleLetters.append(w)
                else:
                    possibleLetters.append(w)
        return possibleLetters

    def getMove(self, category, obscuredPhrase, guessed):
        possibleLetters = self.getPossibleLetters(guessed)

        if len(possibleLetters) == 0:
            return "pass"

        SORTEDFREQUENCIES = []
        for w in WOFComputerPlayer.SORTED_FREQUENCIES:
            SORTEDFREQUENCIES.append(w)

        goodOrBad = self.smartCoinFlip()
        h = -1
        if goodOrBad:
            for w in possibleLetters:
                if SORTEDFREQUENCIES.index(w) > h:
                    h = SORTEDFREQUENCIES.index(w)
                    return SORTEDFREQUENCIES[h]
        else:
            return random.choice(possibleLetters)
