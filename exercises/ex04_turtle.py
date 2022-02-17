"""Exercise 04 - Rocketship with Turtle."""

__author__ = "730382185"

from turtle import Turtle, done 


def main() -> None:
    """The entrypoint of my scene."""
    my_turtle: Turtle = Turtle()
    my_turtle.speed(50)
    draw_up_triangle(my_turtle, -150, -150, 150, "red")
    draw_up_triangle(my_turtle, 0, -150, 150, "red")
    # Draw Fins
    draw_rectangle(my_turtle, -75, 150, 300, 150, "grey")
    # Draw Rocket Body
    draw_up_triangle(my_turtle, -75, 150, 150, "red")
    # Draw Nose Cone
    draw_pentagon(my_turtle, -25, 25, 50, "blue")
    # Draw Window
    draw_down_triangle(my_turtle, -60, -150, 120, "yellow")
    draw_down_triangle(my_turtle, -45, -200, 90, "orange")
    draw_down_triangle(my_turtle, -30, -250, 60, "red")
    # Draw Flames
    i = 50
    while i < 200:
        draw_star(my_turtle, i - 300, i + 100, 50, "black")
        draw_star(my_turtle, i + 150, i - 200, 50, "black")
        i = i + 50
    # Draw Stars
    done()


# TODO: Define the procedures for other components in your scene here.
def draw_rectangle(a_turtle: Turtle, x: float, y: float, length: float, width: float, color: str) -> None:
    """For Drawing Rectangles."""
    a_turtle.color(color)
    a_turtle.begin_fill()
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 2:
        a_turtle.forward(width)
        a_turtle.right(90)
        a_turtle.forward(length)
        a_turtle.right(90)
        i = i + 1
    a_turtle.end_fill()


def draw_down_triangle(a_turtle: Turtle, x: float, y: float, size: float, color: str) -> None:
    """For Drawing Down-Facing Triangles."""
    a_turtle.color(color)
    a_turtle.begin_fill()
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 3:
        a_turtle.forward(size)
        a_turtle.right(120)
        i = i + 1
    a_turtle.end_fill()


def draw_up_triangle(a_turtle: Turtle, x: float, y: float, size: float, color: str) -> None:
    """For Drawing Up-Facing Triangles."""
    a_turtle.color(color)
    a_turtle.begin_fill()
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 3:
        a_turtle.forward(size)
        a_turtle.left(120)
        i = i + 1
    a_turtle.end_fill()


def draw_pentagon(a_turtle: Turtle, x: float, y: float, size: float, color: str) -> None:
    """For Drawing Pentagons."""
    a_turtle.color(color)
    a_turtle.begin_fill()
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 5:
        a_turtle.forward(size)
        a_turtle.left(72)
        i = i + 1
    a_turtle.end_fill()


def draw_star(a_turtle: Turtle, x: float, y: float, size: float, color: str) -> None:
    """For Drawing Stars."""
    a_turtle.color(color)
    a_turtle.begin_fill()
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 5:
        a_turtle.forward(size)
        a_turtle.right(144)
        i = i + 1
    a_turtle.end_fill()


if __name__ == "__main__":
    main()