import turtle
import basic_turtle_setup
import turtle_file_handler


basic_turtle_setup.setup_turtle(500, 500, "Mr Fox")


def draw_part(positions_list, colour, start_position):

    turtle.penup()
    # turtle.goto(start_position[0], start_position[1])
    turtle.pendown()

    turtle.color(colour)
    turtle.begin_fill()

    for position in positions_list:
        turtle.goto(position[0] + start_position[0],
                    position[1] + start_position[1])

    turtle.end_fill()


# Setup variables:
start_postion = [-250, 250]
background_colour = "#EBC94A"
body_colour = "#7A7E77"
nose_colour = "#161714"

# draw the body
body_positions = turtle_file_handler.GetPositionsFromFile("mr_fox_body.txt")
draw_part(body_positions, body_colour, start_postion)

# draw the nose
nose_positions = turtle_file_handler.GetPositionsFromFile("mr_fox_nose.txt")
draw_part(nose_positions, nose_colour, start_postion)

# draw eye:
turtle.penup()
eye_position = [115, 232]
turtle.goto(eye_position[0] + start_postion[0], -
            eye_position[1] + start_postion[1])
turtle.pendown()
turtle.begin_fill()
turtle.circle(3)
turtle.end_fill()
turtle.penup()

turtle.bgcolor(background_colour)


basic_turtle_setup.finish_turtle()
