from string import join,upper,lower,capitalize,split
def main():
    print "Find the numeric value of a name."
    print
    names=[]
    names = split(upper(raw_input("Please enter name: ")))
    total = 0
    for name in names:
        for ch in name:
            # A is 65
            total = total+ ord(ch)-64
    print "Numeric value of %s is %d" % (capitalize(lower(name)),total)

main()
