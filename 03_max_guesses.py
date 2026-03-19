import math


#calculate number of guesses aloud
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

def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses
