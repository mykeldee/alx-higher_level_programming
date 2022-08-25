#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as h
    for i in dir(h):
        if not(i.startswith('__')):
            print(i)
