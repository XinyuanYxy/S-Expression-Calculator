

import unittest
import random

from calc import SExpressionCalculator


class SExpressionCalculatorTest(unittest.TestCase):

    def test_no_function(self):
        s_expression_calculator = SExpressionCalculator()
        
        # explicit checks
        self.assertEqual(s_expression_calculator.calculate('0'), 0)
        self.assertEqual(s_expression_calculator.calculate('1'), 1)
        self.assertEqual(s_expression_calculator.calculate('2'), 2)
        self.assertEqual(s_expression_calculator.calculate('3'), 3)
        self.assertEqual(s_expression_calculator.calculate('16'), 16)
        self.assertEqual(s_expression_calculator.calculate('32'), 32)
        self.assertEqual(s_expression_calculator.calculate('64'), 64)
        self.assertEqual(s_expression_calculator.calculate('128'), 128)
        self.assertEqual(s_expression_calculator.calculate('256'), 256)
        self.assertEqual(s_expression_calculator.calculate('512'), 512)

        # check numbers between [0, 1000)
        for i in range(0, 1000):
            self.assertEqual(s_expression_calculator.calculate(str(i)), i)

        # check 100 random numbers between 0 and 10,000
        for i in range(0, 100):
            val = random.randrange(10001)
            self.assertEqual(s_expression_calculator.calculate(str(val)), val)

    def test_single_add(self):
        s_expression_calculator = SExpressionCalculator()
        
        # explicit checks
        self.assertEqual(s_expression_calculator.calculate('(add 2 2)'), 4)
        self.assertEqual(s_expression_calculator.calculate('(add 12 34)'), 46)
        self.assertEqual(s_expression_calculator.calculate('(add 123 456)'), 579)

        # check 0 + 0 through 100 + 100
        for i in range(0, 100):
            for j in range(0, 100):
                self.assertEqual(s_expression_calculator.calculate('(add ' + str(i) + ' ' + str(j) + ')'), i + j)

        # check 100 random numbers between 0 and 10,000
        for i in range(0, 100):
            a = random.randrange(10001)
            b = random.randrange(10001)
            self.assertEqual(s_expression_calculator.calculate('(add ' + str(a) + ' ' + str(b) + ')'), a + b)

    def test_single_multiply(self):
        s_expression_calculator = SExpressionCalculator()
        
        # explicit checks
        self.assertEqual(s_expression_calculator.calculate('(multiply 1 1)'), 1)
        self.assertEqual(s_expression_calculator.calculate('(multiply 12 4)'), 48)
        self.assertEqual(s_expression_calculator.calculate('(multiply 123 456)'), 56088)

        # check 0 * 0 through 100 * 100
        for i in range(0, 100):
            for j in range(0, 100):
                self.assertEqual(s_expression_calculator.calculate('(multiply ' + str(i) + ' ' + str(j) + ')'), i * j)

        # check random values between 0 through 10,000 (100 times)
        for i in range(0, 100):
            a = random.randrange(10001)
            b = random.randrange(10001)
            self.assertEqual(s_expression_calculator.calculate('(multiply ' + str(a) + ' ' + str(b) + ')'), a * b)

    def test_nested_functions(self):
        s_expression_calculator = SExpressionCalculator()
        
        # 1 layer nesting
        self.assertEqual(s_expression_calculator.calculate('(add (add 2 2) 5)'), 9)
        self.assertEqual(s_expression_calculator.calculate('(add (multiply 2 2) 5)'), 9)

        self.assertEqual(s_expression_calculator.calculate('(add 5 (add 1 2))'), 8)
        self.assertEqual(s_expression_calculator.calculate('(add 6 (multiply 2 2))'), 10)

        self.assertEqual(s_expression_calculator.calculate('(add (add 2 4) (add 6 8))'), 20)
        self.assertEqual(s_expression_calculator.calculate('(add (add 2 4) (multiply 6 8))'), 54)
        self.assertEqual(s_expression_calculator.calculate('(add (multiply 1 3) (add 2 4))'), 9)
        self.assertEqual(s_expression_calculator.calculate('(add (multiply 5 3) (multiply 3 4))'), 27)

        self.assertEqual(s_expression_calculator.calculate('(multiply (add 2 2) 5)'), 20)
        self.assertEqual(s_expression_calculator.calculate('(multiply (multiply 2 2) 5)'), 20)

        self.assertEqual(s_expression_calculator.calculate('(multiply 3 (add 1 2))'), 9)
        self.assertEqual(s_expression_calculator.calculate('(multiply 3 (multiply 1 2))'), 6)

        self.assertEqual(s_expression_calculator.calculate('(multiply (add 2 4) (add 6 8))'), 84)
        self.assertEqual(s_expression_calculator.calculate('(multiply (multiply 1 3) (multiply 3 4))'), 36)
        self.assertEqual(s_expression_calculator.calculate('(multiply (add 1 2) (multiply 1 2))'), 6)
        self.assertEqual(s_expression_calculator.calculate('(multiply (multiply 5 3) (add 3 4))'), 105)

        # More layer nesting
        self.assertEqual(s_expression_calculator.calculate('(multiply (add (multiply 1 2) 3) (add 1 2))'), 15)
        self.assertEqual(s_expression_calculator.calculate('(multiply (add (multiply 1 2) (add 3 4)) (multiply (add 5 6) (multiply 7 8)))'), 5544)

    def test_error_handling(self):
        s_expression_calculator = SExpressionCalculator()
        self.assertEqual(s_expression_calculator.calculate('(ad 4 6)'), "Please enter a valid function")
        self.assertEqual(s_expression_calculator.calculate('(multiply (add (multiply 1 2) (add 3 4)) (multi (add 5 6) (multiply 7 8)))'), "Please enter a valid function")
        self.assertEqual(s_expression_calculator.calculate('(multiply (add (multiply 12) (add 3 4)) (multiply (add 5 6) (multiply 7 8)))'), "You may enter an input with not supported format")
        self.assertEqual(s_expression_calculator.calculate('(multiply (add (multiply 1 2) add 3 4) (multiply (add 5 6) (multiply 7 8)))'), "You may enter an input with not supported format")



if __name__ == "__main__":
    unittest.main()