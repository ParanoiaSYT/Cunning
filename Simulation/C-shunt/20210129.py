# from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import math


# E_J,phi_m,a,fb=symbols('E_J phi_m a fb')

# 原式：
# U=E_J*(-2*cos(phi_m)+a*cos(2*pi*fb+2*phi_m))

plt.figure()

E_J=1
a=0.4


fb=0
phi_m=np.linspace(-0.5,0.5,101)*np.pi
# fb=np.linspace(-0.5,0.5,101)

U=E_J*(-2*np.cos(phi_m)+a*np.cos(2*np.pi*fb+2*phi_m))

plt.plot(phi_m,U)
plt.show()


