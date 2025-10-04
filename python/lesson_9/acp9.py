class Robot:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def introduce(self):
        print(f" Hello! I am {self.name}, a {self.model} robot built in {self.year}.")

    def greet(self, human):
        print(f"Hello {human}! I am {self.name}, at your service.")


r1 = Robot("Akki", "Codingal", 2025)

r1.introduce()

r1.greet("Akshita")
