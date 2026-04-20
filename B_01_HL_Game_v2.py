import math
import random




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
(where the number is between 1 and 10) Then choose how many rounds you'd like to play <enter> for infinite mode 

Your goal is to try to guess the secret number without running out of guesses. 

Good luck
    """)


# checks for an integer with optional upper /
# lower limits and optional exit code for infinite mode
# / quitting the game
def int_check(question, low=None, high=None, exit_code=None,):


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

        # check for infinite mode
        if response == "":
            return "infinite"

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
end_game = "no"
feedback = ""

game_history = []
all_scores = []

print("⬆️⬆️⬆️Welcome to the higher lower game⬇️⬇️⬇️")
print()


want_instructions = string_checker("Do you wish to see the instructions? ").lower()

#checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

#user enters username
username = input("What you you like to be referred as? ")
if username == "":
    username = "user"

# Ask the user for number of rounds / infinite mode
num_rounds = int_check(f"How many rounds would you like to play {username}? <enter for infinite>: ",
                       low=1, exit_code="")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# ask user if they want to customise the number range
default_params = string_checker("Do you want the default game parameters? ")
if default_params == "yes":
    low_num = 0
    high_num = 10

# Allow user to choose the high / low number
else:
    low_num = int_check("Low number? ")
    high_num = int_check("High number? ", low=low_num + 1)

# calculate the maximum number of guesses based on the low and high number
guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        round_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (Infinite mode) ♾️♾️♾️"
    else:
        round_heading = f"\n3️⃣2️⃣1️⃣💿📀💿 Round {rounds_played + 1} of {num_rounds} 1️⃣2️⃣3️⃣"

    print(round_heading)

    # Round starts here
    #set guesses used to zero at the start of each round
    guesses_used = 0
    already_guessed = []

    # Choose a 'secret' number between low and high
    secret = random.randint(low_num, high_num)

    guess = ""
    while guess != secret and guesses_used < guesses_allowed:

        # ask the user to guess teh number
        guess = int_check(f"{username}'s guess is: ", low_num, high_num, "xxx")

        if guess == "xxx":
            # set end_game to use so that outer loop can be broken
            end_game = "yes"
            break

        # check that guess is not a duplicate
        if guess in already_guessed:
            print(f"{username} you have already guessed {guess}. You still have"
                  f" {guesses_used} / {guesses_allowed} guesses")
            continue

        # if guess is not a duplicate, add it to the 'already guessed' list
        else:
            already_guessed.append(guess)

        # add one number to the number of guesses used
        guesses_used += 1

        # compare the user's guess with the secret number set up feed back statement

        # if we have guesses left
        if guess < secret and guesses_used < guesses_allowed:
            feedback = (f"Too low {username}, please try a higher number"
                        f" You've used {guesses_used} / {guesses_allowed} guesses")

        elif guess > secret and guesses_used < guesses_allowed:
            feedback = (f"Too high {username}, please try a lower number"
                        f" You've used {guesses_used} / {guesses_allowed} guesses")

        # when the secret number is guessed, we have three different feedback
        # options (lucky / phew / well done)
        elif guess == secret:

            if guesses_used == 1:
                feedback = "Oh, did you cheat?"

            elif guesses_used == guesses_allowed:
                feedback = f"damn, got it in {guesses_used} not your best work {username}."

            else:
                feedback = f"NOICE, you got it in just {guesses_used} guesses {username}."


        # if there are no guesses left
        else:
            feedback = f"Aw shucks, {username} ran outta guesses"

        # print feed back to user
        print(feedback)

        if guess == secret:
            break

        # additional feedback (warn user that they are running out of guesses)
        if guesses_used == guesses_allowed - 1:
            print("\n⏱️ Running outta time there bud, one guess to go ⏱️\n")





    # Round ends here

    # add round result to game history

    if end_game == "yes":
        break

    history_feedback = f"Round {rounds_played + 1}: {feedback}"
    game_history.append(history_feedback)

    all_scores.append(guesses_used)

    # if users are in infinite mode, increase number of rounds!
    rounds_played += 1


    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

if rounds_played > 0:
    # Game history / statistics area

    # ask if user want see game history and output if requested
    see_history = string_checker(f"\nWould you like to see the games history {username}? ")
    if see_history == "yes":
        for item in game_history:
            print(item)

    print("all scores", all_scores)

    # calculate statistics
    all_scores.sort()
    best_score = all_scores[0]
    worst_score = all_scores[-1]
    average_score = sum(all_scores) / len(all_scores)

    # Output statistics
    print("\n📊📊📊Statistics📊📊📊")
    print(f"{username}'s best score: {best_score} | {username}'s worst score: {worst_score} | {username}'s average score: {average_score:.2f}")
    print()