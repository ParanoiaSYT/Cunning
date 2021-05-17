import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt



def func(x,a,b,c):
    return a*x**b+c

# def func(x,a,b,c):
#     return a*np.log(x**b)+c


# def func(x,a,b,c):
#     return a*np.exp(b*x)+c



x_original=np.linspace(40,295,52)
x_data=np.linspace(40,270,47)
y_original=[
    0.38,0.7,0.99,1.22,1.42,1.6,1.73,\
    1.87,2,2.125,2.225,2.33,2.38,2.5,\
    2.55,2.625,2.72,2.78,2.85,2.9,3,\
    3.05,3.1,3.125,3.14,3.2,3.225,3.37,\
    3.375,3.385,3.4,3.45,3.475,3.5,3.55,\
    3.576,3.672,3.634,3.67,3.679,3.736,3.758,\
    3.759,3.783,3.833,3.830,3.878,3.883,3.883,\
    3.877,3.878,3.879
]
y=[
    0.38,0.7,0.99,1.22,1.42,1.6,1.73,\
    1.87,2,2.125,2.225,2.33,2.38,2.5,\
    2.55,2.625,2.72,2.78,2.85,2.9,3,\
    3.05,3.1,3.125,3.14,3.2,3.225,3.37,\
    3.375,3.385,3.4,3.45,3.475,3.5,3.55,\
    3.576,3.672,3.634,3.67,3.679,3.736,3.758,\
    3.759,3.783,3.833,3.830,3.878,
]


popt,pcov=curve_fit(func,x_data,y,maxfev=500000)
# 有popt和pcov两个个参数，其中popt参数为a，b，c，pcov为拟合参数的协方差

print(popt)

# # 系数
a = popt[0]
b = popt[1]
c = popt[2]
print('y=%f*x**%f%f'%(a,b,c))

#拟合y值
yvals = func(x_data,a,b,c)
plot1 = plt.plot(x_original, y_original, 's',label='original values')
plot2 = plt.plot(x_data, yvals, 'r',label='polyfit values')
plt.xlabel('LaserPower')
plt.ylabel('Thickness_decrease')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('Thickness_decrease = 16681*LaserPower^0.000103-16687')
plt.show()