import gdspy as gs
import numpy as np



class CPW:
    lib=gs.GdsLibrary()
    cell=lib.new_cell('01')

    def __init__(self,w,d):
        self.w=w
        self.d=d
        self.D=d+w
        self.T1 = gs.Path(self.d, (0, 0))
        self.T2 = gs.Path(self.d, (self.D, 0))
        self.length=0

    def trans(self,v,direction='+y'):
        self.T1.segment(v,direction)
        self.T2.segment(v,direction)
        self.length+=v

    def round(self,r,n):
        rad=n*np.pi
        if n<0:
            self.T1.turn(r+self.D/2,rad)
            self.T2.turn(r-self.D/2,rad)
        else:
            self.T1.turn(r-self.D/2,rad)
            self.T2.turn(r+self.D/2,rad)

        self.length+=r*abs(rad)


    def cal(self):
        return self.length

    def save(self):
        self.cell.add(self.T1)
        self.cell.add(self.T2)

        self.lib.write_gds('Ttest.gds')



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
    a.trans(400,'+y')
    a.round(100,1/2)
    a.save()
    print(a.cal())



