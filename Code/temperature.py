#!/usr/bin/env python3
fahreheit=0
print("Fahreheit Celsius")
while fahreheit <= 250:
    celsius = (fahreheit - 32) / 1.8
    print("{:9d} {:7.2f}".format(fahreheit,celsius))
    fahreheit = fahreheit + 25

