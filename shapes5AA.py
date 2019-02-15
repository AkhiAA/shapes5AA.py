#shapes5AA.py by akhi abdullah 
from graphics import*

shapesWin = GraphWin("blue triangle",500,500)
shapesWin.setCoords(90,90,950,950)

bTri = Polygon(Point(100,100), Point(150,200), Point(200,100))
bTri.setFill(color_rgb(30,30,230))
bTri.draw(shapesWin)

rCircle = Circle(Point(910,910), 30.5)
rCircle.setFill(color_rgb(230,10,10))
rCircle.draw(shapesWin)

gRectangle = Rectangle(Point(940,100),Point (850,150))
gRectangle.setFill(color_rgb(40,230,30))
gRectangle.draw(shapesWin)

pOval = Oval(Point(100,930), Point(250,850))
pOval.setFill(color_rgb(200,20,200))
pOval.draw(shapesWin)















shapesWin.getMouse()
shapesWin.close()
