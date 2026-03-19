import math


# checks user enters yes (y) or no (n)
def string_checker(question, valid_ans=('yes', 'no')):

    error = f"Please enter a valid option from the following list {valid_ans}"

    while True:

        #get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            #check if the user response is a word in the list
            if item == user_response:
                return item

            #check if the user response is the same as
            #the first letter of an item on the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


#Display instructions

def instructions():
    """Print instructions"""

    print("""
***INSTRUCTIONS***

To begin, choose the number of rounds and either customise the game parameters or go with the default game 
(where the number is between 1 and 100) Then choose how many rounds you'd like to play <enter> for infinite mode 

Your goal is to try to guess the secret number without running out of guesses. 

Good luck
    """)


# checks for an integer with optional upper /
# lower limits and optional exit code for infinite mode
# / quitting the game
def int_check(question, low=None, high=None, exit_code=None):

    # if any integer is allowed...
    if low is None and high is None:
        error = "please enter an integer"

    # if larger number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter and integer that is "
                 f"more than / equal to {low}")

    # if the number needs to be between low & high
    else:
        error = (f"Please enter a integer that "
                 f"is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        #check for infinite mode / exite code
        if response == exit_code:
            return response

        try:
            response = int(response)

            #check the integer is not too low
            if low is not None and response < low:
                print(error)

            #check response is more than low number
            elif high is not None and response > high:
                print(error)

            #if response is valid, return it
            else:
                return response

        except ValueError:
            print(error)

#calculate the maximum number of guesses
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses

# Main Routine Starts here

# Intialise game variables
mode = "regular"
rounds_played = 0


print("⬆️⬆️⬆️Welcome to the higher lower game⬇️⬇️⬇️")
print()


want_instructions = string_checker("Do you wish to see the instructions? ").lower()

#checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()


# Ask the user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like to play? <enter for infinite>: ", low=1, exit_code="")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Get game parameters
low_num = int_check("Low number? ")
high_num = int_check("High Number? ", low=low_num+1)
guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        round_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (Infinite mode) ♾️♾️♾️"
    else:
        round_heading = f"\n💿📀💿 Round {rounds_played + 1} of {num_rounds} 💿📀💿"

    print(round_heading)
    print()

    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1


# Game loop ends here

# Game history / statistics area