#!/usr/bin/env python3
x = 1
sum = 0
n = int(input("Please input a Number: "))
while (x <= n):
    sum += 1.0 / x
    print("x:{} sum:{:5.2f}".format(x,sum))
    x = x + 1
