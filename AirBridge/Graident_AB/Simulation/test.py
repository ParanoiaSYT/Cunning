from sympy import *
import matplotlib.pyplot as plt
import numpy as np



x=symbols('x')


x=np.linspace(40,270,201)
thick = 16690.539477 - 1.66809672e+04 * x ** 1.02533818e-04
plt.figure(1)
plt.plot(x,thick)
plt.show()

