while True:
    try:
        fraction = input("Fraction: ")
        numerator, denominator = fraction.split("/")
        numerator = int(numerator)
        denominator = int(denominator)
        answer = (numerator / denominator) * 100
        answer = round(float(answer))

        if denominator == 0:
            raise ZeroDivisionError

        if numerator < 0 or numerator > denominator:
            raise ValueError
        break

    except (ValueError, ZeroDivisionError):
        pass

if answer >= 99:
    print("F")
elif answer <= 1:
    print("E")
else:
    print(f'{answer}%')
