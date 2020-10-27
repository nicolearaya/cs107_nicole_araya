import numpy as np
import matplotlib.pyplot as plt


xValues = []
yValues = []

hValues = [1*10**-1, 1*10**-7, 1*10**-15]

#1*10**-15
#this was taking too long to calculate, so I wasn't able to include it in my chart

def f(x):
    return np.log(x)

def numerical_diff(f,h):
    def calcDiff(x):
        #calculate differential function
        innerInput = x+h
        function = (f(innerInput) - f(x))/h
        return function
    return calcDiff

closure = numerical_diff(f, hValues[1])
print(closure(0.2))
print(closure(0.4))

for i in hValues:
    a = 0.2
    index = hValues.index(i)
    print(index)
    xlist = []
    ylist = []
    closure = numerical_diff(f, i)
    while a <= 0.4:
        ylist.append(closure(a))
        xlist.append(a)
        a += i
    xValues.append(xlist)
    yValues.append(ylist)


exact_deriv = 1/np.array(xValues[1])

pl1 = plt.plot(xValues[0], yValues[0], 'g', label='h=1*10**-1')
pl2 = plt.plot(xValues[1], yValues[1], 'r', label = 'h=1*10**-7')
pl3 = plt.plot(xValues[2], yValues[2], 'y--', label = 'h=1*10**-15')
pl4 = plt.plot(xValues[1], exact_deriv, 'b:', label = 'Exact Derivative')
plt.legend()

plt.xlabel('X Value')
plt.ylabel('Finite Difference Approximation')
plt.show()




