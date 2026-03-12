# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer that is more or equal to 1. "

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"
        try:
            # response = int(input("Please enter a integer. "))
            response = int(to_check)

            #checks the number is more than / equal to 1
            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
                print(error)

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
num_rounds = int_check("How many rounds would you like to play good sir/madam? Please press <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

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