from math import pi

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):

        return float(pi * (self.radius ** 2))
    
    def perimeter(self):

        return float(self.radius * pi * 2)

circle_1 = Circle(9)

print(f"""
Obsah kruhu o poloměru {circle_1.radius} je {round(circle_1.area(), 4)} jednotek čtverečních
Jeho obvod je {round(circle_1.perimeter(), 3)} jednotek
""")