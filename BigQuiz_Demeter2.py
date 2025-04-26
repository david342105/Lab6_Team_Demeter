
import pgzrun
import pygame
import pgzero
from pgzero.builtins import Actor
from random import randint
import smtplib
import ssl
from openpyxl import *
import time
from sys import exit
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 500, 165)
answer_box2 = Rect(0, 0, 500, 165)
answer_box3 = Rect(0, 0, 500, 165)
answer_box4 = Rect(0, 0, 500, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 15

q1 = ["Which ocean is the largest?",
      "Atlantic", "Indian", "Arctic", "Pacific", 4]

q2 = ["When is Christmas?", "December 24", "January 1", "December 25", "November 25", 3]

q3 = ["What is 8+5=?",
      "10", "11", "12", "13", 4]

q4 = ["What is the letter after D?",
      "F", "E", "B", "C", 2]

q5 = ["What is the tallest building in the world (as of 2025)?", 
      "Burj Khalifa", "Shanghai Tower", "Jeddah Tower", "One World Trade Center", 1]

q6 = ["What is a quarter of 200?", "50", "100", "25", "150", 1]

q7 = ["How many kilometers are there in one mile?",
      "1.2", "1.6", "1.5", "1.7", 2]

q8 = ["Which of the following is NOT a metric unit?", "meter", "mile", "Celcius", "kilogram", 2]

q9 = ["Which planet do we live on?", "Mars", "Earth", "Sun", "Moon", 2]

q10 = ["Which time we use in the summer?", "Daylight Saving", "Standard", "East", "Mountain", 1]

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
question = questions.pop(0)


def draw():
    screen.fill("light cyan")
    screen.draw.filled_rect(main_box, "light green")
    screen.draw.filled_rect(timer_box, "light cyan")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "light gray")
        screen.draw.textbox(str(time_left), timer_box, color=("black"))
        screen.draw.textbox(question[0], main_box, color=("black"))

    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("black"))
        index = index + 1


def game_over():
    global question, time_left
    message = "Game over. You got %s questions correct" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0


def correct_answer():
    global question, score, time_left

    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 15
    else:
        print("End of questions")
        game_over()


def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer " + str(index))
            if index == question[5]:
                print("You got it correct!")
                correct_answer()
            else:
                game_over()
        index = index + 1


def on_key_up(key):
    if key == keys.H:
        print("The correct answer is box number %s " % question[5])


def update_time_left():
    global time_left
    if time_left:
        time_left = time_left - 1
    else:
        game_over()


clock.schedule_interval(update_time_left, 1.0)
pgzrun.go()
