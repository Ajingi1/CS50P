def main():
    while True:
        fraction = input("Fraction:")
        fraction_check = convert(fraction)
        if fraction_check is None:
            continue
        x , y  = fraction_check

        final = round((x/y) * 100)
        if x <= y:
            print(gauge(final))
            break
def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        return x, y
    except(ValueError, ZeroDivisionError):
        return None

def gauge(percentage):
    if 1 < percentage < 99:
        return f"{percentage}%"
    elif percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"

if __name__ == "__main__":
    main()
