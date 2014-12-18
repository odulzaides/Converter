# Functions for converting weight


def ktop(kilograms):
    """Converts kilos to pounds"""
    pounds = kilograms * 2.2046
    print """\n\n\t{} kilograms is equal to {} pounds
    """.format(kilograms, pounds)
    from weightMenu import *
    weight()


def ptok(pounds):
    """ Converts pounds to kilos"""
    kilograms = pounds / 2.2046
    print """
    \n\n\n\t{0} pounds is equal to {1:.2f} kilograms
    """.format(pounds, kilograms)
    from weightMenu import *
    weight()


def gtoo(grams):
    ounces = grams / 28.0
    print """
    \n\n{0} grams is equalt to {1:.2f} ounces
    """.format(grams, float(ounces))
    from weightMenu import *
    weight()


def otog(ounces):
    grams = ounces * 28
    print """\n\n\t{0} ounces is equal to {1:.2f} grams.
    """.format(ounces, grams)
    from weightMenu import *
    weight()


def mltoo(milliliters):
    ounces = milliliters / 29.57
    print """\n\n{0} milliliters is equal to {1:.2f} ounces.
    """.format(milliliters, ounces)
    from weightMenu import *
    weight()


def otoml(ounces):
    milliliters = ounces * 29.57
    print """\n\n{0} ounces is equal to {1:.2f} milliliters.
    """.format(ounces, milliliters)
    from weightMenu import *
    weight()
