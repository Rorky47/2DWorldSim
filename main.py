import pygame, time, sys
from scripts.globals import *
from scripts.terrain import *
from scripts.Map_render import *


import numpy as np


pygame.init()
Runing = True
Sec, Frame, FPS = 0, 0 , 0

terrain = Map_Render.load_Map("world.map")

WHITE = (255, 255, 255)


def fps():
    global Sec, Frame, FPS

    if Sec == time.strftime("%S"):
        Frame += 1
    else:
        FPS = Frame
        Frame = 0
        Sec = time.strftime("%S")
def Render_Window():
    global window, Window_H, Window_W, window_title
    Window_W, Window_H = 800, 650
    window_title = "God Sim"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((Window_W, Window_H), pygame.HWSURFACE|pygame.DOUBLEBUF)


Render_Window()

while Runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Runing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Globals.cam_move = 1
            elif event.key == pygame.K_s:
                Globals.cam_move = -1
            elif event.key == pygame.K_d:
                Globals.cam_move = 2
            elif event.key == pygame.K_a:
                Globals.cam_move = -2
        elif event.type == pygame.KEYUP:
            Globals.cam_move=0


    if event.type == pygame.KEYDOWN:
        if Globals.cam_move == 1:
            Globals.cam_y +=1
        elif Globals.cam_move == -1:
            Globals.cam_y -=1
        elif Globals.cam_move == 2:
            Globals.cam_x -=1
        elif Globals.cam_move == -2:
            Globals.cam_x +=1

    window.fill(WHITE)
    print(FPS)

    window.blit(terrain, (Globals.cam_x, Globals.cam_y))

    fps()
    pygame.display.update()

pygame.quit()
quit()
