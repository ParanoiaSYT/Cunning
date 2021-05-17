import gdspy as gs
from GiadientValue import *




lib = gs.GdsLibrary(precision=1e-9)
cell = lib.new_cell('01')

def dose_poly(w=30,h=3,l=12,x=0,y=0):

    delta_x=Giadient_Design(w=w,h=h,l=l).grey_calc()
    # print(delta_x)
    list.reverse(delta_x)
    # list.reverse () 的返回值是 None ，它逆序的结果直接体现在原来的列表里面。
    # print(delta_x)



    number=len(delta_x)
    delta_x_new=[]
    for i in range(number):
        # delta_x_new.append(int(delta_x[i]+0.5))
    ## 四舍五入取到整型
        delta_x_new.append(int(delta_x[i] * 1000) / 1000)
    ##  无法通过round方法：会导致报错，可以通过这样来截取三位小数！！

    w1=delta_x_new[0]
    points0=[(x-w1,y+l/2),(x-w1,y-l/2),(x+w1,y-l/2),(x+w1,y+l/2)]
    poly0=gs.Polygon(points0,layer=11)
    cell.add(poly0)

    x_i_1=w1
    for i in range(1,number):
        ddx=delta_x_new[i]
        points_right=[(x+x_i_1,y+l/2),(x+x_i_1,y-l/2),(x+x_i_1+ddx,y-l/2),(x+x_i_1+ddx,y+l/2)]
        poly_right = gs.Polygon(points_right, layer=11+i)
        cell.add(poly_right)

        points_left = [(x - x_i_1, y + l / 2), (x - x_i_1, y - l / 2), (x - x_i_1 - ddx, y - l / 2),
                        (x - x_i_1 - ddx, y + l / 2)]
        poly_left = gs.Polygon(points_left, layer=11 + i)
        cell.add(poly_left)
    #
        x_i_1 += delta_x_new[i]

    ## 桥墩绘制
    qd_width=30
    qd_l=l+10
    points_qd_left=[(x - x_i_1, y + qd_l / 2), (x - x_i_1, y - qd_l / 2), (x - x_i_1 - 20, y - qd_l / 2),
                        (x - x_i_1 - 20, y + qd_l / 2)]
    poly_qd_left = gs.Polygon(points_qd_left, layer=number+11)
    cell.add(poly_qd_left)
    points_qd_right = [(x + x_i_1, y + qd_l / 2), (x + x_i_1, y - qd_l / 2), (x + x_i_1 + 20, y - qd_l / 2),
                 (x + x_i_1 + 20, y + qd_l / 2)]
    poly_qd_right = gs.Polygon(points_qd_right, layer=number + 11)
    cell.add(poly_qd_right)

def save_ab():
    lib.write_gds("ABGreyDose.gds")
    gs.LayoutViewer(lib)


if __name__=="__main__":
    dose_poly(w=30,h=3.2,l=12,x=0,y=0)
    dose_poly(w=25,h=3.2,l=12,x=0,y=100)
    dose_poly(w=20,h=3.2,l=12,x=0,y=200)

    dose_poly(w=30, h=3.2, l=20, x=100, y=0)
    dose_poly(w=25, h=3.2, l=20, x=100, y=100)
    dose_poly(w=20, h=3.2, l=20, x=100, y=200)

    dose_poly(w=30, h=3.2, l=40, x=200, y=0)
    dose_poly(w=25, h=3.2, l=40, x=200, y=100)
    dose_poly(w=20, h=3.2, l=40, x=200, y=200)

    save_ab()
