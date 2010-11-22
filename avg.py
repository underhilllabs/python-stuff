# avg.py
# program reads in a list of scores and prints out the average

def main():
    print "This program reads in a list of scores and prints out the average"
    score1 = input("Please enter the first score: ")
    score2 = input("Please enter the second score: ")
    score3 = input("Please enter the third score: ")
    my_avg = (score1 + score2 + score3) / 3.0
    print "The average of score of ", score1,",", score3, "and ", score2, "is ", my_avg

main()

