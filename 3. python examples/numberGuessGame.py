import random
sysNumber = random.randint(0, 9)

def guessGame():
    
    print("I have a number in my RAM between (0 - 9), you got three chances to guess it?")
    chances = 3

    while True:
        try:

            # while True:
            userNumber = int(input("Enter your Guess (00 to STOP) : "))

            if (userNumber == sysNumber):
                print("Yay; your right")
                break
            elif (userNumber < sysNumber):
                chances -= 1
                print("My number is larger than yours. you got {} chances only.".format(chances), end="\n\n")
            else:
                chances -= 1
                print("My number is smaller than yours. you got {} chances only.".format(chances), end="\n\n")
            
            if (chances == 0):
                print("TIMED OUT, My Number is {}".format(sysNumber))
                break
            elif (userNumber == 00):
                print("Your Quit: My Number is {}".format(sysNumber))
                break

        
        except ValueError as err:
            print("ValueError: ", err)


# function call
guessGame()