#!/usr/bin/env python3

import sys
from Stack import Stack

s = Stack()
#s.push('a')
#print(s.size())
#print(s.peek())

def balanced_parentheses(parentheses):
    for i in parentheses:
        if i == '(':
            s.push('(')
        elif i == ')':
            if s.is_empty():
                return False
            else:
                s.pop()
    return s.is_empty()

print(sys.argv[1])
print(balanced_parentheses(sys.argv[1]))

