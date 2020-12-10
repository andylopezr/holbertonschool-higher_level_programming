#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ac = len(argv) - 1
    total = 0
    if ac == 0:
        print("{:d}".format(ac))
    elif ac == 1:
        print("{:d}".format(argv[ac]))
    else:
        for i in range(1, ac + 1):
            total = total + int(argv[i])
        print("{:d}".format(total))
