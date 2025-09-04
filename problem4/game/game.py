import random
while True:
    try:
        level = int(input("Level: "))
        if level <= 0 :
            raise ValueError
    except ValueError:
        pass
    else:
        if level == 1:
            num = random.randint(level, level)
        else:
            num = random.randrange(1, level)
        while True:
            try:
                guess = int(input("Guess: "))
                if guess <= 0 :
                    raise ValueError
            except ValueError:
                pass
            else:
                if guess < num:
                    print("Too small!")
                elif guess > num:
                    print("Too large!")
                else:
                    print("Just right!")
                    exit()
