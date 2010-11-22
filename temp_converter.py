# convert celcius temp to fahrenheit

def celc_to_fahr(celc):
    return 9.0/5.0 * celc + 32

def main():
        print "This program converts a temperature in Celcius into Fahrenheit."
        print
        print "----------------------"
        print "Celcius ==> Fahrenheit"
        print "----------------------"

        for i in range(11):
            fahr = celc_to_fahr(i*10)
            print i*10, "     ==>     ", fahr

        for i in range(5):
            celcius = input("please enter celcius temp: ")
            fahr = celcius * 9.0/5.0 + 32
            print "Fahrenheit temperature is", fahr, "degrees. Thanks, come again!"


main()
