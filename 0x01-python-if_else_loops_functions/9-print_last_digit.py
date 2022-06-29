#!/usr/bin/python3
def print_last_digit(number):
    num_str = f"{number}"
    last = (int)(f"{num_str[-1:]}")
    if last in range(0, 10):
        print(last, end="")
        return last
