#!/usr/bin/env python3
name = input("Enter file name: ")
fobj = open(name)
print(fobj.read())
fobj.close()
