#!/usr/bin/python3
def uppercase(string):
    uppercase_str = ""
    for char in string:
        # convert lowercase character to uppercase
        if ord(char) >= 97 and ord(char) <= 122:
            uppercase_str += chr(ord(char) - 32)
        else:
            uppercase_str += char
    print("{}\n".format(uppercase_str))
