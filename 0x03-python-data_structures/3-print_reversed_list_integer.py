#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):    
    n = my_list.reverse()
    x = len(my_list)
    if x > 0:
        for i in range(x):
            print("{:d}".format(my_list[i]))
