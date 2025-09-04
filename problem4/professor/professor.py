import random


def main():
    level = get_level()
    score = 0

    # 10 tries
    for _ in range(10):
        tries = 0
        x, y = generate_integer(level), generate_integer(level)
        key = x + y

        while tries < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if x + y == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1

                    if tries == 3:
                        print(f"{x} + {y} = {key}")
                    else:
                        pass
            except ValueError:
                pass

    print(f"{score}")

def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            level = int(input("Level: "))
            if level not in levels:
                raise ValueError
        except ValueError:
            pass
        else:
            return level


def generate_integer(level):
    if level == 1:
        start = 0
    else:
        start = 10 ** (level -1)
    end = 10 ** (level)

    return random.randint(start, end-1)


if __name__ == "__main__":
    main()
