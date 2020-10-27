# from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



# x,y,A,omega,phi0,y0=symbols('x y A omega phi0 y0')


def func(x,A,omega,phi0,y0):
    return A*np.cos(omega*x+phi0)+y0


x = [-1.77,-1.92,0.34,1.41,2.14,]
x = np.array(x)
num = [10.16,9.031,11.03,10.74,10.23,]
y = np.array(num)

popt, pcov = curve_fit(func, x, y)
print(popt)
A = popt[0]
omega = popt[1]
phi0 = popt[2]
y0=popt[3]


yvals = func(x,A,omega,phi0,y0) #拟合y值
print('popt:', popt)
print('系数A:', A)
print('系数omega:', omega)
print('系数phi0:', phi0)
print('系数y0:', y0)

print('系数pcov:', pcov)
print('系数yvals:', yvals)


plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('curve_fit')
plt.show()
