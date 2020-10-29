"""Library of units converters"""

# Declare useful constants
NPL = 4.44822 # newtons per pound-foot
IPM = 1550 # square inches per square meter
LPN = 0.224809 # pound-force per newton
MPI = 0.00064516 # meters squared per inch squared

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
