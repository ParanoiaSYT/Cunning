import gdspy as gs
import numpy as np



def dose_poly(h=12,w=30,num=100,x=0,y=0):
    # w1=w/num
    w1=1.524
    lib = gs.GdsLibrary()
    cell = lib.new_cell('01')

    points0=[(x-w1/2,y+h/2),(x-w1/2,y-h/2),(x-w1/2-20,y-h/2),(x-w1/2-20,y+h/2)]
    points1=[(x-w1/2+w,y+h/2),(x-w1/2+w+20,y+h/2),(x-w1/2+w+20,y-h/2),(x-w1/2+w,y-h/2)]
    poly0=gs.Polygon(points0,layer=999)
    cell.add(poly0)
    poly1=gs.Polygon(points1,layer=999)
    cell.add(poly1)

    for i in range(num):
        points = [(x+w1/2,y+h/2),(x+w1/2,y-h/2),(x-w1/2,y-h/2),(x-w1/2,y+h/2)]
        poly = gs.Polygon(points, layer=i+1)
        x+=w1
        cell.add(poly)

    lib.write_gds("ABGreyDose.gds")
    gs.LayoutViewer(lib)



if __name__=="__main__":
    dose_poly(num=100)
