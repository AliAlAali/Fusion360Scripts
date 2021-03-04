#Author-alaalial
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback
import math

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        ui.messageBox('Hello script')
        logSpiral()

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


def archimedeanSpiral():
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        des = adsk.fusion.Design.cast(app.activeProduct)
        root = des.rootComponent
        
        # Create a new sketch.
        sk = root.sketches.add(root.xYConstructionPlane)
 
        # Create a series of points along the spiral using the spiral equation.
        # r = a + (beta * theta)
        pnts = adsk.core.ObjectCollection.create()
        numTurns = 5
        pointsPerTurn = 20
        distanceBetweenTurns = 5  # beta
        theta = 0
        offset = 5                # a
        for i in range(pointsPerTurn * numTurns + 1):
            r = offset + (distanceBetweenTurns * theta) 
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            pnts.add(adsk.core.Point3D.create(x,y,0))
            
            theta += (math.pi*2) / pointsPerTurn
 
        sk.sketchCurves.sketchFittedSplines.add(pnts)        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def logSpiral():
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        des = adsk.fusion.Design.cast(app.activeProduct)
        root = des.rootComponent

        # Create a new sketch
        sketch = root.sketches.add(root.xYConstructionPlane)

        # Create a series of points along the spiral using the spiral equation.
        phi = (1 + math.sqrt(5)) / 2
        lamba = 2 / math.pi * math.log(phi)

        points = adsk.core.ObjectCollection.create()
        pointsShadow = adsk.core.ObjectCollection.create()

        theta = 0
        for i in range(0, 100):
            theta += (math.pi * 2) / 50
            radius = phi ** (2 / math.pi * theta)
            x = radius * math.cos(theta)
            y = radius * math.sin(theta)
            points.add(adsk.core.Point3D.create(x, y, 0))

            radius = phi ** (2 / math.pi * theta) + 0.3
            x = radius * math.cos(theta)
            y = radius * math.sin(theta)
            pointsShadow.add(adsk.core.Point3D.create(x, y, 0))

        sketch.sketchCurves.sketchFittedSplines.add(points)
        sketch.sketchCurves.sketchFittedSplines.add(pointsShadow)


    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
