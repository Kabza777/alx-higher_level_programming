#!/usr/bin/python3
for i in range(1, 10):
    for j in range(i+1, 10):
        print("{:d}{:d}".format(i, j), end=(", "
              if i < 9
              or j < 9
              else "\n"))
