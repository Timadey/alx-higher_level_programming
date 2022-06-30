#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    from sys import argv, exit
    argc = len(argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = f"{argv[2]}"
    if operator != "+" and operator != "-" and operator != "*" and operator != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = (int)(argv[1])
    b = (int)(argv[3])
    if operator == "+":
        res = calc.add(a, b)
    elif operator == "-":
        res = calc.sub(a, b)
    elif operator == "*":
        res = calc.mul(a, b)
    elif operator == "/":
        res = cal.div(a, b)
    print(f"{a:d} {argv[2]} {b:d} = {res}")
