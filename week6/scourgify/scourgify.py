import sys
import csv
def main():
    if (len(sys.argv) <= 1 or len(sys.argv) == 2):
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif (len(sys.argv) == 3 and sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
            with open(sys.argv[1]) as readerfile:
                before = csv.DictReader(readerfile)
                with open(sys.argv[2], "w") as writerfile:
                    fileheader2 = ["first", "last", "house"]
                    after = csv.DictWriter(writerfile, fieldnames = fileheader2)
                    after.writeheader()
                    for row in before:
                        last, first = row["name"].split(", ")
                        house = row["house"]
                        # print(row["name"])
                        # print(first)
                        # print(last)
                        # house = row["house"]
                        after.writerow({"first":first, "last":last, "house":house})
    else:
        sys.exit(f"Could not read {sys.argv[1]}")
if __name__ == "__main__":
    main()
