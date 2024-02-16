# impport package
import inflect

# using engine fron inflect
inflect_inp = inflect.engine()

# define empty dic
array = []

# while true
while True:
    # try these
    try:
        # collect name from user
        name = input("Name:")
        # append ir to the array dic
        array.append(name)
    # when user click ctrl + d
    except EOFError:
        # if the dic length is equal to 1 or more
        if len(array) >= 1:
            # use join method from inflect
            joined_list = inflect_inp.join(array)
            # print joined names
            print(f"Adieu, adieu, to {joined_list}")
            # break from while loop 
            break
