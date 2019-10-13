import unittest
from expression import Expression

class Test(unittest.TestCase):
    data = { 'x':1, 'y':2, 'z':1 }
    def test_equality_false(self):
        expr = Expression('x == y')
        self.assertEqual(False, expr.evaluate(self.data), 'Should be equal')
    
    def test_equality_true(self):
        expr = Expression('x == z')
        self.assertEqual(True, expr.evaluate(self.data), 'Should be equal')

    def test_gt_true(self):
        expr = Expression('y > x')
        self.assertEqual(True, expr.evaluate(self.data), 'Should be equal')

    def test_two_properties_equal(self):
        expr = Expression('x == z')
        self.assertEqual(True, expr.evaluate(self.data), 'Should be equal')


if __name__ == '__main__':
    unittest.main()
