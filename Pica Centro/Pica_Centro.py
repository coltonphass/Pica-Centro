# Global Variables
Guesses      = 10   # Only allow 10 guesses for player 2
digits       = 3    # Only allow three digits for whole number
secretNumber = []   # List, this will store the full secret number and we will convert it later for output.
guess        = []   # List, this will store the full guess number and we will convert it later for output.
playerOne    = ""   # Global variable to store Player One's name
playerTwo    = ""   # Global variable to store Player Two's name

# Main 
def main():
    nameSelect() # Prompt users for name
    playPica()   # Start game loop

# Screen clear
def clearScreen():
    print('\n' * 100)

def nameSelect():
    global playerOne, playerTwo
    playerOne = input("Player one, please input your name: ")
    playerTwo = input("Player two, please input your name: ")
    clearScreen()

# Get secret number from player 1
def generateSecretNumber():
    global secretNumber
    secretNumber = [] # secret number list
    digitCount = 0  
    print("{}, please input the secret number.".format(playerOne)) # Prompt user for input
    
    # Validate input and count the amount of digits input for whole number
    while digitCount < digits:
        digit = input("Enter digit {} (0-9): ".format(digitCount + 1)) # Increment 1
        if digit.isdigit() and 0 <= int(digit) <= 9:
            secretNumber.append(int(digit))
            digitCount += 1 
        else:
            print("ERROR : Please enter a valid digit (0-9).")
    
    clearScreen() # Clear screen so player 2 can't see

# Player 2 guessing loop
def getGuess():
    global guess
    guess = [] # guess list
    # Validate input and loop 3 question and inputs
    for i in range(digits):
        while True:
            digit = input("Please enter digit {} in your guess: ".format(i + 1)) # Increment 1
            if digit.isdigit() and 0 <= int(digit) <= 9:
                guess.append(int(digit))
                break
            else:
                print("ERROR : Please enter a digit (0-9).")
    return guess

# Set rules and do logic for gameplay
def compareNumbers(guess):
    picas   = 0 # Initialize picas and centros
    centros = 0
    for i in range(digits):
        if guess[i] == secretNumber[i]: # If it's exact, increase centros
            centros += 1
        elif guess[i] in secretNumber: # If it's in the number but not in place, increase picas
            picas += 1
    return picas, centros

# Print table
def displayResults(guess, picas, centros):
    print("+-----------------------------------+")
    print("| YOUR GUESS    | PICA    | CENTRO  |")
    print("+-----------------------------------+")
    print("| {:<12} | {:<7} | {:<7}  |".format(' '\
    .join(str(_) for _ in guess), picas, centros)) # Convert guess digits to string for output
    print("+-----------------------------------+")

# ASCII winning message
def winningMsg():
       print("\n  __      _______ _____ _______ ____  _______     ___  \n"
          "  \\ \\    / /_   _/ ____|__   __/ __ \\|  __ \\ \\   / / | \n"
          "   \\ \\  / /  | || |       | | | |  | | |__) \\ \\_/ /| | \n"
          "    \\ \\/ /   | || |       | | | |  | |  _  / \\   / | |  \n"
          "     \\  /   _| || |____   | | | |__| | | \\ \\  | |  |_|  \n"
          "      \\/   |_____|\\_____| |_|  \\____/|_|  \\_\\ |_|  (_)  \n")

# ASCII losing message
def losingMsg(): 
    print("\n   _____                         ____                 \n"
          "  / ____|                       / __ \\                \n"
          " | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __  \n"
          " | | |_ |/ _` | '_ ` _ \\ / _ \\ | |  | \\ \\ / / _ \\ '__| \n"
          " | |__| | (_| | | | | | |  __/ | |__| |\\ V /  __/ |    \n"
          "  \\_____|\\__,_|_| |_| |_|\\___|  \\____/  \\_/ \\___|_|    \n")

# Game loop
def playPica():
    print("WELCOME TO PICA-CENTRO") # Welcome msg
    generateSecretNumber() # Get number from player 1
    print("{}, try to guess the secret number.".format(playerTwo)) 
    input("PRESS ENTER TO BEGIN THE GAME")
    clearScreen()

    # Game start!
    for guess_number in range(1, Guesses + 1):
        print("{} GUESS #{}".format(playerTwo, guess_number))
        guess = getGuess()
        picas, centros = compareNumbers(guess)
        displayResults(guess, picas, centros)

        # Win / lose conditions & fun ascii messages
        if centros == digits:
            winningMsg()
            print("\n{} guessed the secret number!".format(playerTwo))
            return
        elif guess_number == Guesses:
            losingMsg()
            print("\nGAME OVER! {} couldn't guess the number.".format(playerTwo))
            print("The secret number was: {}".format(' '\
            .join(str(_) for _ in secretNumber))) # Convert secretNumber digits to string then format
            return

# Main function
main()
input("Press any key to exit game")

