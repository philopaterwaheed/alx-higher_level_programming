#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list and idx is not None and element is not None and\
            idx >= 0 and idx < len(my_list):
        my_list = my_list[:]
        my_list[idx] = element
    return my_list
