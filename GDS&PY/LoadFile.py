import gdspy as gs



gs2=gs.GdsLibrary(infile='first.gds')
# lib=gs.GdsLibrary()
#
print(gs2.cells)
cell=gs2.cells['FIRST']

# cell=gs2['FIRST']
# cell=gs2.read_gds('first.gds')
points = [(0, 0), (2, 2), (2, 6), (-6, 6), (-6, -6), (-4, -4), (-4, 4), (0, 4)]

poly=gs.Polygon(points)
cell.add(poly)


gs2.write_gds('first.gds')

