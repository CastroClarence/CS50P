fruits = {
    "Apple" : 130,
    "Avocado" : 50,
    "Sweet Cherries" : 100,
    "Kiwifruit" : 90,
    "Pear" : 100
}

answer = input("Item: ").title()

if answer in fruits:
    print(f"Calories: {fruits[answer]}")




