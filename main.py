import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("orange")
drawing_board.title("interactive drawing board")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.right(90)
    turtle_instance.forward(100)
def sola():
    turtle_instance.left(90)
    turtle_instance.forward(100)
def düz():
    turtle_instance.forward(100)
def ters():
    turtle_instance.left()
    turtle_instance.forward(100)


drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="d")
drawing_board.onkey(fun=sola,key="a")
drawing_board.onkey(fun=düz,key="w")
drawing_board.onkey(fun=ters,key="s")

turtle.mainloop()