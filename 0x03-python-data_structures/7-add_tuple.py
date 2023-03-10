#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # If the tuple is smaller than 2, use 0 for the missing integers
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))

    # Take only the first 2 integers of the tuples
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]

    # Calculate the sum of the integers and return a tuple
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
