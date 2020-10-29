"""Unit tests for the units converter Library functions"""

# inport the functions to be tested
from converters import psi2kpa, kpa2psi

def describe_a_library_of_units_converters():
    """Tests suite for units conversion functions"""
    # pylint: disable=unused-variable
    def blows_smoke():
        assert True

    def can_convert_psi_to_kpa():
        assert psi2kpa(32) == 220.631712 # 32psi == 220.631712 KPA; average car tire pressure
        assert psi2kpa(8.5) == 58.6052985 # 32psi == 58.6052985 KPA; average basketball pressure
 
    def can_convert_kpa_psi():
        assert kpa2psi(101.325) == 14.695952495133 # kpa to psi; average air pressure at sea level
        assert kpa2psi(220.631712) == 31.999932479367043 # kpa to psi; average car tire pressure