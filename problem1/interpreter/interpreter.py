def main():
    answer = input("Expression: ")

    x, y, z = answer.split(" ")

    answer = solve(int(x), y, int(z))

    print(float(answer))

def solve(x, y, z):
    if y == "+":
        return x+z
    elif y == "-":
        return x-z
    elif y == "/":
        return x/z
    elif y == "*":
        return x*z

main()
