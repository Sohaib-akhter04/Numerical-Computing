from sympy import *
import math
print("--------Newton divided difference(M2)---------")
noofvalues = int(input("How many values of x and y you would enter: "))
xlist = []
ylist = []
d = []
fd = []

for i in range(int(noofvalues)):
    a = int(input("Enter x" + str(i) + " :"))
    b = int(input("Enter y" + str(i) + " :"))
    xlist.append(int(a))
    ylist.append(int(b))

for k in range(int(noofvalues)-1):
    for j in range(int(noofvalues)-k-1):
        if k==0:
            d.append(((ylist[j+1]-ylist[j])/(xlist[j+1]-xlist[j])))
        else:

            d.append(((temp[j+1]-temp[j])/(xlist[j+k+1]-xlist[j])))
    fd.append(d)
    d = []
    temp = fd[k]



print("-------The values of x are-------")
print(xlist)

print("-------The values of y are-------")
print(ylist)

print("---The divided differnce table-----")
dd = 1
for num in fd:
    print('Difference '+str(dd)+': '+str(num))
    dd = dd+1


unknowny = int(input("Enter the value of x to find y for: "))
answer = ylist[0]
x = symbols('x')
for i in range(int(noofvalues)-1):
    temp = fd[i][0]
    for j in range(i+1):
        temp *= (x-xlist[j])

    answer+= temp

print("The simplified equation is: ")
answer = answer.simplify()
answer = answer.expand()
pprint(answer)
print("The value of y is: "+str(round(answer.subs(x,unknowny)),7))