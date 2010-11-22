# fact.py compute a factorial

def main():
    print "factorial - compute a factorial"
    n = input("Enter a number:")
    total = 1
    for fact in range(n,1,-1):
        total = total * fact
    print "Factorial of", n, "is", total

main()
    
    
