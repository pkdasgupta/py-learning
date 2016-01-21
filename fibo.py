#!/usr/bin/env python

# ---------------------------------------------------------------------------------
# Program to Print Fibonacci series upto a said number of Terms from User Input
# ---------------------------------------------------------------------------------

print "\n ***************** Fibonacci Series ******************"

terms = input("\n Please enter the number of Terms : ")

print "\n Fibonacci Series upto %s-terms is : " %terms,

def fibo(num):
    if (num == 0 or num == 1):
        return num
    else:
        return fibo(num-1) + fibo(num-2)

for num in range(0,terms):
    print fibo(num),


print "\n\n ***************** !! Thank You !! ****************** \n"
