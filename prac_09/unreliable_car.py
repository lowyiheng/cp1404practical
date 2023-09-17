import random
from car import Car


class Unreliable_car(Car):
    def __init__(self, name, fuel, reliable):
        super().__init__(name, fuel)
        self.reliable = reliable

    def drive(self, distance):
        if random.randint(0, 100) < self.reliable:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
