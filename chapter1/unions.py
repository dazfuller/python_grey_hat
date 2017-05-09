""" A simple demo showing how to use C unions in Python
    with ctypes
"""

#pylint: disable=C0325,R0903

from ctypes import (Union, c_long, c_int, c_char)

class BarleyAmount(Union):
    """ Defines a Union type with Python
    """
    _fields_ = [
        ('barley_long', c_long),
        ('barley_int', c_int),
        ('barley_char', c_char * 8)
    ]

def union_demo():
    """ Demo's how you can use C unions in Python
    """
    value = raw_input("Enter the amount of barley to put in the beer vat: ")
    my_barley = BarleyAmount(int(value))
    print('Barley amount as int: {}'.format(my_barley.barley_int))
    print('Barley amount as long: {}'.format(my_barley.barley_long))
    print('Barley amount as char: {}'.format(my_barley.barley_char))

if __name__ == '__main__':
    union_demo()
