import sys
from tabulate import tabulate
import csv


try:
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) == 3:
        sys.exit("Too many comman-line arguments")

    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    elif sys.argv[1].endswith(".csv"):
        with open(sys.argv[1]) as file:
            lines = csv.reader(file)
            print(tabulate(lines,  headers ="firstrow", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
