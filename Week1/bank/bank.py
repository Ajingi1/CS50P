def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    greeting = greeting.lower()
    if "hello" in greeting:
        return 0
    elif not "hello" in greeting and greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
