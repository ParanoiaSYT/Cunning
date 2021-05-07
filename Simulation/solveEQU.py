# from sympy import *
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt




# x,y,A,omega,phi0,y0=symbols('x y A omega phi0 y0')


def func(x,A,B):
    return A*np.sqrt(1-B*x**2)


x = [-15,0,15,0]
x = np.array(x)
num = [0,3,0,-3]
y = np.array(num)

popt, pcov = curve_fit(func, x, y)
print(popt)
A = popt[0]
B = popt[1]
# B = popt[2]
# y0=popt[3]


yvals = func(x,A,B) #拟合y值
print('popt:', popt)
print('系数A:', A)
# print('系数omega:', omega)
# print('系数phi0:', phi0)
# print('系数y0:', y0)

print('系数pcov:', pcov)
print('系数yvals:', yvals)


plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('curve_fit')
plt.show()
