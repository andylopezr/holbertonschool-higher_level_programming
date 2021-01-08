#!/usr/bin/python3
"""
Module containing a function that separates sentences
"""


def text_indentation(text):
    """splits a text followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    switch = 0
    for i in text:
        if switch == 0:
            if i == ' ':
                continue
            else:
                switch = 1
        if switch == 1:
            if i == '?' or i == '.' or i == ':':
                print(i)
                print()
                switch = 0
            else:
                print(i, end="")
