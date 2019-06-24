# Змінити зразок файлу на версію чотирикутника

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side" + str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Quadrangle (Polygon):
    def __init__(self):
        print("Input sides of quadrangle")
        Polygon.__init__(self,4) 

    def findPerymetr(self):
        a, b, c, d = self.sides
        perymetr = (a + b + c + d) / 2
        print('The perymetr of the quadrangle is %0.2f' %perymetr)

q=Quadrangle()
q.inputSides()
q.findPerymetr()


# Створити батьківський клас Figure з методами __init__: ініціалізується колір, 
# від якого наслідуються такі класи як Rectangle, Square, які мають інформацію 
# про ширину, висоту фігури, метод square, який знаходить площу фігури.

class Figure:
    def __init__ (self, no_of_sides):
        self.n=no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
        
    def name_of_colour(self):
        self.color = input("Input colour of figure: ")
        print("Colour of figure is {}".format(self.color))

    def inputSides(self):
        self.sides = [float(input("Enter side " + str(i+1) +" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Rectangle(Figure):
    def __init__(self):
        Figure.__init__(self, 2)

    def area(self):
        areaRectangle=self.sides[0]*self.sides[1]
        # print("Colour of Rectangle is {}".format(self.color))
        print("Area of Rectangle = {}".format(areaRectangle))
        
class Square(Figure):
    def __init__(self):
        Figure.__init__(self, 1)

    def area(self):
        areaSquare=self.sides[0] ** 2
        # print("Colour of Square is {}".format(self.color))
        print("Area of Square = {}".format(areaSquare))

F1=Rectangle()
print("Figure is rectangle")
F1.name_of_colour()
F1.inputSides()
F1.area()
print("")

F2=Square()
print("Figure is square")
F2.name_of_colour()
F2.inputSides()
F2.area()
