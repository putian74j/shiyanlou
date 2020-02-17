#!/usr/bin/env python3
i = 1
print("-"*50)
while i < 11:
    n = 1
    while n < 11:
        print("{:5d}".format(n*i),end = " ")
        n = n + 1
    i = i + 1
    print()
print("_"*50)
