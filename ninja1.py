# Number of Digits


from os import *
from sys import *
from collections import *
from math import *

def countDigit(n: int) -> int:
   spt = [int(i) for i in str(n)]
   nofd = len(spt)
   return nofd

print(countDigit(1234))