def main():
    user_input = input("Enter the name:")
    add_symbol(user_input)

def add_symbol(s):
    for i in s:
        while i.isupper():
            i = "_" + i
            break
        print(i.lower(), end="")
    print()


main()



