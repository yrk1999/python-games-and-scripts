##    X = 1        ##
##    0 = 0        ##
##    Default = X  ##

import pygame
from sys import exit

pygame.init()

display_width = 302
display_height = 350

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Tic Tac Toe')
class Box:
    def __init__(self):
        self.box = [['', 50, 50], ['', 150, 50], ['', 250, 50],
                    ['', 50, 150], ['', 150, 150], ['', 250, 150],
                    ['', 50, 250], ['', 150, 250], ['', 250, 250],
                    ]
        self.lastPlayed = '0'
        self.moveCount = 0

    def change(self, index):
        if self.box[index][0] == '':
            if self.lastPlayed == '0':
                self.box[index][0] = 'X'
                self.lastPlayed = 'X'
                self.moveCount += 1
            elif self.lastPlayed == 'X':
                self.box[index][0] = '0'
                self.lastPlayed = '0'
                self.moveCount += 1

    def draw(self):
        for i in range(len(self.box)):
            if self.box[i][0] == 'X':
                pygame.draw.circle(
                    display, red, (self.box[i][1], self.box[i][2]), 20)
            elif self.box[i][0] == '0':
                pygame.draw.circle(
                    display, blue, (self.box[i][1], self.box[i][2]), 20)

    def match(self):
        # Top left to top right
        if [self.box[0][0], self.box[1][0], self.box[2][0]] == ['X', 'X', 'X']:
            return self.box[0][0]

        if [self.box[0][0], self.box[1][0], self.box[2][0]] == ['0', '0', '0']:
            return self.box[0][0]

        # Top left to bottom left
        if [self.box[0][0], self.box[3][0], self.box[6][0]] == ['X', 'X', 'X']:
            return self.box[0][0]

        if [self.box[0][0], self.box[3][0], self.box[6][0]] == ['0', '0', '0']:
            return self.box[0][0]

        # Bottom left to Bottom right
        if [self.box[6][0], self.box[7][0], self.box[8][0]] == ['X', 'X', 'X']:
            return self.box[6][0]

        if [self.box[6][0], self.box[7][0], self.box[8][0]] == ['0', '0', '0']:
            return self.box[6][0]

        # Top right to bottom right
        if [self.box[2][0], self.box[5][0], self.box[8][0]] == ['X', 'X', 'X']:
            return self.box[2][0]

        if [self.box[2][0], self.box[5][0], self.box[8][0]] == ['0', '0', '0']:
            return self.box[2][0]

        # Top left to bottom left(Diagonal)
        if [self.box[0][0], self.box[4][0], self.box[8][0]] == ['X', 'X', 'X']:
            return self.box[0][0]

        if [self.box[0][0], self.box[4][0], self.box[8][0]] == ['0', '0', '0']:
            return self.box[0][0]

        # Top right to bottom left
        if [self.box[2][0], self.box[4][0], self.box[6][0]] == ['X', 'X', 'X']:
            return self.box[2][0]

        if [self.box[2][0], self.box[4][0], self.box[6][0]] == ['0', '0', '0']:
            return self.box[2][0]

        # Middle row top to bottom
        if [self.box[1][0], self.box[4][0], self.box[7][0]] == ['X', 'X', 'X']:
            return self.box[1][0]

        if [self.box[1][0], self.box[4][0], self.box[7][0]] == ['0', '0', '0']:
            return self.box[1][0]

        # Middle row left to right
        if [self.box[3][0], self.box[4][0], self.box[5][0]] == ['X', 'X', 'X']:
            return self.box[3][0]

        if [self.box[3][0], self.box[4][0], self.box[5][0]] == ['0', '0', '0']:
            return self.box[3][0]


def draw_grid():
    for x in range(0, 400, 100):
        pygame.draw.line(display, white, (x, 0), (x, 300))

    for y in range(0, 400, 100):
        pygame.draw.line(display, white, (0, y), (300, y))


def terminate():
    pygame.quit()
    exit()


def display_text(text, size, x, y, color):
    font = pygame.font.SysFont('freesansbold.ttf', size, False)
    msg = font.render(str(text), False, color)
    display.blit(msg, (x, y))


def change(box, number, pos):
    if pos[0] in range(0, 100):
        box.change(number)

    if pos[0] in range(100, 200):
        box.change(number+1)

    if pos[0] in range(200, 300):
        box.change(number+2)


def main():
    box = Box()
    over = False
    disable = False
    while True:
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        display.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
                if over == True and event.key == pygame.K_RETURN:
                    main()
        if disable == False:
            if click[0] == 1:
                if pos[1] in range(0, 100):
                    change(box, 0, pos)

                if pos[1] in range(100, 200):
                    change(box, 3, pos)

                if pos[1] in range(200, 300):
                    change(box, 6, pos)

        draw_grid()
        box.draw()
        if box.moveCount == 9:
            display_text("Draw! ", 30, 120, 310, (150, 150, 150))
            over = True
            disable = True
        else:
            winner = box.match()
            if winner != None:
                display_text(str(winner)+" wins", 30, 130, 310, green)
                over = True
                disable = True
        pygame.display.update()


main()
