import sys
import re

class SExpressionCalculator:
    # use stack to store operators and numbers, then the most inner function will be calculated first.
    ops = []
    nums = []
    supporttedOPs = ['add', 'multiply']
    def eval(self):
        b = self.nums.pop()
        a = self.nums.pop()
        op = self.ops.pop()
        x = 0
        if op == 'add':
            x = a + b
        elif op == 'multiply':
            x = a * b
        self.nums.append(x)

    def calculate(self, expr):
        try:
            # clear ops and nums every time for a new calculation
            self.ops = []
            self.nums = []
            # iterate through the input expression
            i = 0
            while (i < len(expr)):
                if expr[i].isdigit(): # deal with numbers
                    num = 0
                    j = i
                    while j < len(expr) and expr[j].isdigit():
                        num = num * 10 + int(expr[j])
                        j += 1
                    i = j - 1
                    self.nums.append(num)
                elif expr[i] == '(':
                    self.ops.append('(')
                elif expr[i] == ')':
                    self.eval()
                    if (self.ops[-1] == '('):
                        self.ops.pop() # pop '('
                else:
                    if expr[i].isalpha(): # deal with operators
                        op = ''
                        j = i
                        while j < len(expr) and expr[j].isalpha():
                            op += expr[j]
                            j += 1
                        i = j - 1
                        if op not in self.supporttedOPs:
                            return "Please enter a valid function"
                        self.ops.append(op)
                i += 1
            while (len(self.ops)):
                eval()
            return self.nums[-1]
        except:
            return "You may enter an input with not supported format"




def main():
    expr = sys.argv[1]
    calculator = SExpressionCalculator()
    print(calculator.calculate(expr))

if __name__ == "__main__":
    main()
