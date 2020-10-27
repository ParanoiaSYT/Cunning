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
        self.length+=v

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

    def pad(self, w1=20, d1=12,w2=400,l1=240,l2=400,d2=240, l=100):
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

    # def xmon(self,):


    def save(self,name='test.gds'):
        self.cell.add(self.path1)
        self.lib.write_gds(name)
        gs.LayoutViewer(self.lib)





if __name__=='__main__':
    a=CPW(16.6,14.6)

    a.trans(800,'+y')
    a.round(100,1)
    a.trans(800,'-y')
    a.round(100,-1)
    a.trans(800, '+y')
    a.round(100, 1)
    a.trans(800, '-y')
    a.round(100, -1)
    a.trans(800, '+y')
    a.round(100, 1)
    a.trans(800, '-y')
    a.round(100, -1)
    a.trans(400,'+y')
    a.round(100,1/2)
    a.trans_change(20,'-x',7.4,31)
    a.trans(400,'-x')
    a.pad(50,30)

    a.mark(400,40,40,10)
    a.number('123456789')
    # a.number('NJU')
    # a.trans()
    a.save('Ttest.gds')

    print(a.cal())



