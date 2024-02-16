import sys


try:
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) == 3:
        sys.exit("Too many comman-line arguments")

    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    elif sys.argv[1].endswith(".py"):
        counter = 0
        with open(sys.argv[1]) as file:
            lines = file.readlines()
            for i in lines:
                if not (i.lstrip().startswith("#") or i.strip() == ""):
                    counter = counter + 1
            print(f"{counter}")

except FileNotFoundError:
    sys.exit("File does not exist")
