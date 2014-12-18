#
#   Functions for conversion of measurement units
#


def mtof(meters):
    """Converts meters to feet"""
    rawFeet = meters * 3.280839895
    inches = (rawFeet * 12) % 12
    feet = (rawFeet * 12 - inches) / 12
    print rawFeet, inches, feet
    print """
    \n\n\n\t{0} meters equals {1} feet {2:.0f} inches
    """.format(meters, feet, inches)
    from measureMenu import *
    measure()


def ftom(feet, inches):
    """ Converts feet to meters"""
    print inches, feet
    totalFeet = feet + inches / 12
    meters = totalFeet / 3.280839895
    print """
    \n\n\n\t{0} feet {1:.0f} inches is equal to {2:.2f} meters
    """.format(feet, inches, meters)
    from measureMenu import *
    measure()


def ctoi(centimeters):
    """ Converts Centimeters to inches. """
    inches = centimeters * 0.39
    print """
    \n\n\n\t{0} centimeters is equal to {1:.2f} inches
    """.format(centimeters, inches)
    from measureMenu import *
    measure()


def itoc(inches):
    """ Converts Inches to Centimeters"""
    centimeters = inches * 2.54
    print """
    \n\n\n\t{0} inches is equal to {1:.2f} centimeters.
    """.format(inches, centimeters)
    from measureMenu import *
    measure()
