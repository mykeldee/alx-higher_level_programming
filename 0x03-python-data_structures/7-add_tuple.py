#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    c = abs(len(tuple_a) -len(tuple_b))
    if c != 0:
        x=tuple([0 for i in range(c)])
        if len(tuple_a) > len(tuple_b):
            tuple_b += x
        else:
            tuple_a += x
    return (tuple([sum(i) for i in zip(*(tuple_a,tuple_b))]))
