due = 50

denomination = [10, 25, 5]

while due > 0:
    print(f"Amount Due: {due}")
    insert = int(input("Insert Coin: "))
    if insert in denomination:
        due -= insert

if due <= 0:
    print(f"Change Owed: {due * -1}")
