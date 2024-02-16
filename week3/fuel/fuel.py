# my main function
def main():
    # while my code is True
    while True:
        # try this
        try:
            # put my two number in to X and Y
            x, y = input("Fraction:").split("/")
            # convert x and y to interger
            x = int(x)
            y = int(y)
            # divide x by y
            result = x / y
            # put the final result in to the final variable and round it to 100
            final = round(result * 100)
            # if my tank is greaterthan %1 or lesthan %99 print pecentage
            if 1 < final < 99:
                print(f"{final}%")
                # if 99 or 100 print F
            elif final >= 99:
                print("F")
                # if 1 or les print E
            elif final <= 1:
                print("E")
            # if X is not greaterthan or equal to Y return false and propmt again
            if x <= y:
                return True
        # cach value error and zero division error and pass it
        except (ValueError, ZeroDivisionError):
            pass
main()
