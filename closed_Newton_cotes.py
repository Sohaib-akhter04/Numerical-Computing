import scipy.misc as sy
from sympy import var
from sympy import sympify
import numexpr as ne
import math
import numpy as np
import scipy as sp
import sympy as smp
from scipy.integrate import quad, cumulative_trapezoid
import ast
from numpy import cos, sin, tan, exp
from math import cos, sin, tan, pi, exp, log
def absolute(x0,xn,eq):
    x = smp.symbols('x')
    y =str(smp.integrate(eq,x))
    x = xn
    f1 = eval(y)
    x = x0
    f0 = eval(y)
    absol = f1-f0
    return absol




def func(y, e):
    x = var('x')
    res = e.subs(x, y)
    return res

def func_simplify(user_input):
    expr = sympify(user_input)
    return expr 

def func_input():
    user_input = input("Enter Function: ")
    return user_input


def func_eval(x):
    return ne.evaluate(exp)
    
def simpson(f, expr):
    a = input('Enter "a": ')
    a=float(eval(a))
    b = input('Enter "b": ')
    b=float(eval(b))
    h = (b - a) / 2
    x_mid = a + h
    ans = (h / 3) * (func(a, expr) + (4 * func(x_mid, expr)) + func(b, expr))
    print('\nIntegral is: %0.9f' % ans)
    a_der = sy.derivative(func_eval, a, dx=0.001, n=4, order=5)
    b_der = sy.derivative(func_eval, b, dx=0.001, n=4, order=5)
    error = ((h**5) / 90) * max(a_der, b_der)

    print('\nBound Error is: %0.9f' % error)
    real_value=absolute(a,b,expr)
    actual_error=abs(real_value-ans)
    print('actual error is->%0.9f' %actual_error)


def trapezoidal(f, expr):
    a=input('Enter "a":')
    a=float(eval(a))
    b = input('Enter "b": ')
    b=float(eval(b))
    h = b - a

    ans = (h / 2) * (func(a, expr) + func(b, expr))

    print('\nIntegral is: %0.9f' % ans)

    a_der = sy.derivative(func_eval, a, dx=0.001, n=2, order=3)
    b_der = sy.derivative(func_eval, b, dx=0.001, n=2, order=3)
    error = ((h**3) / 12) * max(a_der, b_der)

    print('\nBound Error is: %0.9f' % error)
    real_value=absolute(a,b,expr)
    actual_error=abs(real_value-ans)
    print('actual error is->%0.9f' %actual_error)
    return


def simpsons_three_eights(f, expr):
    a = input('Enter "a": ')
    a=float(eval(a))
    b = input('Enter "b": ')
    b=float(eval(b))
    h = (b - a) / 3
    x1 = a + h
    x2=a+2*h
    ans = (3*h / 8) * (func(a, expr) + (3 * func(x1, expr)) +(3*func(x2,expr)) + func(b, expr))
    print('\nIntegral is: %0.9f' % ans)
    a_der = sy.derivative(func_eval, a, dx=0.001, n=4, order=7)
    b_der = sy.derivative(func_eval, b, dx=0.001, n=4, order=7)
    error = (3*(h**5) / 80) * max(a_der, b_der)

    print('\nBound Error is: %0.9f' % error)
    real_value=absolute(a,b,expr)
    actual_error=abs(real_value-ans)
    print('actual error is->%0.9f' %actual_error)
    


def n_4(f, expr):
    a = input('Enter "a": ')
    a=float(eval(a))
    b = input('Enter "b": ')
    b=float(eval(b))
    h = (b - a) / 4
    x1 = a + h
    x2 = a + 2*h
    x3 = a + 3*h
    ans = (2*h / 45) * ( (7*func(a, expr)) + (32 * func(x1, expr)) + (12*func(x2,expr)) +(32*func(x3,expr)) + (7*func(b, expr)))
    print('\nIntegral is: %0.9f' % ans)
    a_der = sy.derivative(func_eval, a, dx=0.001, n=6, order=7)
    b_der = sy.derivative(func_eval, b, dx=0.001, n=6, order=7)
    error = abs((8*(h**7) / 945) * max(a_der, b_der))

    print('\nBound Error is: %0.9f' % error)
    real_value=absolute(a,b,expr)
    actual_error=abs(real_value-ans)
    print('actual error is->%0.9f' %actual_error)



print("1- Trapezoidal\n2- simpson\n3-Simpson's Three-Eights rule\n4-n=4")

ch = int(input("Enter Choice: "))
if(ch == 2):
    exp = func_input()
    expr = func_simplify(exp)
    simpson(func, expr)
      

elif(ch == 1):
    exp = func_input()
    expr = func_simplify(exp)
    trapezoidal(func, expr)

elif(ch == 3):
    exp = func_input()
    expr = func_simplify(exp)
    simpsons_three_eights(func, expr)
elif(ch == 4):
    exp = func_input()
    expr = func_simplify(exp)
    n_4(func, expr)