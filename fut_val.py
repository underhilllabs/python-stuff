# fut_val.py
# compute the value of an investment in 10 years at a set interest rate
from math import exp

def main():
    print "This program computes the value of an investment after a specified number of years."
    print 
    princ = input("Please enter amount you are investing per year. $")
    rate = input("Please enter interest rate in decimal format: ")
    years = input("Please enter how many years: ")
    origp = princ + 0
    totalp = 0
    for i in range(years):
        totalp = (totalp + princ) * (1 + rate) 
    print "After ", years, " years at ", rate, " percent interest, your investment is: ", totalp
    princ = origp
    totalp = 0
    for i in range(years):
        totalp = (totalp + origp) * exp(rate*1) 
    
    princ = origp + princ
    print "with continuous compounding it will be: ", totalp


main()
