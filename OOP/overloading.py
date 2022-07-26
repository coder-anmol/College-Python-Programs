# addition overloading


class Point():

    def __init__(self, x, y):
        self.coordinates = (x, y)

    def __add__(self, point):
        return (
            self.coordinates[0] + point.coordinates[0],
            self.coordinates[1] + point.coordinates[1],
        )

    def __repr__(self):
        return (f"({self.coordinates[0]} , {self.coordinates[1]})")


p1 = Point(1, 1)
p2 = Point(2, 4)
p3 = p1 + p2

print("P1", p1)
print("P2", p2)
print("P1 + P2", p3)
