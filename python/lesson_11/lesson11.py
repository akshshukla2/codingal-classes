class fruit:
    def __init__(self,colour,weight,size):
        self.colour = colour
        self.weight = weight
        self.size = size

    def desc(self):
        print(f"The colour of the fruit is", {self.colour})

class apple(fruit):
    def __init__(self,colour,weight,size,price,popularity):
       # fruit.__init__(self,colour,weight,size)
       super().__init__(colour,weight,size)
       self.price = price
       self.popularity = popularity

o1 = apple('red','2.5','small', 20, 'very')

o1.desc()
print(o1.colour)
print(o1.price)
print(o1.weight)
print(o1.popularity)

