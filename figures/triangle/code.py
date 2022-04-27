__all__ = ['triangle_perimeter', 'triangle_area']

import math


def triangle_perimeter(a=7, b=2, c=8):
    print(a + b + c)


def triangle_area(a=7, b=2, c=8):
    p = (a + b + c) / 2
    print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
