import turtle

turtle.Screen().bgcolor("aqua")

sc = turtle.Screen()

sc.setup(500, 500)

turtle.title("TURTLE HEXAGON")

board = turtle.Turtle()
#hexagon
for i in range(7):
     board.forward(100)
     board.left(60)


turtle.done()

