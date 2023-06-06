import pytest

from Calculator import Calculator

class TestCalc:
   def setup(self):
       self.calc = Calculator

   def test_multiply_calculate_correctly(self):
       assert self.calc.multiply(self, 2, 2) == 4

   def test_division_calculate_correctly(self):
       assert self.calc.division(self, 6, 2) == 3

   def test_subtraction_calculate_correctly(self):
       assert self.calc.subtraction(self, 5, 4) == 1

   def test_adding_calculate_correctly(self):
       assert self.calc.adding(self, 4, 4) == 8

   def test_rooting_calculate_correctly(self):
       assert self.calc.rooting(self, 25) == 5

   def test_squaring_calculate_correctly(self):
       assert self.calc.squaring(self, 2, 2) == 4

   def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
          self.calc.division(self, 1, 0)

def teardown(self):
    print('  Выполнение метода Teardown')