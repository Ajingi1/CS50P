import random
def main():
    level = get_level()
    score = 0
    ans = 0
    for _ in range(10):
        x, y = generate_integer(level)
        for i in range(3):
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans == (x + y):
                    score = score + 1
                    break
            except ValueError:
                pass
            else:
                    print("EEE")
                    if i == 2:
                        print(f"{x} + {y} = {x+y}")
    print(score)
def get_level():
    try:
        level = int(input("Level:"))
        rang = [1,2,3]
        if not level in rang:
            raise ValueError
        return level
    except ValueError:
        return get_level()

def generate_integer(level):
    if level == 1:
        min_rang = 0
        max_rang = 10** level -1
    else:
        min_rang = 10** (level - 1)
        max_rang = 10** level -1
    rang_x = random.randint(min_rang, max_rang)
    rang_y = random.randint(min_rang, max_rang)
    return rang_x, rang_y
if __name__ == "__main__":
    main()
