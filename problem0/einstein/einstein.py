def main():
    mass = input("m: ")
    energy = einstein(int(mass))
    print(f"E: {energy}")

def einstein(m):
    energy = m * (300000000 * 300000000 )
    return energy

main()
