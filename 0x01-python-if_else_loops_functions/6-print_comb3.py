#!/usr/bin/python3
for i in range(90):
    if (i % 10 > i / 10):
        if (i < 89):
            print("{:02}, ".format(i), end='')
        else:
            print("{:02}".format(i))
