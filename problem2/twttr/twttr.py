vowels = ["a", "e", "i", "o" ,"u"]

answer = input("Input: ")

word = ""

upper = []
for vowel in vowels:
    upper.append(vowel.upper())

for letter in upper:
    vowels.append(letter)

for letter in answer:
    if letter not in vowels:
        word += letter

print(f"Output: {word}")


