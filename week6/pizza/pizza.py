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
        table = []
        with open(sys.argv[1]) as file:
            for line in file:
                name, s_size, x_size = line.rstrip().split(",")
                pizza_line  = {}
                pizza_line["name"] = name
                pizza_line["s_size"] = s_size
                pizza_line["x_size"] = x_size
                table.append(pizza_line)
            print(tabulate(table, headers="firstrow", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
