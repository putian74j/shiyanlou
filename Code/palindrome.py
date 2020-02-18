#!/usr/bin/env python3
s = input("Please enter a string: ")
r = s[::-1]
if s == r:
    print("{} is a palindrome".format(s))
else:
    print("{} is not a palindrome".format(s))
