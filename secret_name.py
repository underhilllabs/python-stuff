import string
# Secret_name 

vowels = ['a','e','i','o','u']
def mk_sec_name(name):
    " go thru name char by char. skip if its a vowel, than add a new vowel to it."
    count = 0
    newname = ""
    for ch in name:
        if ch in vowels:
            print "skipping %s its a vowel" % (ch)
        else:
            if count < 1:
                newname =newname+ ch + "a"    
            else: 
                newname =newname+ ch + "o"
            count=count+1
        if count > 2:
            return newname
            
def main():
    print "this program creates a secret name for you!"
    print 
    thename = ""
    thename = raw_input("Enter name to secret-codify: ")
    thename = mk_sec_name(thename)
    print "Your secret code name is",thename.capitalize()

main()
