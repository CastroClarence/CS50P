import sys
from pyfiglet import Figlet
figlet = Figlet()

if len(sys.argv) == 1:
    pass
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

answer = input("Input: ")
print(figlet.renderText(answer))







