from sympy import *
import math
print("Code to calculate the newton forward difference")
noofvalues = int(input("How many numbers of x and y you would enter: "))
xlist = []
ylist = []
d = []
fd = []

for i in range(int(noofvalues)):
    a = float(input("Enter x" + str(i) + " :"))
    b = float(input("Enter y" + str(i) + " :"))
    xlist.append(float(a))
    ylist.append(float(b))

for k in range(int(noofvalues)-1):
    for j in range(int(noofvalues)-k-1):
        if k==0:
            d.append(round(ylist[j+1]-ylist[j],9))
        else:
            d.append(round(temp[j+1]-temp[j],9))
    fd.append(d)
    d = []
    temp = fd[k]



print("-------The values of x are-------")
print(xlist)

print("-------The values of y are-------")
print(ylist)



print("---The difference table-----")
dd = 1
for num in fd:
    print('Difference '+str(dd)+': '+str(num))
    dd = dd+1

x = symbols('x')
unknowny = float(input("Enter the value of x to find y: "))
p = (x - xlist[0])/(xlist[1]-xlist[0])
answer = ylist[0]
t1 = 0
for i in range(1,int (noofvalues)):
    t1 = p
    if(i==1):
        answer+= fd[0][0]*p
    else:
        for j in range(1,i):
            t1*=(p-j)
        t1/= math.factorial(j+1)
        t1*= fd[i-1][0]
        answer += t1

print("The simplfied equation is: ")
answer = answer.simplify()
answer = answer.expand()
pprint(answer)
print("The value of y is: "+str(round(answer.subs(x,unknowny),7)))


