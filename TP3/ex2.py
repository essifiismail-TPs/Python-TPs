import math

class Deplacement:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficher_point(self):
        print(f"({self.x}, {self.y})")

    def distance(self, autre):
        return math.sqrt((autre.x - self.x)**2 + (autre.y - self.y)**2)

    def milieu_segment(self, autre):
        return Point((self.x + autre.x) / 2, (self.y + autre.y) / 2)

    def translation(self, deplacement):
        return Point(self.x + deplacement.dx, self.y + deplacement.dy)

    def projection_x(self):
        return Point(self.x, 0)

    def projection_y(self):
        return Point(0, self.y)

xA = float(input("x A: "))
yA = float(input("y A: "))
xB = float(input("x B: "))
yB = float(input("y B: "))

A = Point(xA, yA)
B = Point(xB, yB)

A.afficher_point()
B.afficher_point()

print(A.distance(B))

milieu = A.milieu_segment(B)
milieu.afficher_point()

proj_A_x = A.projection_x()
proj_A_x.afficher_point()

dx = float(input("dx: "))
dy = float(input("dy: "))
dep = Deplacement(dx, dy)

A = A.translation(dep)
B = B.translation(dep)

A.afficher_point()
B.afficher_point()

proj_A_x_nouv = A.projection_x()
proj_A_x_nouv.afficher_point()