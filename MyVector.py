class MyVector:
    '''MyVector is a vector has +, -, scalar multiplication and abs'''
    name = "vector"
   
    
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, other):
        return MyVector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return MyVector(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return (self.x * self.y) + (self.y * other.y)
    def __str__(self):
        return "%d, %d" % (self.x, self.y)
    def __abs__(self):
        return sqrt((self.x * self.x) +(self.y * self.y))
from math import*
v1 = MyVector(1,0)
v2 = MyVector(0,1)
print(v1*v2)
print(v1+v2)
print(abs(v1))
