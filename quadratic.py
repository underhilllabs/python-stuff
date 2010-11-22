# quadratic.py
# this program calculates the roots of a quadratic equation
# WARNING it crashes if there are no real roots
from math import sqrt

def main():
    print "This program calculates the real roots of a quadratic equation"
    a, b, c = input("please enter the coefficients (a, b, c): ")
    discroot = sqrt(b * b - 4 * a * c)
    root1 = -b + discroot
    root2 = -b - discroot
    print "The roots are", root1, "and", root2


main()
