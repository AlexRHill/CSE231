import math

class Vector(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return('Vector = <%.2f,%.2f>'% (self.x, self.y))
    def __repr__(self):
        return self.__str__()
    def __add__(self, vector):
        x = self.x + vector.x
        y = self.y + vector.y
        return Vector(x,y)
    def __sub__(self, vector):
        x = self.x - vector.x
        y = self.y - vector.y
        return Vector(x,y)
    def __mul__(self, other):
        if type(other) == int:
            x = self.x * other
            y = self.y * other
            return Vector(x, y)
        else:
            scalar = (self.x*other.x) + (self.y*other.y)
            return(scalar)
    def __rmul__(self, rhs):
        return self.__mul__(rhs)
    def __eq__(self, other):
        if self.x == other.x:
            if self.y == other.y:
                return True
            else:
                return False
        else:
            return False
    def magnitude(self):
        return(math.hypot(self.x,self.y))
    def unit(self):
        if Vector.magnitude(self) == 0:
            print("cannot convert zero vector to a unit vector")
        else:
            self.x = self.x * (1/(Vector.magnitude(self)))
            self.y = self.y * (1/(Vector.magnitude(self)))
        
        
    

myVect = Vector(3,2)
otherVect = Vector(4,5)
zeroVect = Vector(0,0)
print("My Vector")
print(myVect)
add = myVect + otherVect
print("Add")
print(add)
subtract = myVect - otherVect
print("Subtract")
print(subtract)
mult1 = myVect * otherVect
print("Dot Product")
print(mult1)
mult2 = myVect * 3
print("Scalar Mult")
print(mult2)
mult3 = 3 * myVect
print("Rmul")
print(mult3)
print("Magnitude")
print(Vector.magnitude(myVect))
print("Unit")
Vector.unit(myVect)
print(myVect)
Vector.unit(zeroVect)
print(zeroVect)
