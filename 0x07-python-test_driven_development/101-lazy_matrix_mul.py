#!/usr/bin/python3
""" Multiplies two matrices using numpy """

import numpy


def lazy_matrix_mul(m_a, m_b):
    """ returns the multiplication result """
    return numpy.matmul(m_a, m_b)
