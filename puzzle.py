import pygame
import sys
from random import choice, shuffle
pygame.init()

display_width = 200
display_height = 200
display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('15 Puzzle')

black = (0,  0,  0)
white = (155, 155, 155)
green = (0, 255,  0)
blue = (0,  0, 255)
red = (255,  0,  0)


class Block:
    def __init__(self, loadedList=None, index=None):
        if loadedList is None:
            self.rectList = [
                [0, 0], [50, 0], [100, 0], [150, 0],
                [0, 50], [50, 50], [100, 50], [150, 50],
                [0, 100], [50, 100], [100, 100], [150, 100],
                [0, 150], [50, 150], [100, 150],
            ]
            self.values = [1, 2, 3, 4, 5, 6, 7,
                           8, 9, 10, 11, 12, 13, 14, 15, 16]
            self.select = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            shuffle(self.select)
            self.emptyIndex = 15
            for i in range(15):
                number = choice(self.select)
                self.rectList[i].append(number)
                self.select.remove(number)
            self.rectList.append([150, 150, 16])
        else:
            self.rectList = loadedList
            self.values = [1, 2, 3, 4, 5, 6, 7,
                           8, 9, 10, 11, 12, 13, 14, 15, 16]
            self.emptyIndex = index

    def drawBlocks(self):
        for i in range(16):
            if self.rectList[i][2] != 16:
                pygame.draw.rect(
                    display, white, (self.rectList[i][0], self.rectList[i][1], 50, 50), 3)
                display_text(str(
                    self.rectList[i][2]), 30, self.rectList[i][0]+10, self.rectList[i][1]+10, white)
            else:
                pygame.draw.rect(
                    display, black, (self.rectList[i][0]+2, self.rectList[i][1]+2, 48, 48), 2)

    def move(self, action):
        if action == 'R':
            if self.emptyIndex % 4 != 0:
                temp = self.rectList[self.emptyIndex]
                self.rectList[self.emptyIndex] = self.rectList[self.emptyIndex-1]
                self.rectList[self.emptyIndex-1] = temp
                self.emptyIndex -= 1
                self.rectList[self.emptyIndex][0] -= 50
                self.rectList[self.emptyIndex+1][0] += 50
        if action == 'L':
            if self.emptyIndex not in [3, 7, 11, 15]:
                temp = self.rectList[self.emptyIndex]
                self.rectList[self.emptyIndex] = self.rectList[self.emptyIndex+1]
                self.rectList[self.emptyIndex+1] = temp
                self.emptyIndex += 1
                self.rectList[self.emptyIndex][0] += 50
                self.rectList[self.emptyIndex-1][0] -= 50

        if action == 'D':
            if self.emptyIndex not in [0, 1, 2, 3]:
                temp = self.rectList[self.emptyIndex]
                self.rectList[self.emptyIndex] = self.rectList[self.emptyIndex-4]
                self.rectList[self.emptyIndex-4] = temp
                self.emptyIndex -= 4
                self.rectList[self.emptyIndex][1] -= 50
                self.rectList[self.emptyIndex+4][1] += 50

        if action == 'U':
            if self.emptyIndex not in [12, 13, 14, 15]:
                temp = self.rectList[self.emptyIndex]
                self.rectList[self.emptyIndex] = self.rectList[self.emptyIndex+4]
                self.rectList[self.emptyIndex+4] = temp
                self.emptyIndex += 4
                self.rectList[self.emptyIndex][1] += 50
                self.rectList[self.emptyIndex-4][1] -= 50


class Button:
    def __init__(self, x, y, width, height, label, color1, color2, textcolor):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = str(label)
        self.color1 = color1
        self.color2 = color2
        self.textcolor = textcolor

    def drawButton(self, function):
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if pos[0] in range(self.x, self.x + self.width) and pos[1] in range(self.y, self.y + self.height):
            pygame.draw.rect(display, self.color1,
                             (self.x, self.y, self.width, self.height))
            if click[0] == 1:
                function()
        else:
            pygame.draw.rect(display, self.color2,
                             (self.x, self.y, self.width, self.height))
        display_text(self.label, 25, self.x + 5, self.y + 5, self.textcolor)


def display_text(text, size, x, y, color):
    font = pygame.font.SysFont('freesansbold.ttf', size, False)
    msg = font.render(str(text), False, color)
    display.blit(msg, (x, y))


def terminate():
    pygame.quit()
    sys.exit()


def stopExecution(text, action):
    while True:
        display.fill(black)
        display_text(str(text), 30, 50, 50, green)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
                if event.key == pygame.K_RETURN or pygame.K_SPACE:
                    if action == 'return':
                        return
                    else:
                        action()
        pygame.display.update()


def getlist():
    try:
        file = open('15Puzzle.txt', 'r')
        a = file.readlines()
        templist, xlist, rectlist = [], [], []
        x = ''
        m, i = 0, 0
        while i < len(a[0]):
            if a[0][i].isdigit():
                m = i
                try:
                    while a[0][m] != ',':
                        if a[0][m].isdigit():
                            xlist.append(a[0][m])
                        m += 1
                except IndexError:
                    pass
                i = m
                x = x.join(xlist)
                xlist.clear()
                templist.append(int(x))
                if len(templist) == 3:
                    rectlist.append([templist[0], templist[1], templist[2]])
                    templist.clear()
                x = ''
            i += 1
        for i in range(len(rectlist)):
            if rectlist[i][2] == 16:
                index = i
                break
        file.close()
        return [rectlist, index]
    except FileNotFoundError:
        return [None, None]


def load():
    x = getlist()
    main(x[0], x[1])
    del x


def save(rectList):
    file = open('15Puzzle.txt', 'w')
    file.writelines(str(rectList))
    file.close()


def start():
    button1 = Button(20, 150, 50, 30, 'New', green,
                     (0, 200, 0), (255, 255, 255))
    button2 = Button(120, 150, 50, 30, 'Load', blue,
                     (0, 0, 200), (255, 255, 255))
    while True:
        display.fill(black)
        display_text('15 Puzzle', 40, 45, 50, green)
        button1.drawButton(main)
        button2.drawButton(load)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
                if event.key == pygame.K_RETURN or pygame.K_SPACE:
                    main()
        pygame.display.update()


def main(loadedList=None, index=None):
    block = Block(loadedList, index)
    notBreak = False
    pygame.mouse.set_visible(False)
    while True:
        for event in pygame.event.get():
            for i in range(len(block.rectList)):
                if block.rectList[i][2] == block.values[i]:
                    notBreak = True
                    continue
                else:
                    notBreak = False
                    break
                if notBreak is True:
                    stopExecution('Complete', main)
            display.fill(black)
            block.drawBlocks()
            if event.type == pygame.QUIT:
                save(block.rectList)
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    stopExecution('Pause', 'return')
                if event.key == pygame.K_ESCAPE:
                    save(block.rectList)
                    terminate()
                if event.key == pygame.K_RIGHT:
                    block.move('R')
                if event.key == pygame.K_LEFT:
                    block.move('L')
                if event.key == pygame.K_UP:
                    block.move('U')
                if event.key == pygame.K_DOWN:
                    block.move('D')
                if event.key == pygame.K_n:

                    main()
        pygame.display.update()


start()
