class Car(object):
    def __init__(self, color, model, top_speed):
        self.color = color
        self.model = model
        self.top_speed = top_speed

    def start(self):
        print("the car has started")

    def stop(self):
        print("the car has stopped")


car = Car("red", "tesla", "200 million")
print(car.color)
