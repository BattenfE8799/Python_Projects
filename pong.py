# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 19:00:24 2023

@author: Elizabeth
Pong
"""
import turtle
#making screen
wn = turtle.Screen()
wn.title("Pong by @TokyoEdTeach")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#add ball and paddles to screen
#paddle A
paddle_a = turtle.Turtle()
#spped of animation, set to max
paddle_a.speed(0)
#gives it shape
paddle_a.shape("square")
#lengthening the shape
paddle_a.shapesize(stretch_wid=5,stretch_len=1)

paddle_a.color("white")

paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b = turtle.Turtle()
#spped of animation, set to max
paddle_b.speed(0)
#gives it shape
paddle_b.shape("square")
#lengthening the shape
paddle_b.shapesize(stretch_wid=5,stretch_len=1)

paddle_b.color("white")

paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
#spped of animation, set to max
ball.speed(0)
#gives it shape
ball.shape("circle")
ball.color("white")

ball.penup()
ball.goto(0,0)


#functions
def paddle_a_up():
#returns the y corrdinate
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
#keyboard binding


    


#main game loop
while True:
    wn.update()
    
