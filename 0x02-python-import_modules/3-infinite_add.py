#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    sum = 0

    for n in range(1, argc):
        num = (int)(argv[n])
        sum += num
    print(sum)
