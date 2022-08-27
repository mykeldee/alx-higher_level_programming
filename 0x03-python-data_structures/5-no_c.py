#!/usr/bin/python3
def no_c(my_string):
    a = "cC"
    b = "  "
    c = "cC"
    translation = my_string.maketrans(a, b, c)
    return my_string.translate(translation)
