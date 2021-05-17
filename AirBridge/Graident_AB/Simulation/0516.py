import matplotlib.pyplot as plt
import numpy as np


value=np.linspace(40,295,52)
# 两端都包含
# print(value)

height_lose=[
    0.38,0.7,0.99,1.22,1.42,1.6,1.73,\
    1.87,2,2.125,2.225,2.33,2.38,2.5,\
    2.55,2.625,2.72,2.78,2.85,2.9,3,\
    3.05,3.1,3.125,3.14,3.2,3.225,3.37,\
    3.375,3.385,3.4,3.45,3.475,3.5,3.55,\
    3.576,3.672,3.634,3.67,3.679,3.736,3.758,\
    3.759,3.783,3.833,3.830,3.878,3.883,3.883,\
    3.877,3.878,3.879
]

plt.figure(1)
plt.plot(value,height_lose)
plt.show()