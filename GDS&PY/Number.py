import gdspy as gs



lib=gs.GdsLibrary()

cell=lib.new_cell('Num')

htext1=gs.Text('123456',5,(0,0))

htext2=gs.Text('7891011',10,(15,15))

vtext=gs.Text('ABCD',1.5,(-5,-5),horizontal=False)

cell.add(htext1)
cell.add(htext2)
cell.add(vtext)


lib.write_gds('num_write.gds')

gs.LayoutViewer(lib)