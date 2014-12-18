#   Menu for Weight Conversions
#   This calls on the 'weight.py' module
#   for the calculations

from weight import *


def weight():
    """ Weight conversion menu """
    print """What would you like to convert?
    \t1. Kilograms to Pounds.
    \t2. Pounds to Kilograms.
    \t3. Grams to Ounces
    \t4  Ounces to grams
    \t5. Milliliters to Ounces.
    \t6. Ounces to Milliliters.
    \t7. Return to Main Menu.
    """
    choice = input("Enter choice: ")
    if choice == 1:
        kilograms = input("Enter kilograms to convert: ")
        ktop(kilograms)
    if choice == 2:
        pounds = input("Enter pounds to convert: ")
        ptok(pounds)
    if choice == 3:
        grams = input("Enter grams to convert: ")
        gtoo(grams)
    if choice == 4:
        ounces = input("Enter ounces to convert: ")
        otog(ounces)
    if choice == 5:
        milliliters = input("Enter milliltiers to convert: ")
        mltoo(milliliters)
    if choice == 6:
        ounces = input("Enter ounces to convert: ")
        otoml(ounces)
    if choice == 7:
        from converter import *
        menu()
