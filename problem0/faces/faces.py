def main():
    message = input()
    message = convert(message)
    print(message)


def convert(message):
    message = message.replace(":)", "🙂")
    message = message.replace(":(", "🙁")
    return message

main()


