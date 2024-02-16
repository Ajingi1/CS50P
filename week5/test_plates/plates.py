import sys

def main():
    plate = input("Plate: ")
    if is_valid(plate) :
        print("Valid")
    else:
        print("Invalid")
        

def is_valid(s):
    text = ""
    if len(s) >= 2 and len(s) <= 6:
        if s[0:2].isalpha():
            for ev in s:
                if ev.isnumeric():
                    break
                text += ev
            num = s[len(text):]
            if len(num) != 0:
                if num.isnumeric() and num[0] != "0":
                    return True
                else:
                    return False
            elif len(num) == 0:
                return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
