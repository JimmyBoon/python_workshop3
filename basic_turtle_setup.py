import turtle


def setup_turtle(width, height, title):
    turtle.setup(width, height)
    turtle_window = turtle.Screen()
    turtle_window.title(title)


def finish_turtle():
    turtle.hideturtle()
    turtle.mainloop()
    turtle.done()
