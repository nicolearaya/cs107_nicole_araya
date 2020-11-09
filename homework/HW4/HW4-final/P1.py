import numpy as np
import matplotlib.pyplot as plt


xValues = []
yValues = []

hValues = [1*10**-1, 1*10**-7]

#1*10**-15
#this was taking too long to calculate, and eventually kept automatically killing the process so I wasn't able to include it in my chart

def f(x):
    return np.log(x)

def numerical_diff(f,h):
    def calcDiff(x):
        #calculate differential function
        innerInput = x+h
        function = (f(innerInput) - f(x))/h
        return function
    return calcDiff

for i in hValues:
    a = 0.2
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
#pl3 = plt.plot(xValues[2], yValues[2], 'y--', label = 'h=1*10**-15')
pl4 = plt.plot(xValues[1], exact_deriv, 'b:', label = 'Exact Derivative')
plt.legend()

print("Answer to Q-a: the value of h that was closest to the true derivative was 1*10**-7. When h is too small, the approximation takes too long compute. When h is too large, the linear approximation is not accurate.")
print("Answer to Q-b: Automatic differentiation addresses the problems of heavy computation and inaccuracy, by breaking functions down into small elementary functions that are easy to compute yet still yield machine precision answers.")

plt.xlabel('X Value')
plt.ylabel('Finite Difference Approximation')
plt.show()




