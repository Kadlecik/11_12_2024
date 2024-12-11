import json

class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def save_to_json(self):
        data = {
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "color": self.color
        }

    @staticmethod
    def from_json(data):
        pass

        return Car()

    def __str__(self):
        return f'{self.brand} {self.model} {self.year} {self.color}'

    def start(self):
        print("I am starting.")


cars = [Car("bmw", "X6", 2020, "black"),
        Car("audi", "X6", 2020, "black"),
        Car("Skoda", "octavia", 2020, "black")]


counter = 0
for c in cars:
    c.save_to_json()