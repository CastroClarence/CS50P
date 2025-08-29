def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return is_two_letters(s) and contains_letters(s) and is_end(s) and not contains_special(s)

#“All vanity plates must start with at least two letters.”
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
#“No periods, spaces, or punctuation marks are allowed.”

def contains_special(plate):
    seen_special = False
    special = [".", " ", "'"]
    for letter in plate:
        if letter in special:
            seen_special = True
    return seen_special


def is_two_letters(plate):
    two_index = range(2)
    for pos, letter in enumerate(plate):
        if letter.isalpha() and pos in two_index:
            return True
        else:
            return False

def contains_letters(plate):
    num_characters = 0
    for letter in plate:
        if letter.isalpha() or letter.isnumeric():
            num_characters += 1
    if 2 <= num_characters <= 6:
        return True
    else:
        return False

def is_end(plate):
    seen_num = False

    for  letter in plate:
        if letter.isnumeric():
            if not seen_num:
                seen_num = True
                if letter == "0":
                    return False
        else:
            if seen_num:
                return False

    return True

main()
