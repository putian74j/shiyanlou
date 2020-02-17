#!/usr/bin/env python3
num = int(input("Please input Camera numer: "))
price = float(input("Please input Camera price: "))

salary = 1500 + num * price * 0.02 + 200 * num

print("salary is {:6.2f}".format(salary))
