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
    
def n_0(f, expr):
    a = input('Enter "a": ')
    a=float(eval(a))
    b = input('Enter "b": ')
    b=float(eval(b))
    h = (b - a) / 2
    x0 = a + h
    ans = (2*h*func(x0, expr))
    print('\nIntegral is: %0.9f' % ans)
    a_der = sy.derivative(func_eval, a, dx=0.001, n=2, order=5)
    b_der = sy.derivative(func_eval, b, dx=0.001, n=2, order=5)
    error = ((h**3) / 3) * max(abs(a_der), abs(b_der))

    print('\nBound Error is: %0.9f' % error)
    real_value=absolute(a,b,expr)
    actual_error=abs(real_value-ans)
    print('actual error is->%0.9f' %actual_error)


def n_1(f, expr):
    a=input('Enter "a":')
    a=float(eval(a))
    b = input('Enter "b": ')
    b=float(eval(b))
    h = (b - a) / 3
    x0=a+h
    x1=a+2*h
    ans = (3*h / 2) * (func(x0, expr) + func(x1, expr))

    print('\nIntegral is: %0.9f' % ans)

    a_der = sy.derivative(func_eval, a, dx=0.001, n=2, order=3)
    b_der = sy.derivative(func_eval, b, dx=0.001, n=2, order=3)
    error = ((h**3) / 12) * max(abs(a_der), abs(b_der))

    print('\nBound Error is: %0.9f' % error)
    real_value=absolute(a,b,expr)
    actual_error=abs(real_value-ans)
    print('actual error is->%0.9f' %actual_error)
    return


def n_2(f, expr):
    a = input('Enter "a": ')
    a=float(eval(a))
    b = input('Enter "b": ')
    b=float(eval(b))
    h = (b - a) / 4
    x0 = a + h
    x1=a+2*h
    x2=a+3*h
    ans = (4*h / 3) * (2*func(x0, expr) - (func(x1, expr)) +(2*func(x2,expr)))
    print('\nIntegral is: %0.9f' % ans)
    a_der = sy.derivative(func_eval, a, dx=0.001, n=4, order=5)
    b_der = sy.derivative(func_eval, b, dx=0.001, n=4, order=5)
    error = (14*(h**5) / 45) * max(abs(a_der), abs(b_der))

    print('\nBound Error is: %0.9f' % error)
    real_value=absolute(a,b,expr)
    actual_error=abs(real_value-ans)
    print('actual error is->%0.9f' %actual_error)
    


def n_3(f, expr):
    a = input('Enter "a": ')
    a=float(eval(a))
    b = input('Enter "b": ')
    b=float(eval(b))
    h = (b - a) / 5
    x1 = a + 2*h
    x2 = a + 3*h
    x3 = a + 4*h
    x0 = a + h
    ans = (5*h / 24) * ( ((11*func(x0, expr)) + (func(x1, expr)) + (func(x2,expr)) +(11*func(x3,expr)) ))
    print('\nIntegral is: %0.9f' % ans)
    a_der = sy.derivative(func_eval, a, dx=0.001, n=6, order=7)
    b_der = sy.derivative(func_eval, b, dx=0.001, n=6, order=7)
    error = abs((95*(h**7) / 144) * max(abs(a_der), abs(b_der)))

    print('\nBound Error is: %0.9f' % error)
    real_value=absolute(a,b,expr)
    actual_error=abs(real_value-ans)
    print('actual error is->%0.9f' %actual_error)



print("0- n=0\n1- n=1\n2- n=2\n3- n=3")

ch = int(input("Enter Choice: "))
if(ch == 0):
    exp = func_input()
    expr = func_simplify(exp)
    n_0(func, expr)
      

elif(ch == 1):
    exp = func_input()
    expr = func_simplify(exp)
    n_1(func, expr)

elif(ch == 2):
    exp = func_input()
    expr = func_simplify(exp)
    n_2(func, expr)
elif(ch == 3):
    exp = func_input()
    expr = func_simplify(exp)
    n_3(func, expr)