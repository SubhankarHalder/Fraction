# Function to calculate the Greatest Common Divisor
def gcd(m,n):
    """This function calculates the Greatest Common Divisor of 2 numbers.
    It uses the Euclid's Algorithm to calculate the GCD.
    This only works if the denominator is positive """

    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

# We create a Fraction class to instantiate a fraction and perform mathematical operations on that object.

class Fraction:
    """ This is a class to represent a Fraction and perform certain fraction related mathematical operations """

    def __init__(self, top, bottom):
        """Constructor that instantiates the fraction object"""
        # When users pass a negative denominator, this is converted to a negative numerator and a positive denominator
        if bottom < 0:
            top = -top
            bottom = -bottom
        # Check whether numbers given are integers
        if isinstance(top, int) and isinstance(bottom, int):
            numerator = top
            denominator = bottom
            # Here we check whether the fraction is in the lowest terms
            common = gcd(numerator, denominator)
            self.num = numerator // common
            self.den = denominator // common

        else:
            # If numbers entered are not integers, then the program exits
            raise Exception("Numbers entered are not integers!!")
    
    def __repr__(self):
        """ Returns a strings useful for debugging """
        return f"Fraction with Numerator {self.num} and Denominator {self.den}"
        

    def __str__(self):
        """Converts the fraction object as a string that can be used for print statements"""
        # If Denominator is 1, returns the numerator.
        if self.den == 1:
            return self.num
        else:
            return str(self.num) + "/" + str(self.den)

    def getNum(self):
        """Returns the numerator of the fraction"""
        return self.num

    def getDen(self):
        """Returns the denominator of the fraction """
        return self.den

    def __add__(self, otherfraction):
        """Add the two fraction"""
        # Integers are fractions with denominator 1. 
        # The following condition takes care of this situation
        if isinstance(otherfraction, int):
            otherfraction = Fraction(otherfraction, 1)

        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den*otherfraction.den

        return Fraction(newnum, newden)

    # Implementing Radd
    # Radd ensures commutivity of addition

    __radd__ = __add__

    # Implementing iadd
    # Iadd is equivalent to +=
    __iadd__ = __add__
  
    def __eq__ (self,other):
        """ Checks whether two fractions are equal"""

        firstnum = self.num*other.den
        secondnum = other.num*self.den

        return firstnum == secondnum

    def __mul__ (self, otherfraction):
        """ Multiplies two fractions"""

        newnum = self.num*otherfraction.num
        newden = self.den*otherfraction.den

        return Fraction(newnum, newden)

    def __truediv__ (self, otherfraction):
        """ Divides two fractions"""

        newnum = self.num*otherfraction.den
        newden = self.den*otherfraction.den

        return Fraction(newnum, newden)

    def __sub__ (self, otherfraction):
        """ Subtracts two fractions"""

        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den*otherfraction.den

        return Fraction(newnum, newden)

    def comparison (self, otherfraction):
        """ This function converts fractions into decimals for comparison"""

        newnum_1 = self.num/self.den
        newnum_2 = otherfraction.num/otherfraction.den
        return newnum_1, newnum_2

    def __lt__ (self, otherfraction):
        """ Less Than Comparison"""

        newnum_1, newnum_2  = self.comparison(otherfraction)
        return newnum_1 < newnum_2

    def __gt__ (self, otherfraction):
        """ Greter than Comparison """

        newnum_1, newnum_2 = self.comparison(otherfraction)
        return newnum_1 > newnum_2

    def __ge__ (self, otherfraction):
        """Greater than Equal Comparison """

        newnum_1, newnum_2 = self.comparison(otherfraction)
        return newnum_1 >= newnum_2

    def __le__ (self, otherfraction):
        """Less Than Equal Comparison """

        newnum_1, newnum_2 = self.comparison(otherfraction)
        return newnum_1 <= newnum_2

    def __ne__ (self, otherfraction):
        """Not Equal Comparison """

        newnum_1, newnum_2 = self.comparison(otherfraction)
        return newnum_1 != newnum_2

def main():
    a = Fraction(2,-3)
    b = Fraction(3,4)
    print("Numerator:", a.getNum())
    print("Denominator:", b.getDen())
    print("Addition:",a+b)
    print("Subtraction:",a-b)
    print("Multiplication:",a*b)
    print("Division:",a/b)
    print("Comparison Left:", a<b)
    print("Comparison Right:", a>b)
    print("Greater Than Equals:", a>=b)
    print("Lesser Than Equals:", a<=b)
    print("Not Equal:", a!=b)
    a += 1
    print("+=: ", a)
    print("Evaluation Repr:", repr(a))
    
main()

