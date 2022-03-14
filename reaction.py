import pygame
import sys
from time import time
from random import choice

pygame.init()

display_width = 300
display_height = 300
display = pygame.display.set_mode((display_width,display_height))

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)

color_list = [green,blue,red]

def terminate():
    pygame.quit()
    sys.exit()

def display_text(text, size, x, y, color):
    font = pygame.font.SysFont('freesansbold.ttf', size, False)
    msg = font.render(str(text), False, color)
    display.blit(msg, (x, y))

def main():
    color = black
    lock = True
    while True:
        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        x = pygame.time.get_ticks()
        display.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
        pygame.draw.rect(display,color,(100,100,50,50))
        if int((x)/1000) == 3 and lock == True:
            color = choice(color_list)
            lock = False
            z = time()
            
        if lock == False and pos[0] in range(100,150) and pos[1] in range(100,150) and click[0] == 1:
            a = time()
            print("Reaction time:"+str(round((a-z),3))+" seconds")
            break

        pygame.display.update()


main()
