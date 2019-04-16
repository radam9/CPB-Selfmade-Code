#OOP Homework
#Question 1 - Line
class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (((x2-x1)**2)+((y2-y1)**2))**0.5
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)

c1 = (3,2)
c2 = (8,10)
li = Line(c1,c2)
li.distance()
li.slope()

class Cylinder:
    def __init__(self,h,r):
        self.h = h
        self.r = r
    def volume(self):
        return 3.14 * self.r * self.r * self.h
    def sa(self):
        return 2*3.14*self.r*(self.h + self.r)

c = Cylinder(2,3)
c.volume()
c.sa()
