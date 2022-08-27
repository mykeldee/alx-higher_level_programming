#!/usr/bin/python
def no_c(my_string):
    if 'c' in my_string or 'C' in my_string:
        n = ""
        for i in range(len(my_string)):
            if my_string[i] == 'c' or my_string[i] == 'C':
                continue
            n += my_string[i]
        return n
