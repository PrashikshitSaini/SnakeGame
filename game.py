from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # set according to the dimension of the project
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):

        self.segments = []  # each block of the snake is called segment
        self.create_snake() # to call the snake the function and to make it
        self.head = self.segments[0]

    def add_segment(self, position):  # adds a segment to a new coordinate
        tim = Turtle("square")
        tim.color('white')
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)

    def reset(self):
        for seg in self.segments:
             seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

          #  Add a anew segment to the snake



    def create_snake(self):  # only used to create snake and call it on the initial position
        for position in STARTING_POSITION:
            self.add_segment(position)


    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):  # start=2 stop=0 step=-1
            new_x = self.segments[seg_num - 1].xcor()  # seg_num is the range of the segment and
            new_y = self.segments[seg_num - 1].ycor()  # new_x or _y represents the one less coordinate to shift
            self.segments[seg_num].goto(new_x, new_y) # all the segment individually will shift to the new coordinates
        self.head.forward(MOVE_DISTANCE) # all the segments will move together the given distance

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
