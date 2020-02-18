#!/usr/bin/env python3
num = int(input("Please input student's number: "))
#print(num)
data = {}
i = 0
while i < num:
    name = input("Enter the name of the student " + str(i + 1) + ": ")
    mark_ph = int(input("Enter marks of physics:  "))
    mark_ma = int(input("Enter marks of maths: "))
    mark_hi = int(input("Enter marks of history: "))
    data.setdefault(name,[]).append(mark_ph)
    data.setdefault(name,[]).append(mark_ma)
    data.setdefault(name,[]).append(mark_hi)
    i += 1
    #print(data)

for a, b in data.items():
    print(a + "'s total marks " + str(sum(b)))
    if sum(b) >= 120:
        print(a + " passed :)")
    else:
        print(a + " failed :(")



