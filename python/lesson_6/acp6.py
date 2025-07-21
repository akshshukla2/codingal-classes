import turtle

turtle.Screen().bgcolor("aqua")
# for teacher : i have also done equilateral triangle but that is in "acp6pt2.py" folder because i dont know how to do it in one.
sc = turtle.Screen()

sc.setup(500, 500)

turtle.title("TURTLE HEXAGON")

board = turtle.Turtle()
#hexagon
for i in range(7):
     board.forward(100)
     board.left(60)


turtle.done()

