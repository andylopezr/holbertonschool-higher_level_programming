#!/usr/bin/env python3
def no_c(my_string):
    new_string = [i for i in my_string if (i is not "c" and i is not "C")]
    return "".join(new_string)
