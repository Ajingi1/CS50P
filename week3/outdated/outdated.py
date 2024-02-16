# i wasted many time to figue out how to do this assignment but i learn many thing in my reseach
def main():
    month_name = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        user_input = input("input a date:")
        # month_inp = ""
        # day_inp = ""
        # year_inp = ""
        try:
            if "/" in user_input:
                month_inp, day_inp, year_inp = user_input.split("/")
                if (0 < int(month_inp) <= 12 and 0 < int(day_inp) < 31):
                    break
            elif "," in user_input:
                    month_inp, day_inp, year_inp = user_input.split(" ")
                    day_inp = day_inp.replace(",", "")
                    for i in month_name:
                        if month_inp == i:
                            month_inp = month_name.index(i) + 1
                    if (0 < int(month_inp) <= 12 and 0 < int(day_inp) < 31):
                        break
            # else:
            #     return False
        except:
            print()
            pass
    # convert month and day input to interger to handle adding 0 before them and remove every sapce in the year input
    month_inp = int(month_inp)
    day_inp = int(day_inp)
    year_inp = year_inp.strip()
    print(f"{year_inp}-{month_inp:02}-{day_inp:02}")


main()
