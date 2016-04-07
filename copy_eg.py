# import copy
from copy import *

a = [1, 2]
b = a
print b
c = copy(a)
print c
a[0] = 'hello, world!'
print a #['hello, world!', 2]
print b #['hello, world!', 2]
print c #[1, 2]