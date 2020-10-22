import gdspy as gs
import numpy as np



lib=gs.GdsLibrary()

cell=lib.new_cell('T')

D=14.6
W=16.6
S=D+W

T1=gs.Path(D,(0,0))
T2=gs.Path(D,(S,0))

T1.segment(200,'+y')
T2.segment(200,'+y')

T1.turn(100+S/2,'r')
T2.turn(100-S/2,'r')

cell.add(T1)
cell.add(T2)

lib.write_gds('TransmissionLine.gds')
gs.LayoutViewer(lib)
