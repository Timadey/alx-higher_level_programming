#!/usr/bin/python3
for x in range(0, 8):
    for y in range(0, 10):
        if x == y or x > y:
            continue
        print(f"{x:d}{y:d}", end=", ")
print(f"{89:d}")
