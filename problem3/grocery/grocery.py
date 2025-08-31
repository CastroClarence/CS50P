groceries = {}

while True:
    try:
        item = input().upper()
        if item == "":
            raise KeyError
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1
    except EOFError:
        break
    except KeyError:
        pass

for grocery in sorted(groceries):
    print(groceries[grocery], grocery)


