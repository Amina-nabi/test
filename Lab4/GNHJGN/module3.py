class Yacht:
    def __init__(self, model, speed):
        self.model = model
        self.speed = speed
    def yacht_speed(self):
        return f'{self.model}, ускоряется до 135 км/ч'
yacht = Yacht('Titan', '25')
print(yacht.yacht_speed())
