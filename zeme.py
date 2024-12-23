# import zeme
import time
import webbrowser
def products():
    productloop = True
    while productloop:
        print("Type the letter hilighted by brackets '()' to go to product GitHub page")
        product = input("(A)dvanced Maths, (L)ists\n")
        if product == "a":
            webbrowser.open("https://github.com/ZemeTechnologies/zeme/tree/AdvancedMath", 2)
            productloop = False
        elif product == "l":
            webbrowser.open("https://github.com/ZemeTechnologies/zeme/tree/zemeLists", 2)
            productloop = False
        else:
            print("Try again.")
def intro():
    for i in range(3):
        time.sleep(0.3)
        print("/")
        time.sleep(0.3)
        print("|")
        time.sleep(0.3)
        print("\\")
    websitepromptloop = True
    while websitepromptloop:
        websiteprompt = input("Would you like to go to the Zeme Website? (y/n)\n")
        if websiteprompt == "y":
            webbrowser.open("zemetechnologies.github.com", 2)
            websitepromptloop = False
        elif websiteprompt == "n":
            print("Continuing to Zeme Product Select.")
            products()
            websitepromptloop = False
        else:
            print("Try again.")
            continue
intro()