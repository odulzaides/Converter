from measure import *

def measure():
    print """
    What would you like to convert?
    \t1. Meters to Feet.
    \t2. Feet to Meters.
    \t3. Centimeters to Inches.
    \t4. Inches to Centimeters.
    \t5. Return to main Menu.
    """
    choice = input("Enter choice: ")
    if choice == 1:
        meters = input("Enter meters to convert: ")
        mtof(meters)
    if choice == 2:
        print "Enter feet and inches."
        feet = input("Enter feet: ")
        inches = input("Enter inches: ")
        ftom(feet, inches)
    if choice == 3:
        centimeters = input("Enter centimeters to convert: ")
        ctoi(centimeters)
    if choice == 4:
        inches = input("Enter inches to convert: ")
        itoc(inches)
    if choice == 5:
        import converter
        converter.menu()
