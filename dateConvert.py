# dateConvert - convert dates to strrings
from string import split

def main():
    print "dateConvert, convert a date to a string"
    print

    monthStr, dateStr, yearStr = split(raw_input("Enter date (mm/dd/YYYY): "),"/")
    months = ["January","February","March","April","May","June","July","August","September","October",
              "November","December"]
    #print "The date entered:", months[int(monthStr)-1], dateStr+",", yearStr
    print "The date entered: %s %s, %s" % (months[int(monthStr)-1], dateStr, yearStr)

main()
