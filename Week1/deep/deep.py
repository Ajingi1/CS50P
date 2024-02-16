inpt = input("What is the Answer to the Great Question of Life, the Universe and Everything:")
inpt = inpt.lower().lstrip().rstrip()

match inpt:
    case "42" | "Forty Two" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
