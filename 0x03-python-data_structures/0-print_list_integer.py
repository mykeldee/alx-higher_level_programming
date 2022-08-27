#!/usr/bin/python3
def print_list_integer(my_list=[]):
    n = len(my_list)
    if n > 1:
        for i in range(n):
            print(my_list[i])
