import matplotlib.pyplot as plt
from AirBridge.Graident_AB.GiadientValue import *



a=Giadient_Design(h=3.2)
a.grey_calc()
x,y,ddx=a.coor

plt.figure(1)
# 去除四边框框


plt.bar(x=x, height=y, label='GiadentAirBridge', width=ddx ,color='steelblue',edgecolor='green', linewidth=0.5,alpha=0.3)

# for x1, yy in zip(x, y):
#     plt.text(x1, yy + 1, str(yy), ha='center', va='bottom', fontsize=10, rotation=0)

plt.plot(x,y, ms=10,color="slateblue")
plt.title('Giadent_AirBridge')

plt.show()