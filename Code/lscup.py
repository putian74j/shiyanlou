#!/usr/bin/env python3
name = "//proc//cpuinfo"
with open(name) as fobj:
    for line in fobj:
        print(line,end = "")
