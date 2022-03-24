import turtle
import basic_turtle_setup
import turtle_file_handler


basic_turtle_setup.setup_turtle(500, 500, "Build Squares")

# turtle.goto(100, 0)
# turtle.goto(100, 100)
# turtle.goto(0, 100)
# turtle.goto(0, 0)

# square_positions_list = [[100, 0], [100, 100], [0, 100], [0, 0]]


def draw_part(positions_list, colour, start_position):

    turtle.penup()
    turtle.goto(start_position[0], start_position[1])
    turtle.pendown()

    turtle.color(colour)
    turtle.begin_fill()

    for position in positions_list:
        turtle.goto(position[0] + start_position[0],
                    position[1] + start_position[1])

    turtle.end_fill()


square_positions_list = turtle_file_handler.GetPositionsFromFile(
    "square_positions.txt")

draw_part(square_positions_list, "blue", [125, -50])
draw_part(square_positions_list, "pink", [-100, 50])

basic_turtle_setup.finish_turtle()
