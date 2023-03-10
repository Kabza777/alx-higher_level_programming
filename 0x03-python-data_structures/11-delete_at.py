#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Create a new list without the element at the specified index
    new_list = my_list[:idx] + my_list[idx+1:]

    # Return the new list
    return new_list
