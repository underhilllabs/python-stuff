# acronymer.py
from string import split,join,upper

def acronymizer(thephrase):
    mylist = split(thephrase)
    for i in range(len(mylist)):
        mylist[i]=(mylist[i])[0:1]
    return upper(join(mylist,""))

def main():
    instr = raw_input("please enter phrase to acronymize: ")
    instr = acronymizer(instr)
    print "New acronym: %s" % (instr)

main()

