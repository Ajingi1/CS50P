from pyfiglet import Figlet
from sys import argv
import random
import sys

figlet_var = Figlet()

font_list = figlet_var.getFonts()


if len(sys.argv) == 1:

    user_input = input("Enter the words:")

    figlet_var.setFont(font=random.choice(font_list))

    print(f"{figlet_var.renderText(user_input)}")


elif len(sys.argv) == 3:

    if argv[1] == "-f" or argv[1] == "--font":

        if argv[2] in font_list:
            user_input = input("Enter the words:")
            figlet_var.setFont(font=argv[2])
            print(f"{figlet_var.renderText(user_input)}")

        else:
            sys.exit("error Occur you enter Wrong font")

    else:
        sys.exit("error Occur you enter Wrong font")
        
else:
    sys.exit("error Occur you enter Wrong font")
