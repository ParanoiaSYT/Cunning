from sympy import *


n0,n1,n2,n3,n_x1,n_x2,n_x3=symbols('no n1 n2 n3 n_x1 n_x2 n_x3')

H1=(n1-0.5*((n1+n2+n3)+n_x1-n_x3))**2+(-n2+0.5*((n1+n2+n3)+n_x2-n_x3))**2-n1*n2

# print(H1)
res1=expand(H1)
print(res1)


print('===========================')
H2=(n1-n_x1)**2+(n2-n_x2)**2+(n3-n_x3)**2
res2=expand(H2)
print(res2)