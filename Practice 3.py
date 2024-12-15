import random

## example of guessing number 
def startgame():
    b = random.randint(0,1001)
    print('Welcome to the guessing game, guess the number, you have ten tries')
    user_input = input("Type 'y' to start, 'n' to stop, or 'c' to cancel: ")
    
    if user_input.lower() == 'y':
        # Start the game
        tries = 10
        while tries > 0 :
            a = int(input('Guess a number between 1 to 1000: '))
            if 0 < a < 1001:
                # Your game logic goes here
                # comparing now
                if a > b:
                    print('Lower!')
                elif a < b:
                    print('Higher')
                else:
                    print("Correct Number!")
                    break
                tries -= 1
                print ("You have",tries,"tries left")
            else:
                print("Choose a number between 1 and 1000.")
        if tries == 0:
            print("Sorry, you ran out of tries. The number was", b)
    elif user_input.lower() == 'n':
        print("Game stopped.")
    elif user_input.lower() == 'c':
        print("Game cancelled.")
    else:
        print("Invalid input. Please try again.")

    
startgame()