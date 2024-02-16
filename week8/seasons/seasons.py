from datetime import datetime, date, time
import re
import sys
import inflect
import operator

def main():
    birth_date = Validate_date(input("Enter the Date YYYY-MM-DD "))
    # print(date.today())
    # print(get_days("2023-02-14"))
    dif = get_dif(birth_date)
    minutes = convert_to_minutes(dif)
    words = convert_to_words(minutes)
    print(words)

def Validate_date(birth_date):
    matche = re.search(r"(([1-2][9][7-9][0-9])|(20[0-3][0-9]))-([0-1][0-9]-([0-3][0-9]))", birth_date)
    if not matche:
        sys.exit("Invalid date")
    else:
        return birth_date

def get_dif(birth_date):
    dif = operator.sub(date.today(), date.fromisoformat(birth_date))
    return dif.days
def convert_to_minutes(days):
    minutes = days * 24 * 60
    return minutes

def convert_to_words(minute):
    convert = inflect.engine()
    words = convert.number_to_words(minute)
    words = re.sub(r"\band\b", "", words, re.IGNORECASE)
    words = words.capitalize().replace("  ", " ")
    return f"{words} minutes"


if __name__ == "__main__":
    main()
