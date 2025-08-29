answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

# Make answer to lower case to make answer insensitive and remove whitespaces
answer = answer.lower().strip()

if answer == "42" or answer == "forty two" or answer == "forty-two":
        print("Yes")
else:
        print("No")
