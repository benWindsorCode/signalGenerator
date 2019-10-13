import unittest
from condition import Condition

class Test(unittest.TestCase):
    data = { 'x':1, 'y':2, 'z':1 }

    def test_equality_false(self):
        cond = Condition('x == y')
        self.assertEqual(False, cond.evaluate(self.data), 'Should be equal')

    def test_multiple_conditions_with_or(self):
        cond = Condition('x == y or x >= 1')
        self.assertEqual(True, cond.evaluate(self.data), 'Should be equal')

    def test_multiple_conditions_with_and(self):
        cond = Condition('x == y and x >= 1')
        self.assertEqual(False, cond.evaluate(self.data), 'Should be equal')

    def test_multiple_conditions_beginning_brackets(self):
        # Will evaluate to ( False and True) or True
        cond = Condition('( x == y and x >= 1 ) or z == 1')
        self.assertEqual(True, cond.evaluate(self.data), 'Should be equal')

    def test_multiple_conditions_beginning_brackets_2(self):
        # Will evaluate to ( False and True) and True
        cond = Condition('( x == y and x >= 1 ) and z == 1')
        self.assertEqual(False, cond.evaluate(self.data), 'Should be equal')

    def test_multiple_conditions_end_brackets(self):
        cond = Condition('x == y or ( x == z and y > z )')
        # Will evaluate to False or ( True and True ) 
        self.assertEqual(True, cond.evaluate(self.data), 'Should be equal')

    def test_multiple_conditions_beginning_and_end_brackets(self):
        cond = Condition('( x == y or z < 1 ) and ( x == y and z == x)')
        # Will evaluate to ( False or True ) and ( False and True ) 
        self.assertEqual(False, cond.evaluate(self.data), 'Should be equal')

if __name__ == '__main__':
    unittest.main()
