from sympy import *
import numpy as np
import matplotlib.pyplot as plt


x,y,omega=symbols('x y omega')

fx=sqrt(39**2-x**2)-36

res=fx.subs(x,14)
print(res.evalf())
grey=res*50/3
print(grey.evalf())

# raddd=np.arcsin(12/13)
# print(np.rad2deg(raddd))




number=6
for i in range(number):
    dx=(30/2)/number

    x_i=-15+i*dx
    res=fx.subs(x,x_i)

    grey=int(127-res*((127-50)/3))

    print("第(%d和%d)个layer的greyvlue为："%(i+1,100-i)+str(grey))


print(fx.subs(x,-8).evalf())
n=-4
left1=fx.subs(x,n).evalf()
right1=fx.subs(x,n+1).evalf()
print(right1-left1)