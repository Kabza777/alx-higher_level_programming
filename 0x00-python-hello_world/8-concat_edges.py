#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(" ".join(str.split()[5:9] + str.split()[-7:-4]).capitalize() + "\n")
