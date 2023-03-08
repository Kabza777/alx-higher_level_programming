#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
    if chr(i) not in ['e', 'q']:
        print(chr(i), end='')
