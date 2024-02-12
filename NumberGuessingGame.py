import random
class GuessingGame(object):
    def __init__(self,lowerBound,upperBound,numberOfGuesses):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.numberOfGuesses =numberOfGuesses
    def guessNumber(self,attemptsLeft):
            userInput = input("Guess a number: ")

            if int(userInput)>self.lowerBound and int(userInput)<self.upperBound:
                print("Number guessed by a user is: ",userInput)
                return userInput
            else:
                print("Wrong number, please try again as number of chances left are: ",attemptsLeft)
                return 0
    def startGame(self):
        for i in range(1,self.numberOfGuesses+1):
            attemptsLeft = self.numberOfGuesses - i
            #invoke guessNumber method
            userInput = self.guessNumber(attemptsLeft)
            if userInput == 0:
                continue
            #Generate a random number
            randomNumer =random.randint(self.lowerBound,self.upperBound)
            print("Random number is: ",randomNumer)
            if randomNumer == int(userInput):
                print("Congratulations!")
            else:
                print("You lost the attempt no.",attemptsLeft, "try again. ")
#create Object
#change input parameter as req.
game = GuessingGame(1,5,2)
game.startGame()