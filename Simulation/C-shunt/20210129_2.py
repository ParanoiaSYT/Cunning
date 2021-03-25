import numpy as np
import matplotlib.pyplot as plt


plt.figure(1)
fb=np.linspace(-1,0,101)
a=0.4
E_J=85e9
E_cm=0.35e9
EJm=(2-4*a*np.cos(2*np.pi*fb))*E_J
for m in range(3):
# m=0
    Em=np.sqrt(E_cm*EJm)*(m+0.5)+(8*a*np.cos(2*np.pi*fb)-1)*E_cm*(6*m**2+6*m+3)/(96*(1-2*a*np.cos(2*np.pi*fb)))+a*E_J*(1+np.cos(2*np.pi*fb))
    # E1=Em.subs(m,0)

    plt.plot(fb,Em)
H0=E_J*(a+a*(np.cos(2*np.pi*fb)))
plt.plot(fb,H0)
plt.show()