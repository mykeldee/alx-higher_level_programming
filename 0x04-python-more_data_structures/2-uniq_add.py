#!/usr/bin/python3
def uniq_add(my_list=[]):
    a_list = list(set(my_list))
    total=0
    for i in a_list:
        total += i
    return total
