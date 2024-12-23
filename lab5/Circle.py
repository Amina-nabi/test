class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius
my_circle = Circle(10)
print("Текущий радиус:", my_circle.get_radius())
my_circle.set_radius(56)
print("Новый радиус:", my_circle.get_radius())
