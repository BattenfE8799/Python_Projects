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
paddle_a.color("white")

paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B


#Ball

#main game loop
while True:
    wn.update()
    
