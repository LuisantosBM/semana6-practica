import unittest
from src.operaciones import sumar, restar, multiplicar, dividir, potencia

class TestOperaciones(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
    
    def test_restar(self):
        self.assertEqual(restar(3, 1), 2)
        self.assertEqual(restar(3, 2), 1)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 3), 6)

    def test_dividir(self):
        self.assertEqual(dividir(6, 2), 3)
        with self.assertRaises(ValueError):
            dividir(3,0)
    
    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)

if __name__ == '__main__':
    unittest.main()
