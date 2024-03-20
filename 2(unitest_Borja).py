# test_unittest.py
import unittest

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("¡No se puede dividir por cero!")
    return a / b

class TestFunciones(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(3, 5), 8)
        self.assertEqual(suma(-3, 5), 2)
        self.assertEqual(suma(0, 0), 0)

    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)
        self.assertEqual(resta(-3, 5), -8)
        self.assertEqual(resta(0, 0), 0)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(3, 5), 15)
        self.assertEqual(multiplicacion(-3, 5), -15)
        self.assertEqual(multiplicacion(0, 5), 0)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(-10, 2), -5)
        self.assertEqual(division(0, 5), 0)

    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            division(10, 0)
    
    
            

if __name__ == '__main__':
    unittest.main()
