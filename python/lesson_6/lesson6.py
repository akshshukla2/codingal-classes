import turtle

turtle.Screen().bgcolor("orange")

sc = turtle.Screen()

sc.setup(400, 300)

turtle.title("Welcome to Akshita's Turtle world")

board = turtle.Turtle()

for i in range(4):
     board.forward(100)
     board.left(90)

turtle.done()