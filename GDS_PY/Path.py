import gdspy as gs
import numpy as np


lib=gs.GdsLibrary()

cell=lib.new_cell('PATH')

path1=gs.Path(4,(0,0))
path1.segment(6,'+y')
path1.turn(12,np.pi/4)
path1.turn(8,'rr')


path2=gs.Path(14.6, (-20, 0), number_of_paths=2, distance=16.6)
# path2.segment(2, "-y", final_width=0.5)
path2.segment(200, "-y")
path2.turn(100,'r')

path3=gs.Path(2,(0,0))
path3.bezier([(0,5),(5,5),(5,10)])

path4=gs.Path(1,(0,0))
path4.segment(100,'+x')
# path4.segment(100,'+x',axis_offset=10)
path4.turn(10,'l').turn(10,'r')


# cell.add(path1)
# cell.add(path2)
# cell.add(path3)
cell.add(path4)


lib.write_gds('Path.gds')

gs.LayoutViewer(lib)