#!/usr/bin/python3
def max_integer(my_list=[]):
    # If the list is empty, return None
    if not my_list:
        return None

    # Initialize the max value as the first element of the list
    max_value = my_list[0]

    # Loop through the list and compare each element to the current max value
    for value in my_list:
        if value > max_value:
            max_value = value

    # Return the max value
    return max_value
