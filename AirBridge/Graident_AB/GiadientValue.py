# import plistlib
from sympy import *


x,y,thick=symbols('x y thick')

class Giadient_Design:
    def __init__(self,w=30,h=3,l=12):
        self.w=w
        self.h=h
        self.l=l

    def grey_calc(self):
        w=self.w
        h=self.h
        r=w**2/(8*h)+h/2
        self.fx=sqrt(r**2-x**2)-(r-h)
        fy=-1*sqrt(r**2-(y+r-h)**2)

        # y_min=self.fx.subs(x,-1*w/2+1)-self.fx.subs(x,-1*w/2)
        y_min=0.28
        print(y_min)

        turn=0
        self.delta_x=[]
        x1 = fy.subs(y, y_min) - fy.subs(y, 0)
        # print(type(fy.subs(y,y_min*(turn+2))))
        # if fy.subs(y,y_min*(turn+2))<h:
        #     print("111")

        # 根据y_min的倍数来定x的位置
        while 1:
            x1=fy.subs(y,y_min*(turn+1))-fy.subs(y,y_min*turn)
            if y_min*(turn+1)>h:
                x2=0-fy.subs(y,y_min*turn)
                self.delta_x.append(x2)
                break
            else:
                self.delta_x.append(x1)
                turn += 1


        # 取每层的中心定剂量
        x_sum=0
        self.x_coordinate=[]
        for i in range(len(self.delta_x)):
            x_i=-1*self.w/2+self.delta_x[i]/2+x_sum
            x_sum += self.delta_x[i]
            self.x_coordinate.append(x_i)

        # 这里是power对于剩余厚度的函数
        LaserPower= ((16690.539477 -thick)/1.66809672e+04)**(1.02533818e-04**-1)
        for j in range(len(self.delta_x)):
            res = self.fx.subs(x, self.x_coordinate[j])
            # print(res)
            gradient=LaserPower.subs(thick,res)
            num=len(self.delta_x)
            print("第%d层layer的greyvlue为："%(10+num-j)+str(gradient))
        print("桥面一共有%d层"%num)



        # # 获取最大剂量和最小剂量
        # dose_max=140
        # dose_min=40
        # for j in range(len(self.delta_x)):
        #     res = self.fx.subs(x, self.x_coordinate[j])
        #     giadent=int(dose_max-res*((dose_max-dose_min)/h))
        #     num=len(self.delta_x)
        #     print("第%d个layer的greyvlue为："%(10+num-j)+str(giadent))
        # print("桥面一共有%d层"%num)

        return self.delta_x

    @property
    def coor(self):
        ## x、y所有中心坐标
        x_coor_all=[]
        x_copy=self.x_coordinate
        for whichcoor in x_copy:
            x_coor_all.append(whichcoor)
        list.reverse(x_copy)
        for whichcoor in x_copy:
            whichcoor*=-1
            x_coor_all.append(whichcoor)

        y_coor_all=[]
        for each in x_coor_all:
            y_coor_all.append(self.fx.subs(x,each))

        ## 绘图间隔
        delta_x_all=[]
        delta_x_copy=self.delta_x
        for each in delta_x_copy:
            delta_x_all.append(each)

        list.reverse(delta_x_copy)
        for each in delta_x_copy:
            delta_x_all.append(each)

        return x_coor_all,y_coor_all,delta_x_all


if __name__=="__main__":
    a=Giadient_Design(h=3)
    print(a.grey_calc())
    print(a.coor)