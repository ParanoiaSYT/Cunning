import gdspy as gs
import numpy as np



class CPW:
    lib=gs.GdsLibrary()
    cell=lib.new_cell('01')

    def __init__(self,w,d):
        # w is the width of center conductor, d is the width of gap
        self.w=w
        self.d=d
        self.D=d+w
        self.path1 = gs.Path(d, (0, 0),number_of_paths=2,distance=self.D)
        # self.path2=gs.Path(d)
        self.length=0

    def trans(self,v,direction='+y'):
        self.path1.segment(v,direction)
        self.length+=v

    def trans_change(self,v,direction='+y',fw=0,fd=0):
        fd=fw+fd
        self.path1.segment(v,direction,final_width=fw,final_distance=fd)
        # self.length+=v

    # def pad(self,v=300,direction='-x',fw=230,fd=400,ao=200):
    #     fd=fw+fd
    #     self.path1.segment(v,direction=direction,final_width=fw,final_distance=fd,axis_offset=ao)
    #     self.path1.segment(v,direction=direction)


    def round(self,r,n):
        rad=n*np.pi
        self.path1.turn(r,rad)

        self.length+=r*abs(rad)

    def cal(self):
        return self.length

    def pad(self, w1=21.8, d1=12,w2=400,l1=240,l2=400,d2=240, l=100):
        points=[(0,w1/2),(-l1,w2/2),(-l1-l2,w2/2),(-l1-l2,-w2/2),(-l1,-w2/2),(0,-w1/2),\
                (0,-w1/2-d1),(-l1,-w2/2-d2),(-l1-l2-l,-w2/2-d2),(-l1-l2-l,w2/2+d2),(-l1,w2/2+d2),(0,w1/2+d1)]
        self.poly=gs.Polygon(points,layer=1)
        self.cell.add(self.poly)

    def mark(self,w1=200,d1=20,w2=20,d2=4):
        self.l1=gs.Rectangle((-w1/2,d1/2),(w1/2,-d1/2),layer=3)
        self.l2=gs.Rectangle((-d1/2,w1/2),(d1/2,-w1/2),layer=3)
        self.l12=gs.boolean(self.l1,self.l2,'xor',layer=3)

        self.m1=gs.Rectangle((-w2/2,d2/2),(w2/2,-d2/2),layer=3)
        self.m2=gs.Rectangle((-d2/2,w2/2),(d2/2,-w2/2),layer=3)
        self.m12=gs.boolean(self.m1,self.m2,'or',layer=3)

        self.lm=gs.boolean(self.l12,self.m12,'or',layer=3)
        self.cell.add(self.lm)

    def number(self,text='123456',size=300):
        self.htext1=gs.Text(text=text,size=size,layer=2)
        self.cell.add(self.htext1)

    def resonator(self,L,X=0,Y=0):
        r=25
        l1=121.2
        l2=182.2
        l=(L-3900)/14
        self.path1 = gs.Path(self.d, (X, Y+2.5), number_of_paths=2, distance=self.D)
        self.path1.segment(120,direction='+y')
        self.path1.turn(r,-np.pi/2)
        self.path1.segment(80,"+x")
        self.path1.turn(r,np.pi)
        self.path1.segment(234,"-x")
        self.path1.turn(r,-np.pi)
        self.path1.segment(234, "+x")
        self.path1.turn(r, np.pi)
        self.path1.segment(234, "-x")
        self.path1.turn(r, -np.pi)
        self.path1.segment(234, "+x")
        self.path1.turn(r, np.pi)
        self.path1.segment(234, "-x")
        self.path1.turn(r, -np.pi)
        self.path1.segment(l2+l,"+x")
        self.path1.turn(r, np.pi)
        self.path1.segment(l1+2*l,"-x")
        self.path1.turn(r, -np.pi)
        self.path1.segment(l1+2*l,"+x")
        self.path1.turn(r, np.pi)
        self.path1.segment(l1+2*l, "-x")
        self.path1.turn(r, -np.pi)
        self.path1.segment(l1+2*l, "+x")
        self.path1.turn(r, np.pi)
        self.path1.segment(l1 + 2 * l, "-x")
        self.path1.turn(r, -np.pi)
        self.path1.segment(l1 + 2 * l, "+x")
        self.path1.turn(r, np.pi)
        self.path1.segment(l2+l, "-x")

        self.path1.turn(r, -np.pi / 2)
        self.path1.segment(100, '+y')
        self.path1.turn(r, -np.pi / 2)
        self.path1.segment(300, "+x")

        self.cell.add(self.path1)
        self.length += r * 2*np.pi*7.25+120+300+250*5+(l2+l)*2+(l1+2*l)*6




    def sink(self,X=0,Y=0):
        points1 = [(X - 5, Y - 2.5), (X - 5, Y + 2.5), (X - 79, Y + 2.5), (X - 79, Y - 83), (X - 39, Y - 83),
                   (X - 39, Y - 17.5), (X + 39, Y - 17.5), (X + 39, Y - 83), (X + 79, Y - 83),
                   (X + 79, Y + 2.5), (X + 5, Y + 2.5), (X + 5, Y - 2.5), (X + 74, Y - 2.5), (X + 74, Y - 78),
                   (X + 44, Y - 78), (X + 44, Y - 12.5), (X - 44, Y - 12.5), (X - 44, Y - 78), (X - 74, Y - 78),
                   (X - 74, Y - 2.5)]
        poly1 = gs.Polygon(points1)
        self.cell.add(poly1)

    def ten(self,X=0,Y=0):
        points2 = [(X - 36, Y - 20.5), (X - 36, Y - 160.5), (X - 124, Y - 160.5), (X - 124, Y - 148.5),
                   (X - 182, Y - 148.5), (X - 182, Y - 244.5), (X - 124, Y - 244.5), (X - 124, Y - 232.5),
                   (X - 36, Y - 232.5), (X - 36, Y - 318.5), (X - 9, Y - 318.5), (X - 9, Y - 314.5),
                   (X - 11, Y - 314.5), (X - 11, Y - 312.5), (X - 7, Y - 312.5), (X - 7, Y - 318.5),
                   (X + 7, Y - 318.5), (X + 7, Y - 312.5), (X + 11, Y - 312.5), (X + 11, Y - 314.5), (X + 9, Y - 314.5),
                   (X + 9, Y - 318.5), (X + 36, Y - 318.5), (X + 36, Y - 232.5),
                   (X + 124, Y - 232.5), (X + 124, Y - 244.5), (X + 182, Y - 244.5), (X + 182, Y - 148.5),
                   (X + 124, Y - 148.5), (X + 124, Y - 160.5), (X + 36, Y - 160.5),
                   (X + 36, Y - 20.5)]
        points3 = [(X - 12, Y - 44.5), (X - 12, Y - 184.5), (X - 148, Y - 184.5), (X - 148, Y - 180.5),
                   (X - 172, Y - 180.5), (X - 172, Y - 212.5), (X - 148, Y - 212.5), (X - 148, Y - 208.5),
                   (X - 12, Y - 208.5), (X - 12, Y - 300.5), (X - 1.5, Y - 300.5), (X - 1.5, Y - 306.5),
                   (X + 2.5, Y - 306.5), (X + 2.5, Y - 304.5), (X + 0.5, Y - 304.5), (X + 0.5, Y - 300.5),
                   (X + 12, Y - 300.5),
                   (X + 12, Y - 208.5), (X + 148, Y - 208.5), (X + 148, Y - 212.5), (X + 172, Y - 212.5),
                   (X + 172, Y - 180.5), (X + 148, Y - 180.5), (X + 148, Y - 184.5), (X + 12, Y - 184.5),
                   (X + 12, Y - 44.5)]
        poly2 = gs.Polygon(points2)
        poly3 = gs.Polygon(points3)
        cap_fin = gs.boolean(poly2, poly3, "not")
        self.cell.add(cap_fin)

    def save(self,name='test.gds'):
        self.cell.add(self.path1)
        self.lib.write_gds(name)
        # gs.LayoutViewer(self.lib)



# import sys
# sys.modules[__name__] = CPW()



if __name__=='__main__':
    a=CPW(10,6)

    a.resonator(5000,0,0)
    a.ten(0,0)
    a.sink(0,0)
    # a.number('NJU')
    # a.trans()
    a.save('Ttest.gds')

    print(a.cal())



