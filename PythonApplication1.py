import sys
import numpy as np
import numexpr as ne
import array as arr
import sympy as sp
from sympy import *
from tabulate import tabulate

def enter():
    expr = input("Enter expression in x: ")
    print("Interval for Bisection and Regula Falsi Methods:")
    a = input("Enter a: ")
    b = input("Enter b: ")
    print("Initial value for Newton's Raphson Method:")
    x0 = input("Enter X0: ")
    print("Initial values for Secant Method:")
    p0 = input("Enter P0: ")
    p1 = input("Enter P1: ")
    n = input("Enter max iterations: ")
    ep = input("Enter epsilon value: ")
    d = input("Enter decimal places for rounding values: ")

    x0 = float(x0)
    p0 = float(p0)
    p1 = float(p1)
    n = int(n)
    a = float(a)
    b = float(b)
    d = int(d)

    while(true):
        x = a
        foa = ne.evaluate(expr)
        x = b
        fob = ne.evaluate(expr)
        if(foa*fob < 0):
            bisection(expr, ep, n, a, b, d)
            regula_falsi(expr, ep, n, a, b, d)
            break
        else:
            print("Invalid interval! Input new interval.")
            a = input("Enter a: ")
            b = input("Enter b: ")
            a = float(a)
            b = float(b)

    newtons(expr, ep, n, x0, d)
    secant(expr, ep, n, p0, p1, d)
        

def bisection(exp, ep, n, a, b, d):
    i_arr = arr.array('i', [0]*n)
    a_arr = arr.array('d', [0]*n)
    b_arr = arr.array('d', [0]*n)
    c_arr = arr.array('d', [0]*n)
    foc_arr = arr.array('d', [0]*n)
    abs_err = arr.array('d', [0]*n)
    rel_err = arr.array('d', [0]*n)
    x = 0
    i = 1
    while(i < n):
        i_arr[i] = i
        a_arr[i] = a
        b_arr[i] = b
        
        c_arr[i] = (a+b)/2              #Bisection formula

        abs_err[i] = abs(x-c_arr[i])    #absolute error
        if(x == 0):
            rel_err[i] = 0
        else:
            rel_err[i] = abs_err[i]/x    #relative error

        if(abs_err[i] < float(ep)):      #breaking condition
            x = c_arr[i]
            foc_arr[i] = ne.evaluate(exp)
            break
        x = c_arr[i]
        foc_arr[i] = ne.evaluate(exp)           #f(c)

        if(foc_arr[i] < 0):
            b = c_arr[i]
        else:
            a = c_arr[i]
        i+=1

    n = 0
    m = 0
    data = np.empty([i, 7], dtype=float)
    for n in range(i):
        for m in range(7):
            data[n][0] = i_arr[n+1]
            data[n][1] = a_arr[n+1]
            data[n][2] = b_arr[n+1]
            data[n][3] = c_arr[n+1]
            data[n][4] = foc_arr[n+1]
            data[n][5] = abs_err[n+1]
            data[n][6] = rel_err[n+1]

    print("\nBisection Method Answer: " , round(c_arr[i], d), "\nTotal iterations: ", i)
    col_names = ["N", "a", "b", "c", "f(c)", "Absolute error", "Relative error"]
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid", floatfmt=(".0f",".10f",".10f",".10f",".10f",".10f",".10f")))


def regula_falsi(exp, ep, n, a, b, d):
    i_arr = arr.array('i', [0]*n)
    a_arr = arr.array('d', [0]*n)
    b_arr = arr.array('d', [0]*n)
    c_arr = arr.array('d', [0]*n)
    foc_arr = arr.array('d', [0]*n)
    abs_err = arr.array('d', [0]*n)
    rel_err = arr.array('d', [0]*n)
    c0 = 0
    i = 1
    while(i < n):
        i_arr[i] = i
        a_arr[i] = a
        b_arr[i] = b

        x = a
        foa = ne.evaluate(exp)                      #f(a)                   
        x = b
        fob = ne.evaluate(exp)                      #f(b)

        if((fob-foa) == 0):
            sys.exit("f(b)-f(a) becomes 0, no solution available!")

        c_arr[i] = ((a*fob)-(b*foa))/(fob-foa)      #Regula-Falsi formula

        abs_err[i] = abs(c0-c_arr[i])               #absolute error
        if(x == 0):
            rel_err[i] = 0
        else:
            rel_err[i] = abs_err[i]/x               #relative error

        if(abs_err[i] < float(ep)):                 #breaking condition
            x = c_arr[i]
            foc_arr[i] = ne.evaluate(exp)
            break
        x = c_arr[i]
        c0 = c_arr[i]
        foc_arr[i] = ne.evaluate(exp)
        if(foc_arr[i] < 0):
            b = c_arr[i]
        else:
            a = c_arr[i]
        i+=1

    n = 0
    m = 0
    data = np.empty([i, 7], dtype=float)
    for n in range(i):
        for m in range(7):
            data[n][0] = i_arr[n+1]
            data[n][1] = a_arr[n+1]
            data[n][2] = b_arr[n+1]
            data[n][3] = c_arr[n+1]
            data[n][4] = foc_arr[n+1]
            data[n][5] = abs_err[n+1]
            data[n][6] = rel_err[n+1]

    print("\nRegula Falsi Method Answer: " , round(c_arr[i], d), "\nTotal iterations: ", i)
    col_names = ["N", "a", "b", "c", "f(c)", "Absolute error", "Relative error"]
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid", floatfmt=(".0f",".10f",".10f",".10f",".10f",".10f",".10f")))
    

