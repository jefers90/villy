
import unittest
from scr.calculadora import Calculadora

class testcalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_sumar(self):
        self.assertEqual(self.calc.sumar(2, 3), 5)

    def test_restar(self):
        self.assertEqual(self.calc.restar(5, 3), 2)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(3, 4), 12)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()
