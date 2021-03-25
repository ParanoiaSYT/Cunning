from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import math

E_J,phi_m,a=symbols('E_J phi_m a')

fb=0
# U=E_J*(-2*cos(phi_m)+a*cos(2*pi*fb+2*phi_m))
U_diff=E_J*(-2*a*sin(2*pi*fb + 2*phi_m) + 2*sin(phi_m))


phi_m_star=solve(U_diff,phi_m)
print(phi_m_star)
