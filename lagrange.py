from sympy import *
import math
print("--------Lagrange(M1)---------")
noofvalues = int(input("How many values of x and y you would enter: "))
xlist = []
ylist = []

for i in range(int(noofvalues)):
    a = float(input("Enter x" + str(i) + " :"))
    b = float(input("Enter y" + str(i) + " :"))
    xlist.append(float(a))
    ylist.append(float(b))

answer = 0
x = symbols('x')
for i in range(noofvalues):
    temp = ylist[i]
    temp2 = 1
    for j in range(noofvalues):
        if j==i:
            continue
        else:
            temp *= (x-xlist[j])
            temp2 *= (xlist[i] - xlist[j])

    answer += (temp/temp2)




print("-------The values of x are-------")
print(xlist)

print("-------The values of y are-------")
print(ylist)

unknowny = float(input("Enter the value of x to find y for: "))
print("The simplified lagrange equation is: ")
anwer = answer.simplify()
answer = answer.expand()
pprint(answer)
print("The answer of y is: "+str(round(answer.subs(x,unknowny),7)))