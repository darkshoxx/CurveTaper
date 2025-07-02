import Draft
ss = Draft.make_shapestring(String="悪", FontFile="E:/KanjiSix/FreeCAD/yumin.ttf", Size=10.0, Tracking=0.0)
plm = FreeCAD.Placement()
plm.Base = FreeCAD.Vector(0.0, 0.0, 0.0)
plm.Rotation.Q = (0.0, 0.0, 0.0, 1.0)
ss.Placement = plm
ss.AttachmentSupport = None
Draft.autogroup(ss)
FreeCAD.ActiveDocument.recompute()