"""Library of units converters"""

# Declare useful constants
NPL = 4.44822 # newtons per pound-foot
IPM = 1550 # square inches per square meter
LPN = 0.224809 # pound-force per newton
MPI = 0.00064516 # meters squared per inch squared
MPK = 0.621372 # meters per kilometer
LPG = 3.78541 # liters per gallon
KPM = 1.60934 # kilometers per mile
GPL = 0.264172 # gallons per liter


def psi2kpa(psi):
    """
    takes in a PSI value and converts it to KPA
    """
    return psi * NPL * IPM / 1000

def kpa2psi(kpa):
    """
    takes in a KPA value and converts it to PSI
    """
    return kpa * 1000 * LPN * MPI

def mpg2LP100K(mpg):
    """
    takes in a mpg value and converts it to Liters per 100 Km
    """
    return mpg * MPK * LPG * 100

def LP100K2mpg(LP100K):
    """
    takes in a liter per 100 km value and converts it to mpg
    """
    return LP100K * KPM * GPL / 100