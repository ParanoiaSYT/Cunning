import gdspy as gs
import numpy as np




lib = gs.GdsLibrary()
cell = lib.new_cell('01')

# def dose_poly(w=30,h=12,l=12,num=20,x=0,y=0):

def dose_poly(w=30,l=12,num=20,x=0,y=0):
    w1=w/num
    # w1=1.524

###########
    points0 = [(x - w1, y + l / 2), (x - w1, y - l / 2), (x + w1, y - l / 2), (x + w1, y + l / 2)]
    poly0 = gs.Polygon(points0, layer=11)
    cell.add(poly0)

    x_i_1 = w1
    number=num//2
    for i in range(1, number):
        ddx = w1
        points_right = [(x + x_i_1, y + l / 2), (x + x_i_1, y - l / 2), (x + x_i_1 + ddx, y - l / 2),
                        (x + x_i_1 + ddx, y + l / 2)]
        poly_right = gs.Polygon(points_right, layer=11 + i)
        cell.add(poly_right)

        points_left = [(x - x_i_1, y + l / 2), (x - x_i_1, y - l / 2), (x - x_i_1 - ddx, y - l / 2),
                       (x - x_i_1 - ddx, y + l / 2)]
        poly_left = gs.Polygon(points_left, layer=11 + i)
        cell.add(poly_left)
        #
        x_i_1 += w1

    ## 桥墩绘制
    qd_width = 30
    qd_l = l + 10
    points_qd_left = [(x - x_i_1, y + qd_l / 2), (x - x_i_1, y - qd_l / 2), (x - x_i_1 - 20, y - qd_l / 2),
                      (x - x_i_1 - 20, y + qd_l / 2)]
    poly_qd_left = gs.Polygon(points_qd_left, layer=number + 11)
    cell.add(poly_qd_left)
    points_qd_right = [(x + x_i_1, y + qd_l / 2), (x + x_i_1, y - qd_l / 2), (x + x_i_1 + 20, y - qd_l / 2),
                       (x + x_i_1 + 20, y + qd_l / 2)]
    poly_qd_right = gs.Polygon(points_qd_right, layer=number + 11)
    cell.add(poly_qd_right)


def save_ab():
    lib.write_gds("test001.gds")
    gs.LayoutViewer(lib)










##################
    # points0=[(x-w1/2,y+h/2),(x-w1/2,y-h/2),(x-w1/2-20,y-h/2),(x-w1/2-20,y+h/2)]
    # points1=[(x-w1/2+w,y+h/2),(x-w1/2+w+20,y+h/2),(x-w1/2+w+20,y-h/2),(x-w1/2+w,y-h/2)]
    # poly0=gs.Polygon(points0,layer=999)
    # cell.add(poly0)
    # poly1=gs.Polygon(points1,layer=999)
    # cell.add(poly1)
    #
    # for i in range(num):
    #     points = [(x+w1/2,y+h/2),(x+w1/2,y-h/2),(x-w1/2,y-h/2),(x-w1/2,y+h/2)]
    #     poly = gs.Polygon(points, layer=i+1)
    #     x+=w1
    #     cell.add(poly)
    #
    # lib.write_gds("ABGreyDose.gds")
    # gs.LayoutViewer(lib)



if __name__=="__main__":
    dose_poly(w=30,l=12,num=20,x=0,y=0)
    dose_poly(w=25,l=12,num=20,x=0,y=100)
    dose_poly(w=20,l=12,num=20,x=0,y=200)

    dose_poly(w=30, l=20, num=20, x=100, y=0)
    dose_poly(w=25, l=20, num=20, x=100, y=100)
    dose_poly(w=20, l=20, num=20, x=100, y=200)

    dose_poly(w=30, l=40, num=20, x=200, y=0)
    dose_poly(w=25, l=40, num=20, x=200, y=100)
    dose_poly(w=20, l=40, num=20, x=200, y=200)

    save_ab()
