#shapes5AA.py by akhi abdullah 
from graphics import*

bTriWin = GraphWin("blue triangle",300,300)
bTriWin.setCoords(0,0,300,300)

bTri = Polygon (Point(100,100), Point (150,200), Point (200,100))
bTri.setFill (color_rgb(30,30,230))
bTri.draw (bTriWin)

bTriWin.getMouse()
bTriWin.close()
