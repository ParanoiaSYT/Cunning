from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import math


# x=symbols('x')
# y=symbols('y')
E_J,phi_m,a,fb=symbols('E_J phi_m a fb')

# 原式：
# U=E_J*(-2*cos(phi_m)+a*cos(2*pi*fb+2*phi_m))
# 当fb为0时：
U=E_J*(-2*cos(phi_m)+a*cos(2*phi_m))

U1=diff(U,phi_m)
print(U1)
# E_J*(-2*a*sin(2*phi_m) + 2*sin(phi_m))

print(solve(U1, phi_m))
# [0, pi, -I*log(-(sqrt(1 - 4*a**2) - 1)/(2*a)), -I*log((sqrt(1 - 4*a**2) + 1)/(2*a))]

U2=diff(U1,phi_m)/2
print(U2)       # E_J*(-4*a*cos(2*phi_m) + 2*cos(phi_m))/2

def diffen(fx,x,n):
    for i in range(n):
        fx=diff(fx,x)
    return fx/factorial(n)

res0=diffen(U,phi_m,0)
print(res0.subs(phi_m,0))   # E_J*(a - 2)


res4=diffen(U,phi_m,4)
res4_0=res4.subs(phi_m,0)
print(simplify(res4_0))         # E_J*(8*a - 1)/12

res6=diffen(U,phi_m,6)
res6_0=res6.subs(phi_m,0)
print(simplify(res6_0))         # E_J*(1 - 32*a)/360



#######################
# U=E_J*(-2*cos(phi_m)+a*cos(2*pi*fb+2*phi_m))