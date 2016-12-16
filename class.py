import math

__author__ = "K. Sravanthi"


class math():
    def fib(self):
        n = int(raw_input("Enter the value of n: "))
        a, b = 0, 1
        while n > 0:
            a, b = b, a + b
            n -= 1
            print a
        return a
    def sum_of_n(self):
        n = int(raw_input("Upto which digit do you want to find the sum? "))
        n = n*(n+1)/2
        print n
        return n

print ("this is for git stash")
obj1 = math()
obj1.fib()
obj1.sum_of_n()
