import turtle

class Triangle(object):
    def __init__(self,coord1 = (0.0,0.0),coord2 = (10.0,0.0),coord3 = (10.0,10.0),
                 fillcolor = '',linecolor = 'black'):
        '''takes coordinates and colors as input'''
        self.coord1 = coord1
        self.coord2 = coord2
        self.coord3 = coord3
        self.fillcolor = fillcolor
        self.linecolor = linecolor
        self.tag = "Triangle"

    def __str__(self):
        return "%s(%s,%s,%s)" % (self.tag,self.coord1,self.coord2,self.coord3)

    def draw(self,pen):
        '''draw the triangle'''
        pen.pencolor(self.linecolor)
        if pen.pos() != self.coord1:
            pen.up()
            pen.goto(self.coord1)
        if self.fillcolor:
            pen.fillcolor(self.fillcolor)
            pen.begin_fill()
        pen.down()
        pen.goto(self.coord2)
        pen.goto(self.coord3)
        pen.goto(self.coord1)
        pen.end_fill()
        pen.up()

class Rectangle(object):
    def __init__(self,coord1 = (0.0,0.0),coord2 = (150.0,200.0),fillcolor = '',
                 linecolor = 'black'):
        '''takes coordinates and colors as input'''
        self.coord1 = coord1
        self.coord2 = coord2
        self.fillcolor = fillcolor
        self.linecolor = linecolor
        self.tag = "Rectangle"

    def __str__(self):
        return "%s(%s,%s)" % (self.tag,self.coord1,self.coord2)

    def draw(self,pen):
        '''draw the rectangle'''
        pen.pencolor(self.linecolor)
        if pen.pos() != self.coord1:
            pen.up()
            pen.goto(self.coord1)
        if self.fillcolor:
            pen.fillcolor(self.fillcolor)
            pen.begin_fill()
        pen.goto(150.0,0.0)
        pen.goto(self.coord2)
        pen.goto(0.0,200.0)
        pen.goto(self.coord1)
        pen.end_fill()
        pen.up()

class Circle(object):
    def __init__(self,center = (0.0,0.0),radius = 10.0,fillcolor = '',
                 linecolor = 'black'):
        '''takes coordinates and colors as input'''
        self.center = center
        self.radius = radius
        self.fillcolor = fillcolor
        self.linecolor = linecolor
        self.tag = "circle"

    def __str__(self):
        return "%s(%s,%s)" % (self.tag,self.center,self.radius)

    def draw(self,pen):
        '''draw the circle'''
        pen.pencolor(self.linecolor)
        if pen.pos() != self.center:
            pen.up()
            pen.goto(self.center)
        if self.fillcolor:
            pen.fillcolor(self.fillcolor)
            pen.begin_fill()
        #pen.right(90)
        #pen.forward(radius)
        pen.down()
        pen.circle(self.radius)
        pen.end_fill()

def main():
    pen = turtle.Turtle()

    rectangle = Rectangle((0.0,0.0),(150.0,200.0),'blue','black')
    rectangle.draw(pen)
    print(rectangle)
    
    triangle = Triangle((-25.0,200.0),(75.0,200.0),(75.0,250.0),'black','black')
    triangle.draw(pen)
    str(triangle)
    
    triangle = Triangle((175.0,200.0),(75.0,200.0),(75.0,250.0),'black','black')
    triangle.draw(pen)

    circle = Circle((-100,250),50,'yellow','black')
    circle.draw(pen)
    str(circle)




main()


        
        

        
