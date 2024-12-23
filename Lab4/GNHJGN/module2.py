class Plane:
    def __init__(self, model, speed):
        self.model = model
        self.speed = speed

    def plane_speed(self):
        return f'{self.model} ускоряется до 954 км/ч'
plane = Plane('AIR-67', '955')
print(plane.plane_speed())