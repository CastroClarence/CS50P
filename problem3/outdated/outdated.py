import re
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()

        if "/" in date:
            date = re.split(r"[/]+", date)
            if date[0].isalpha():
                raise ValueError
        elif "," in date:
            date = re.split(r"[\s,]+", date)

        month = 0
        day = 0
        year = 0

        month, day, year = date

        day = int(day)

        if month.isalpha():
            month = months.index(month) + 1

        month = int(month)

        if  1 < month > 12 or 1 < day > 31:
            raise KeyError

    except KeyError:
        pass
    except ValueError:
        pass
    else:
        print(f"{year}-{month:02}-{day:02}")
        break

