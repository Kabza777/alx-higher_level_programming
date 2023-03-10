#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create an empty list to store the results
    result = []

    # Loop through the list and check if each element is a multiple of 2
    for value in my_list:
        if value % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    # Return the result
    return result