def newtons(exp, ep, n, p0, d):
    i_arr = arr.array('i', [0]*n)
    p = arr.array('d', [0]*n)
    abs_err = arr.array('d', [0]*n)
    rel_err = arr.array('d', [0]*n)
    x = symbols('x')
    d_exp = Derivative(exp, x)             #derivative of f(x)
    d_exp = str(d_exp.doit())              #returned and cast as string

    p[0] = p0
    i = 1
    while(i < n):
        i_arr[i] = i
        x = p0
        fop0 = ne.evaluate(exp)                   #f(x0) or f(p0)
        fodp0 = ne.evaluate(d_exp)                #f'(x0) or f'(p0)

        if(fodp0 == 0):
            sys.exit("Derivative of f(x) becomes 0, no solution available!")

        p[i] = p0 - (fop0/fodp0)           #Newtons's formula

        abs_err[i] = abs(p[i] - p0)
        if(p[i] == 0):
            rel_err[i] = 0
        else:
            rel_err[i] = abs_err[i]/p[i]

        if(abs_err[i] < float(ep)):        #breaking condition
            break
        p0 = p[i]
        i+=1

    n = 0
    m = 0
    data = np.empty([i, 4], dtype=float)
    for n in range(i):
        for m in range(4):
            data[n][0] = i_arr[n+1]
            data[n][1] = p[n+1]
            data[n][2] = abs_err[n+1]
            data[n][3] = rel_err[n+1]

    print("\nNewton's Raphson Method Answer: " , round(p[i], d), "\nTotal iterations: ", i)
    col_names = ["N", "Xn", "Absolute error", "Relative error"]
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid", floatfmt=(".0f",".10f",".10f",".10f",".10f",".10f",".10f")))


def secant(exp, ep, n, p0, p1, d):
    i_arr = arr.array('i', [0]*n)
    p = arr.array('d', [0]*n)
    abs_err = arr.array('d', [0]*n)
    rel_err = arr.array('d', [0]*n)

    p[0] = p0
    p[1] = p1

    abs_err[1] = abs(p1-p0)
    if(p0 == 0):
        rel_err[1] = 0
    else:
        rel_err[1] = abs_err[1]/p0

    i = 1
    while(i < n):
        i_arr[i] = i
        x = p0
        fop0 = ne.evaluate(exp)                            #f(p0)
        x = p1
        fop1 = ne.evaluate(exp)                            #f(p1)

        p[i+1] = p1 - ((fop1*(p1-p0))/(fop1 - fop0))         #secant formula
        
        abs_err[i+1] = abs(p[i+1]-p1)
        if(p1 == 0):
            rel_err[i+1] = 0
        else:
            rel_err[i+1] = abs_err[i+1]/p1

        if(abs_err[i+1] < float(ep)):
            i_arr[i+1] = i+1
            break

        p0 = p1
        p1 = p[i+1]
        i+=1

    n = 0
    m = 0
    data = np.empty([i+1, 4], dtype=float)
    for n in range(i+1):
        for m in range(4):
            data[n][0] = i_arr[n+1]
            data[n][1] = p[n+1]
            data[n][2] = abs_err[n+1]
            data[n][3] = rel_err[n+1]

    print("\nSecant Method Answer: " , round(p[i], d), "\nTotal iterations: ", i+1)
    col_names = ["N", "Xn", "Absolute error", "Relative error"]
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid", floatfmt=(".0f",".10f",".10f",".10f",".10f",".10f",".10f")))

enter()
