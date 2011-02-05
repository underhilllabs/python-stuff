#!/usr/bin/env python
from math import pow
# functions for use with Digital Circuits

# binary to decimal
def bin_to_dec(num):
    total = 0
    i = 0
    for dig in str(num)[::-1]: 
        total += int(dig) * int(pow(2,i))
        i = i + 1
    return total

# binary to oct
def bin_to_oct(num):
    total = ""
    subtotal = 0
    numstr = str(num)
    while(numstr):
        # foreach digit of the nibble (3 binary digits) translate into single oct digit
        # start from least sig digit
        subtotal = 0
        # pad front of numbers with 0's to fill to 4 bits
        if len(numstr) < 3:
            numstr = "0"*(3-len(numstr))+numstr
        for i in range(1,4):
            dig = numstr[-i]
            subtotal += int(dig) * int(pow(2,i-1))
        total = str(subtotal) + total
        # slice off last 3 bits and loop again
        numstr = numstr[:-3]    
    return total

# binary to hexidecimal
def bin_to_hex(num):
    total = ""
    subtotal = 0
    numstr = str(num)
    while(numstr):
        # foreach digit of the nibble (4 binary digits) translate into single hex digit
        # start from least sig digit
        subtotal = 0
        # pad front of numbers with 0's to fill to 4 bits
        if len(numstr) < 4:
            numstr = "0"*(4-len(numstr))+numstr
        for i in range(1,5):
            dig = numstr[-i]
            subtotal += int(dig) * int(pow(2,i-1))
        if (subtotal < 10):
            total = str(subtotal) + total
        else:
            # 65 - 9 = 
            total = chr(subtotal-10+65) + total
        # slice off last 4 bits and loop again
        numstr = numstr[:-4]    
    return total


# subtract two numbers by adding first with second nums 10s complement
def subtract_comp(minuend, subtrahend):
    # step 1: 10s complement the subtrahend
    sub_comp = nums_comp_dec(subtrahend)
    # step 2: add the minuend and the 10s comp of the subtrahend
    sumd_min = str(minuend + int(sub_comp))
    # step 3 
    if(minuend > subtrahend):
        # if min larger discard end carry which is first digit
        sumd_min = sumd_min[1:]
    else:
        # else answer is negative of the 10s comp of result 
        sumd_min = "-" + nums_comp_dec(int(sumd_min))
    return sumd_min

# return the number of digits of the passed in num or hell, even a string
def count_digits(num):
    #count = 0
    #for dig in str(num):
    #    count+=1
    #return count
    return str(num).__len__()

def nums_comp_dec(num):
    comp = ""
    nonzero_reached = 0
    # [::-1] reverse via slice
    for dig in str(num)[::-1]:
        if dig == "0":
            comp = comp + dig
        else:
            if nonzero_reached > 0:
                comp = comp + str(9 - int(dig))
            else:
                comp = comp + str(10 - int(dig))
                nonzero_reached = 1
    # return the reversed complement
    return comp[::-1]

