class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def max_speed(self):
        return f'{self.name} ускоряется до, {self.speed}'
my_car = Car('Mazda', '175 км/ч')
print(my_car.max_speed())
