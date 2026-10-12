import unittest
from calculator import Calculator


class test_math(unittest.TestCase):
    def setUp(self) -> None:
        self.Calc = Calculator()

    def tearDown(self) -> None:
        pass

    def test_sum(self):
        result = self.Calc.sum(3, 4)
        target = 7
        assert result == target

    def test_subst(self):
        result = self.Calc.subst(3, 10)
        target = -7
        assert result == target

    def test_mult(self):
        result = self.Calc.mult(7, 111)
        target = 777
        assert result == target

    def test_div(self):
        result = self.Calc.div(7, 1)
        target = 7
        assert result == target

    def test_div_zero(self):
        with self.assertRaises(ValueError):
            result = self.Calc.div(3, 0)
