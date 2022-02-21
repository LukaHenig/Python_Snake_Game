#############################################################
#Date: 21.02.22                                             #
#Programmed by: Luka Henig (luka.henig@gmail.com)           #
#Curse: 100 Days of Code(udemy)                             #
#Description: Litle snake game to learn and understand      #
#python directories, files and paths                        #
#############################################################

#imports
from turtle import Turtle

#constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """creates the starting snake with 3 segments, no parameters"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """add a new segment to the snake, at the given position"""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """extend the snake by one segment at the end, no parameters"""
        self.add_segment(self.segments[-1].position())

    def reset(self):
        """resets the snake to 3 segments and back to the starting point, no parameters"""
        for seg in self.segments:
            seg.goto(1000, 1000)    #move old snake out of screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        """moves snake elements starting by the end to the next segment position and head by one distance forward, no parameters"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """set direction of the head segment up, no parameters"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """set direction of the head segment down, no parameters"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """set direction of the head segment left, no parameters"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """set direction of the head segment right, no parameters"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
