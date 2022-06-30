#!/usr/bin/python3
if __name__ == "__main__":
    for name in dir("hidden_4"):
        if "__" in name:
            continue
        print(f"{name}")
