#!/usr/bin/env python3
days = int(input("Please input days:"))
print("Months:{} Days:{}".format(*divmod(days,30)))
