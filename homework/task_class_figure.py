from math import pi

class Figure(object):
    def get_area(self):
        raise NotImplementedError

    def get_perimeter(self):
        raise NotImplementedError
    
class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def get_perimeter(self):
        return 2 * (self.a + self.b)
        
    def get_area(self):
        return self.a * self.b


class Triangle(Figure):
    def __init__(self,a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def get_perimeter(self):
        return self.a + self.b + self.c
        
    def get_area(self):
        p = self.get_perimeter() / 2
        return (p*(p-self.a) * (p-self.b) * (p-self.c)) **.5



class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def get_perimeter(self):
        return self.r * (2 * pi)

    def get_area(self):
        return (self.r ** 2) * pi
