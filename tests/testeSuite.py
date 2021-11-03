import unittest
from expense import new_expense

class TestExpense(unittest.TestCase):

    def test_add_expense(self):
        self.assertEqual(new_expense(23, 'toto', 'pchojka'), True)
        self.assertEqual(new_expense('bonjour',23,23), False)

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestExpense))
    return test_suite

mySuit=suite()

runner=unittest.TextTestRunner()
runner.run(mySuit)