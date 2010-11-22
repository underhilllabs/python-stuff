#!/usr/bin/python

num_primes = 0
found_primes = []
x = 3

def test_prime(num):
    if num == 3 or num == 5:
        return True;
    else:
        for i in range(3,num/2,2):
            if not num%i:
                return False;
        return True

# 2 is first prime so start count at 2nd prime, and append 2 to found primes list
num_primes = 2
found_primes.append(2)

while num_primes <= 1000:
    if test_prime(x):
        found_primes.append(x)
        print "Found another: ", x, "! Its number %d" % len(found_primes)
        num_primes += 1
    # all primes are odd after 2, so start odd and step by 2 to test only odd numbers
    x += 2


        
