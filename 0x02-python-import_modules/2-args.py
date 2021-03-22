#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ac = len(argv) - 1
    if ac == 0:
        print("{:d} arguments.".format(ac))
    elif ac == 1:
        print("{:d} argument:".format(ac))
        print("{:d}: {}".format(ac, argv[1]))
    else:
        print("{:d} arguments:".format(ac))
        for i in range(1, ac + 1):
            print("{:d}: {}".format(i, argv[i]))
