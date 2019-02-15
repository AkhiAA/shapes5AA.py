#shapes5AA.py by akhi abdullah 
from graphics import*
winX = 500
winY = 500
#--------------Window --------------------------
shapesWin = GraphWin("blue triangle",500,500)
shapesWin.setCoords(0,0,500,500)

#--------------Blue Triangle----------------------
bTri = Polygon(Point(50,50), Point(75,100), Point(100,50))
bTri.setFill("navy blue")
bTri.draw(shapesWin)

#---------------Red Circle-------------------
rCircle = Circle(Point(450,450), 25.5)
rCircle.setFill(color_rgb(230,10,10))
rCircle.draw(shapesWin)

#---------------Green Rectangle--------------------
gRectangle = Rectangle(Point(470,50),Point (425,75))
gRectangle.setFill(color_rgb(40,255,30))
gRectangle.draw(shapesWin)

#----------------Purple Oval------------------------
pOval = Oval(Point(50,465), Point(125,425))
pOval.setFill(color_rgb(200,20,200))
pOval.draw(shapesWin)

#------------------Blue Diamond----------------
bDiamond = Polygon(Point(winX/2-100,winY/2), Point(winX/2,winY/2+100), Point(winX/2+100,winY/2), Point(winX/2,winY/2-100))
bDiamond.setFill("light blue")
bDiamond.draw(shapesWin)


#--------------window------------
shapesWin.getMouse()
shapesWin.close()
