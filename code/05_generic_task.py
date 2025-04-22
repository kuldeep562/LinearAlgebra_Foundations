
# Q-10 Apply Newton Raphson’s method to solve the algebraic equation f(x): x3 -5x +1 =0


import math
from sympy import *
x=Symbol('x')
def f(x):
    a=x*x*x -9*x + 1
    return(a)
f=x*x*x -9*x +1
print(f.diff(x))

