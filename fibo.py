#!/usr/bin/env python

# ---------------------------------------------------------------------------------
# Program to Print Fibonacci series up to a said number of Terms from User Input
# ---------------------------------------------------------------------------------

print("\n ***************** Fibonacci Series ******************")

terms = int(input("\n Please enter the number of Terms : "))

print("\n Fibonacci Series up to %s-terms is : " % terms, end=" ")


def fibo(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibo(num - 1) + fibo(num - 2)


for n in range(0, terms):
    print(fibo(n), end=" ")

print("\n\n ***************** !! Thank You !! ****************** \n")
