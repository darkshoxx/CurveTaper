Doc = App.getDocument('SharePlinth')

# GLOBALS
radius = 10.0
pad_height = 3.0
font_file_path = "E:/KanjiSix/FreeCAD/yumin.ttf"

# Create Sketch
App.activeDocument().addObject('Sketcher::SketchObject', 'Sketch')
App.activeDocument().Sketch.Placement = App.Placement(App.Vector(0.000000, 0.000000, 0.000000), App.Rotation(0.000000, 0.000000, 0.000000, 1.000000))
App.activeDocument().Sketch.MapMode = "Deactivated"

ActiveSketch = Doc.getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)



corners = [
App.Vector(radius, radius, 0.0),
App.Vector(-radius, radius, 0.0),
App.Vector(-radius, -radius, 0.0),
App.Vector(radius, -radius, 0.0),
]

geoList = []
geoList.append(Part.LineSegment(corners[0],corners[1]))
geoList.append(Part.LineSegment(corners[1],corners[2]))
geoList.append(Part.LineSegment(corners[2],corners[3]))
geoList.append(Part.LineSegment(corners[3],corners[0]))

Doc.getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 0, 2, 1, 1))
constraintList.append(Sketcher.Constraint('Coincident', 1, 2, 2, 1))
constraintList.append(Sketcher.Constraint('Coincident', 2, 2, 3, 1))
constraintList.append(Sketcher.Constraint('Coincident', 3, 2, 0, 1))
constraintList.append(Sketcher.Constraint('Horizontal', 0))
constraintList.append(Sketcher.Constraint('Horizontal', 2))
constraintList.append(Sketcher.Constraint('Vertical', 1))
constraintList.append(Sketcher.Constraint('Vertical', 3))
ActiveSketch.addConstraint(constraintList)
del constraintList

# fully constrain

# Width
ActiveSketch.addConstraint(Sketcher.Constraint('Distance',3,1,1,2*radius))

# Attach to center
ActiveSketch.addConstraint(Sketcher.Constraint('Distance',-2,1,1,radius))

# Height
ActiveSketch.addConstraint(Sketcher.Constraint('Distance',2,1,0,2*radius))

# Attach to center
ActiveSketch.addConstraint(Sketcher.Constraint('Distance',-1,1,0,radius))



# Pad

Doc.addObject('Part::Extrusion','Extrude')
f = Doc.getObject('Extrude')
f.Base = Doc.getObject('Sketch')
f.DirMode = "Normal"
f.DirLink = None
f.LengthFwd = pad_height
f.LengthRev = 0.0
f.Solid = True
f.Reversed = False
f.Symmetric = False
f.TaperAngle = 0.0
f.TaperAngleRev = 0.0

import Draft
ss = Draft.make_shapestring(String="菴羅", FontFile="E:/KanjiSix/FreeCAD/yumin.ttf", Size=5.0, Tracking=0.0)
plm = FreeCAD.Placement()
plm.Base = FreeCAD.Vector(-5.0, -5.0, pad_height)
plm.Rotation.Q = (0.0, 0.0, 0.0, 1.0)
ss.Placement = plm
ss.AttachmentSupport = None
Draft.autogroup(ss)
FreeCAD.ActiveDocument.recompute()

Doc.recompute(None,True,True)