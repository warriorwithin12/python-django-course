import random

def get_random_values():
    """
    Get a randomized three digit value used to play "the discover number game".
    - First, we create a 10 number list.
    - We randomize the list positions.
    - We get the 3 first values of randomized list and generates a string number list.
    - Finally we returns a number string concatenating all the digits.
    """
    digits = list(range(10))
    random.shuffle(digits)
    digits = [str(digit) for digit in digits[:3]]
    return "".join(digits)


def get_user_guess():
    """
    Get a user input guess.
    """
    user_input = input("What is your guess?")
    while len(user_input) != 3:
        user_input = input("Sorry, I need a 3 digit value. Try again:")
    return user_input

def play(random_value, user_value):
    if random_value == user_value:
        return "FULL"
    else:
        uv_list = list(user_value)
        rv_list = list(random_value)
        if uv_list[0] == rv_list[0] or uv_list[1] == rv_list[1] or uv_list[2] == rv_list[2]:
            return "MATCH"
        elif user_value[0] in rv_list or user_value[1] in rv_list or user_value[2] in rv_list:
            return "CLOSE"
        else:
            return "NOPE"

if __name__ == "__main__":
    print("Hello! Wellcome to \"the discover number game\".")
    random_value = get_random_values()
    user_value = get_user_guess()
    result = play(random_value, user_value)

    while result != "FULL":            
        print(result)
        user_value = get_user_guess()
        result = play(random_value, user_value)

    if result == "FULL":
        print("Congratulations! You discovered the hidden number {}!".format(random_value))
        exit()


    
