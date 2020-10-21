import gdspy as gs
import numpy as np


lib=gs.GdsLibrary()

cell=lib.new_cell('PATH')

path1=gs.Path(4,(0,0))

path1.segment(6,'+y')
path1.turn(12,np.pi/4)

path1.turn(8,'rr')


cell.add(path1)
lib.write_gds('Path.gds')

gs.LayoutViewer(lib)