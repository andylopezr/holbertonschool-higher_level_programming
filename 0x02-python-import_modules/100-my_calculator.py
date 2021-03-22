#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    length = len(argv) - 1
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    ops = "+", "-", "*", "/"
    if op in ops:
        if op == ops[0]:
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif op == ops[1]:
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif op == ops[2]:
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif op == ops[3]:
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
