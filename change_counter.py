# change counter: adds up the change in your pocket.

def main():
    print "This program counts the change in your pocket!"
    quarters = input("How many quarters do you have? ")
    dimes = input("Dimes? ")
    nickels = input("Nickels? ")
    pennies = input("Pennies? ")
    total = quarters * .25 + dimes * .10 + nickels *.05 + pennies *.01
    print "The total change adds up to $", total, "!"
    
main()
