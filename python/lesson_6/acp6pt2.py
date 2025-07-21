import turtle

turtle.Screen().bgcolor("pink")

sc = turtle.Screen()

sc.setup(500, 600)

turtle.title("TURTLE TRIANGLE")

board = turtle.Turtle()
#EQUILATORAL TRIANGLE
for i in range(4):
     board.forward(150)
     board.left(120)


turtle.done()
