def main():
    print "Grade Report: enter number between 5-0 and returns a letter grade"
    print 
    
    grade_letters = ["F","F","F","F","F","F","D","C","B","A"]
    grade_num = raw_input("Please enter a grade from 0-100: ")
    grade_num = (eval(grade_num)-1)/10
    if grade_num > 100 or grade_num < 0:
        print "You failed!"
    else:
        print "Grade is %s" % (grade_letters[grade_num])

main()
    
