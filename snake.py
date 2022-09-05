from turtle import Turtle

MOVE_DISTANCE = 20
HEADING_POSITIONS = {
    "right": 0,
    "up": 90,
    "left": 180,
    "down": 270
}


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for i in range(3):
            new_snake_segment = Turtle(shape="square")
            new_snake_segment.penup()
            new_snake_segment.color("white")
            new_snake_segment.back(i * 20)
            self.snake_segments.append(new_snake_segment)

    def shift_body(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != HEADING_POSITIONS["left"]:
            self.head.setheading(HEADING_POSITIONS["right"])

    def up(self):
        if self.head.heading() != HEADING_POSITIONS["down"]:
            self.head.setheading(HEADING_POSITIONS["up"])

    def left(self):
        if self.head.heading() != HEADING_POSITIONS["right"]:
            self.head.setheading(HEADING_POSITIONS["left"])

    def down(self):
        if self.head.heading() != HEADING_POSITIONS["up"]:
            self.head.setheading(HEADING_POSITIONS["down"])
