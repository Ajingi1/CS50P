import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matche = re.findall(r'\bum\b', s, re.IGNORECASE)
    counter = 0
    # print(matche)
    for um in range(len(matche)):
        counter = counter + 1
    return counter
if __name__ == "__main__":
    main()
