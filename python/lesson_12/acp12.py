class Animal:
    def __init__(self, name, size, colour):
        self.name = name
        self.size = size
        self.colour = colour

    def info(self):
        print(f'Hi I am {self.name}, and I am {self.size}')


class Human:
    def __init__(self, emotions,travel, cafe_hoping):
        self.emotions = emotions
        self.travel = travel
        self.cafe_hoping = cafe_hoping

    def info(self):
        print(f'Hi i am emotion: {self.emotions}, I do travel: {self.travel}, I do cafe hoping : {self.cafe_hoping}')

a1 = Animal('Lion', 'Big', 'Brown')
h1 = Human('full', 'yes', 'yes')

a1.info()
h1.info()

