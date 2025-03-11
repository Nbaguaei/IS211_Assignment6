import unittest
from conversions import convertCelsiusToKelvin, convertCelsiusToFahrenheit

class TestTemperatureConversions(unittest.TestCase):
    
    def test_celsius_to_kelvin(self):
        """Test conversion from Celsius to Kelvin"""
        self.assertEqual(convertCelsiusToKelvin(0), 273.15)
        self.assertEqual(convertCelsiusToKelvin(100), 373.15)
        self.assertEqual(convertCelsiusToKelvin(-273.15), 0)
        self.assertEqual(convertCelsiusToKelvin(37), 310.15)
        self.assertEqual(convertCelsiusToKelvin(300), 573.15)
    
    def test_celsius_to_fahrenheit(self):
        """Test conversion from Celsius to Fahrenheit"""
        self.assertEqual(convertCelsiusToFahrenheit(0), 32)
        self.assertEqual(convertCelsiusToFahrenheit(100), 212)
        self.assertEqual(convertCelsiusToFahrenheit(-40), -40)
        self.assertEqual(convertCelsiusToFahrenheit(37), 98.6)
        self.assertEqual(convertCelsiusToFahrenheit(300), 572)

if __name__ == '__main__':
    unittest.main()
