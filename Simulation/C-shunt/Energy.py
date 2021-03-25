import numpy as np
import matplotlib.pyplot as plt
import sympy as sy


a=0.4
Ej=85e9
Ecm=0.35e9


phi_m=sy.symbols('phi_m')
# U=E_J*(-2*cos(phi_m)+a*cos(2*pi*fb+2*phi_m))
# for fb in sy.linspace(0,0.5,1):

fb_list=[]
E01_list=[]
E12_list=[]
E02_list=[]
for fb in np.linspace(-0.5,0.5,1001):
    U_diff1=(-2*a*sy.sin(2*sy.pi*fb + 2*phi_m) + 2*sy.sin(phi_m))
    # nsolve数值解
    # 这里给定猜测值为0，求近于0处的phi_star
    phi_star = sy.nsolve(U_diff1, phi_m,0)
    # phi_star=phi_star_list[0]
    # print(fb,phi_star)
    fb_list.append(fb)

    U4=Ej*(-2*sy.cos(phi_star)+a*(16*sy.cos(2*sy.pi*fb)*sy.cos(2*phi_star)-16*sy.sin(2*sy.pi*fb)*sy.sin(2*phi_star)))/24
    Ejm=Ej*(2*sy.cos(phi_star)+a*(-4*sy.cos(2*sy.pi*fb)*sy.cos(2*phi_star)+4*sy.sin(2*sy.pi*fb)*sy.sin(2*phi_star)))

    E01=sy.sqrt(Ecm*Ejm)+U4*3*Ecm/Ejm
    E12=sy.sqrt(Ecm*Ejm)+U4*6*Ecm/Ejm
    E02=sy.sqrt(Ecm*Ejm)+U4*9*Ecm/Ejm


    # print(U4)
    # print(Ecm/Ejm)
    # print(U4*3*Ecm/Ejm)
    # print(E01)

    E01_list.append(E01)
    E02_list.append(E02)
    E12_list.append(E12)

plt.figure(1)
plt.plot(fb_list,E01_list)
plt.plot(fb_list,E12_list)

plt.plot(fb_list,E02_list)

plt.legend(['E01','E12','E02'])

plt.xlabel('fb')
plt.ylabel('\Delta E')


plt.title('Emn-fb(When a=0.4, Ej=85e9, Ecm=0.35e9)')
plt.show()