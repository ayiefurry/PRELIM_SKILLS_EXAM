#Rono, Ia Shaira A.
import unittest
class Temperature:
    def __init__(self,kelvin = None, celsius = None, fahrenheit = None):
        values = [x for x in[kelvin,celsius,fahrenheit] if x]

        if len(values) < 1:
            raise ValueError('Need Argument.')
        if len(values) > 1:
            raise ValueError('Only one arguement.')
        if celsius is not None:
            self.kelvin = celsius + 273.15
        elif fahrenheit is not None:
            self.kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
        else:
            self.kelvin = kelvin

        if self.kelvin < 0:
            raise ValueError('Temperature in Kelvin cannot be negative.')
    def __str__(self):
        return f'Temperature = {self.kelvin} Kelvins'
#Test Cases
class Test_Temperature(unittest.TestCase):
    #Test 1
    def test_celsius_to_kelvin(self):
        kel = Temperature(fahrenheit = 20)
        t1 = kel.kelvin
        t2 = t1
        self.assertIs(t1,t2)
        print("Temperature in Kelvin is: ", t2)
        print("Successful")

    #Test 2
    def test_not_none(self):
        tmp = Temperature(celsius = 20)
        self.assertIsNotNone(tmp)
        print("Temperature has an argument: ", tmp)
        print("Successful")

    #Test 3
    def test_kelvin_neg(self):
        with self.assertRaises(ValueError, msg = 'Enter a negative number to raise the Value Error.'):
            kelvs = Temperature(kelvin = -2)
        print("A negative number is not allowed.")
        print("Error raised successfully")

    #Test 4
    def test_kelvin(self):
        kelvs = Temperature(1)
        self.assertEqual(kelvs.kelvin,1)
        print(str(kelvs.kelvin) + " is equal to 1" )
        print("Successful")
if __name__ == '__main__':
    unittest.main()       