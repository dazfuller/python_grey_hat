""" Simple hello world script from Grey Hat Hacking
"""
from ctypes import cdll

def test_c_library():
    """ Executes a small piece of code which calls the print
        method on the libc library
    """
    libc = cdll.LoadLibrary('libc.dylib')
    msg_string = 'Hello world!\n'
    libc.printf('Testing: %s', msg_string)

if __name__ == '__main__':
    test_c_library()
