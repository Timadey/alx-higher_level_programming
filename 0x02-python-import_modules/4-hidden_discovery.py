#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for name in (dir(hidden_4)):
        if "__" == name[:2]:
            continue
        print(f"{name}")
