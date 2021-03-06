#Author Andrew Clavin
"""
Write a class that represents a rational number
(i.e., a number that can be represented as a fraction).
The constructor for your class should take as parameters
a numerator and denominator. In addition,
implement the following methods for your class:
• arithmetic: __add__, __sub__, __mul__, __truediv__
• comparison: __lt__, __eq__, __le__
• __str__
When you are done, you should be able to perform calculations
like the following:
a = Rational(3, 2) # 3/2
b = Rational(1, 3) # 1/3
sum = a + b
print(sum)
print(a < b)
"""

class Rational:
    """Rational Number Class"""
    def __init__(self, numerator, denomenator):
        self.numerator = numerator
        self.denomenator = denomenator
        self.value = "" + str(numerator) + "/" + str(denomenator)
        self.digit = numerator / denomenator

    def __add__(self, summand):
        numerator = (self.numerator * summand.denomenator) + (summand.numerator * self.denomenator)
        denomenator = (self.denomenator * summand.denomenator)
        return "" + str(numerator) + "/" + str(denomenator)

    def __sub__(self, term):
        numerator = (self.numerator * term.denomenator) - (term.numerator * self.denomenator)
        denomenator = (self.denomenator * term.denomenator)
        return "" + str(numerator) + "/" + str(denomenator)

    def __mul__(self, term):
        numerator = (self.numerator * term.numerator)
        denomenator = (self.denomenator * term.denomenator)
        return "" + str(numerator) + "/" + str(denomenator)

    def __truediv__(self, term):
        numerator = (self.numerator * term.denomenator)
        denomenator = (self.denomenator * term.numerator)
        return "" + str(numerator) + "/" + str(denomenator)

    def __lt__(self, other):
        if (self.numerator * other.denomenator) < (other.numerator * self.denomenator):
                     return True
        else:
                     return False
    def __eq__(self, other):
        if (self.numerator * other.denomenator) == (other.numerator * self.denomenator):
                     return True
        else:
                     return False
    def __le__(self, other):
        if (self.numerator * other.denomenator) <= (other.numerator * self.denomenator):
                     return True
        else:
                     return False
    def __str__(self):
                     return self.value


def main():
    a = Rational(3, 2)
    b = Rational(2, 3)
    print (a + b)
    print (a - b)
    print (a * b)
    print (a / b)
    print (a < b)
    print (a == b)
    print (b <= a)
    print (b.__str__())

if __name__ == '__main__':
    main()
                     
