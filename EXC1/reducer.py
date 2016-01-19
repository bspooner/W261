#!/usr/bin/python
import sys
sums = 0
for line in sys.stdin:
    sums = sums + int(line)
print sums