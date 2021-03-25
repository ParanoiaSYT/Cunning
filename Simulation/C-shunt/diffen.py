from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import math


E_J,phi_m,a,fb,m,phi_m_star=symbols('E_J phi_m a fb,m,phi_m_star')

# 原式：
# fb=0.3
U=E_J*(-2*cos(phi_m)+a*(cos(2*pi*fb)*cos(2*phi_m)-sin(2*pi*fb)*sin(2*phi_m)))
# U=E_J*(-2*cos(phi_m)+a*cos(2*pi*fb+2*phi_m))
# 当fb为0时：
# U=E_J*(-2*cos(phi_m)+a*cos(2*phi_m))

# U_star=diff(U,phi_m)
# print(U_star)       # E_J*(a*(-2*sin(2*phi_m)*cos(2*pi*fb) - 2*sin(2*pi*fb)*cos(2*phi_m)) + 2*sin(phi_m))
# print(solveset(U_star,phi_m))





def diffen(fx,x,n):
    for i in range(n):
        fx=diff(fx,x)
    fx1=fx / factorial(n)
    return sympify(fx1.subs(phi_m,phi_m_star))


U0=diffen(U,phi_m,0)
print(U0)

U1=diffen(U,phi_m,1)
print(U1)

U2=diffen(U,phi_m,2)
print(U2)

U3=diffen(U,phi_m,3)
print(U3)

U4=diffen(U,phi_m,4)
print(U4)


