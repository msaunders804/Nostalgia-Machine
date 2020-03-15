import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class cube(object):
    rows = 0
    w = 0

    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass

class snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass

def drawGrid(w, rows, surface):
    #need to figure out how big each of the lines is going to be.
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w)) #surface, color(255, 255, 255), start position of the line, end position of the line
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

def redrawWindow(surface):
    global rows, width
    surface.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomSnack(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    global width, rows
    width = 500
    height = 500
    rows = 20 #this divides this board up into rows. make this smaller to maake it harder. must divide 500 evenly
    win = pygame.display.set_mode((width, height))
    s = snake((255, 0, 0), (10, 10)) #255 is the color red
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50) #this will delay 50 milliseconds so it doesnt run too fast. the lower this goes, the faster its going to be.
        clock.tick(10) #this makes sure that the game does not run at more than 10 games per second. if this is too low, then it will go too fast. may vay by machine. the lower this goes, is the slower its going to be
        redrawWindow(win)

rows = 20
w = 500
h = 500

cube.rows = rows
cube.w = w
if __name__ == "__main__":
    main()