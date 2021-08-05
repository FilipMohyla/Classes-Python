from math import pi

class Shapes():
    
    def area_difference(self, objekt2):
        
        return abs(self.area() - objekt2.area())

class Square(Shapes):
    
    def __init__(self, name, side):
        
        self.name = name
        self.side = side

    def area(self):

        return (self.side ** 2)
    
    def perimeter(self):

        return (self.side * 4)  


class Circle(Shapes):

    def __init__(self, name, radius):
        
        self.name = name
        self.radius = radius

    def area(self):

        return (pi * (self.radius ** 2))
    
    def perimeter(self):

        return (self.radius * pi * 2)


class Rectangle(Shapes):

    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

    def area(self):

        return (self.width * self.height)
    
    def perimeter(self):

        return (2 * (self.width + self.height)) 

square_1 = Square("Čtverec 1", 5)
circle_1 = Circle("Kruh 1", 9)
rect_1 = Rectangle("Obdélník 1", 5, 5)

print(f"""
Objekt {square_1.name} má obsah {square_1.area()} jednotek čtverečních
Objekt {rect_1.name} má obsah {rect_1.area()} jednotek čtverečních
Rozdíl jejich obsahů je {circle_1.area_difference(square_1)} jednotek čtverečních
""")