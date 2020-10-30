"""Unit tests for the units converter Library functions"""

# inport the functions to be tested
from converters import psi2kpa, kpa2psi, mpg2LP100K, LP100K2mpg

def describe_a_library_of_units_converters():
    """Tests suite for units conversion functions"""
    # pylint: disable=unused-variable
    def blows_smoke():
        assert True

    def can_convert_psi_to_kpa():
        assert psi2kpa(32) == 220.631712 # 32psi == 220.631712 KPA; average car tire pressure
        assert psi2kpa(8.5) == 58.6052985 # 8.5psi == 58.6052985 KPA; average basketball pressure
 
    def can_convert_kpa_psi():
        assert kpa2psi(101.325) == 14.695952495133 # kpa to psi; average air pressure at sea level
        assert kpa2psi(220.631712) == 31.999932479367043 # kpa to psi; average car tire pressure

    def can_convert_mpg_to_LP100K():
        assert mpg2LP100K(1/40) == 5.8803694563 # gpm to LP100K; car that gets good gas mileage
        assert mpg2LP100K(1/14.5) == 16.22170884496552 # gpm to LP100K; average diesel truck gas mileage

    def can_convert_LP100K_to_mpg():
        assert LP100K2mpg(5.8803694563) == 0.024999953625019847 # LP100k to gpm; car that gets good gas mileage
        assert LP100K2mpg(36) == 0.15305132393280002 # LP100k to mpg; average semi-truck gas mileage
