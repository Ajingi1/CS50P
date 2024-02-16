import random

def main():
    # call level funtion
    rang_inpt = level()
    # use level as input and genarate
    randm_int = random.randint(1, rang_inpt)
    # print(rang_inpt, randm_int, user_gues) // for test
    while True:
        user_gues = gues()
        if user_gues < randm_int:
            print("Too small!")
        elif user_gues > randm_int:
            print("Too large!")
        elif user_gues == randm_int:
            print("Just right!")
            break
# user input for level of guess
def level():
    # try
    try:
        # user input for interger
        level_input = int(input("Level:"))
        # if the user input is greaterthan 0
        # return the user input
        if level_input > 0:
            return level_input
        # if is = 0 or less(negative) return to the funtion again
        else:
            return level()
    # when value error occcur like string input
    # return to the funtion again
    except ValueError:
        return level()

# user guess
def gues():
    # try
    try:
        # input for guess return guess when user input is interger
        user_gues = int(input("Guess:"))
        return user_gues
    # when value error occur return to funtion again
    except ValueError:
        return gues()
if __name__ == '__main__':
    main()
