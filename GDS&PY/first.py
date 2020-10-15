import gdspy as gs



lib=gs.GdsLibrary()

cell=lib.new_cell('FIRST')

rect=gs.Rectangle((0,0),(2,1))
cell.add(rect)

lib.write_gds('first.gds')

cell.write_svg('first.svg')

gs.LayoutViewer()