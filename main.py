import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("orange")
drawing_board.title("interactive drawing board")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.right(45)
def sola():
    turtle_instance.left(45)
def düz():
    turtle_instance.forward(100)

def clear_screen():
    turtle_instance.clear()

def return_home():
    turtle_instance.home()
def pen_up():
    turtle_instance.penup()
def pen_down():
    turtle_instance.pendown()


drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="d")
drawing_board.onkey(fun=sola,key="a")
drawing_board.onkey(fun=düz,key="w")
drawing_board.onkey(fun=clear_screen,key="c")
drawing_board.onkey(fun=return_home,key="h")
drawing_board.onkey(fun=pen_up,key="e")
drawing_board.onkey(fun=pen_down,key="q")
turtle.mainloop()