from validator_collection import validators, checkers, errors

def main():
    print(validate(input("What's your email address?")))



def validate(s):
    try:
        if(validators.email(s)):
            return "Valid"
    except errors.EmptyValueError:
        return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()
