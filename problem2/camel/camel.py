def main():
    camel = input("camelCase: ")
    print(f"snake_case: {snake_case(camel)}")



def snake_case(camel):
    word = ""
    for letter in camel:
        if letter.isupper():
            letter =  f"_{letter.lower()}"
            word += letter
        else:
            word += letter
    return word

main()
