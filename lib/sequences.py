#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []
    while length > 0:

        if len(fib_list) == 0 :
            fib_list.append(0)
        elif len(fib_list) == 1:
            fib_list.append(1)
        else:
            x = fib_list[len(fib_list) - 1]
            y = fib_list[len(fib_list) - 2]
            fib_list.append(x + y)
        length -= 1

    print(fib_list)