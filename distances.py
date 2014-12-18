"""
Menu to convert distances
"""


def km_miles(kilometers):
    """Converts kilometers to miles"""
    miles = kilometers * 0.621371
    print "\n\n\t{0} kilometers is {1} miles ".format(kilometers, miles)
    from distances import *
    distance()

def miles_km(miles):
    """Converts miles to kilometers"""
    km = miles * 1.60934
    print "\n\n\t{0}miles is {1} kilometers ".format(miles, km)
    from distances import *
    distance()


def distance():
    print """
    What would you like to convert?
    \t1. Kilometers to miles.
    \t2. Miles to kilometers.
    \t3. Return to main menu
    """
    choice = input("Enter choice: ")

    if choice == 1:
        kilometers = input("Enter kilometers to be converted")
        km_miles(kilometers)
    if choice == 2:
        miles = input("Enter miles to be converted.")
        miles_km(miles)
    if choice == 3:
        import converter
        converter.menu()
