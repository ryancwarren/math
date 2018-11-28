#!/usr/bin/python
import sys

def sqrt(a,a1):
  try:
    x1=a1*a1
    b1=a/a1
    x2=b1*b1

    print "a: ", a, "a1: ", a1, "b1: ", b1

    if (x1 == a): return x1
    elif (x2 == a): return x2
    else: 
      return sqrt(a, 1.0/2.0*(a1+b1))
  except RuntimeError as re:
    return a1 

print sqrt(float(sys.argv[1]),float(sys.argv[1])/2)
