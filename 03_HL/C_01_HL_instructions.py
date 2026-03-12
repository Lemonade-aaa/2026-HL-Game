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

# Main routine
print()
print("⬆️⬆️⬆️Welcome to the higher lower game⬇️⬇️⬇️")
print()

#ask user is the want to see instructions and display
#them if prompted
want_instructions = string_checker("Do you wish to see the instructions? ").lower()

#checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()
