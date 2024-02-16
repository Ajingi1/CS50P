def main():
    # user input
    plate = input("Plate: ")

    # call is_valid function and put the input as argumane
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # store the text here
    text = ""

    # iterate s input character by character
    for ev in s:
        # if s character is numeric
        if ev.isnumeric():
            # break the loop there
            break
        # put the text before ocurance numbers
        text += ev
        # replace the the text before number with empty
        # and return value after number
        # store them in num
        num = s.replace(text, "")
    # min lenght is 2 and max is 6
    if len(s) >= 2 and len(s) <= 6:
        # if first 2 character are alpabet
        if s[0:2].isalpha():
            # if num is not apmty
            if len(num) != 0:
                # if num is all numeric and first number is not 0
                if num.isnumeric() and num[0] != "0":
                    return True
            # if num is empty 
            elif len(num) == 0:
                return True

main()
