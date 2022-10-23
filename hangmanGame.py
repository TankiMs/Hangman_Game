import random

class Hangman:
    def __init__(self):
        secretWords = ["cat", "squad", "more", "fighter", "mail", "comma", "shooter", "no", "android", "trope", "yes"]
        self.word = secretWords[random.randint(0, len(secretWords)-1)]
        self.body = ["safe", "safe", "safe", "safe", "safe", "safe"]
        self.win = False
        self.x = list(self.word)
        for i in range(0, len(self.word), 1):
            self.x[i] = "?"

    def makeGuessList(self, guess):
        for i in range(0, len(self.word), 1):
            if guess == self.word[i]:
                self.x[i] = guess
            else:
                self.x[i] = "safe"

    def addBody(self, guess):
        for i in self.word:
            if guess == self.word[i]:
                self.body[i] = "safe"
            elif self.word.find(guess) >= 0:
                self.body[i] = "safe"
            elif self.word.find(guess) < 0:
                if i == 0:
                    self.body[i] = "head"
                elif i == 1:
                    self.body[i] = "torso"
                elif i == 2:
                    self.body[i] = "left arm"
                elif i == 3:
                    self.body[i] = "right arm"
                elif i == 4:
                    self.body[i] = "left leg"
                elif i == 5:
                    self.body[i] = "right leg"

    def checkWin(self):
        print("lmao")

    def getSecret(self):
        return self.word

    def getHint(self):
        return self.body

    def getWin(self):
        return self.win


hangman = Hangman()
numGuesses = 0
print("welcome to hangman!" + "\n")
guess = input("Please enter a guess: ")
while not hangman.getWin() and numGuesses < 7:

    numGuesses += 1
    if hangman.getWin():
        print("congrats, you won")
    else:
        print("you didn't win yet, guesses remaining = " + str(6 - numGuesses))
        hangman.addBody(guess)
        print("hint = " + str(hangman.getHint()))
if not hangman.getWin():
    print("sorry, you lost, the secret word was: " + hangman.getSecret())