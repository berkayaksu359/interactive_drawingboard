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
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="d")
drawing_board.onkey(fun=sola,key="a")
drawing_board.onkey(fun=düz,key="w")
drawing_board.onkey(fun=clear_screen,key="c")
drawing_board.onkey(fun=return_home,key="h")
turtle.mainloop()