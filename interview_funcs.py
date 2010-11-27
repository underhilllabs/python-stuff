from string import join
def reverse_str(str):
    new_str = []
    for c in str:
        new_str.insert(0,c)
    print join(new_str,"")
        

def sum_ints_file(file_name):
    "sum the integers in a file, one int per line"
    f = open(file_name, "r")
    total = 0
    for line in f.readlines():
        total = total + eval(line)
    return total

def mult_grid(n):
    for i in range (1,n+1):
        for j in range (1,n+1):
            print "%3.d" % (i*j),
        print
    
def prodd(n):
    # print odd numbers from 1 to n
    for i in range(1,n+1):
        if (i%2):
            print i,

def fib(n):
    if n<2:
        return n
    else: 
        return fib(n-1)+fib(n-2)

def main():
    #print sum_ints_file("/home/bart/numbers.txt")
    mult_grid(12)
    print 
    prodd(100)
    print 
    reverse_str("one ring")
    print
    #for i in range (1,31):
    print "fib of",30, fib(30)

main()
