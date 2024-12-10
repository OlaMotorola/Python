import pygame
import time
import os
import random
from random import shuffle

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 50)

border = 300
W,H = 400,800
n_size = 40

win = pygame.display.set_mode((W+border,H))


# shapes-related stuff
green = pygame.image.load(os.path.join("assets", "green.png"))
pink = pygame.image.load(os.path.join("assets", "pink.png"))
blue = pygame.image.load(os.path.join("assets", "blue.png"))
red = pygame.image.load(os.path.join("assets", "red.png"))
yellow = pygame.image.load(os.path.join("assets", "yellow.png"))
tur = pygame.image.load(os.path.join("assets", "tur.png"))
orange = pygame.image.load(os.path.join("assets", "orange.png"))

S = pygame.image.load(os.path.join("assets", "green_1.png"))
T = pygame.image.load(os.path.join("assets", "pink_1.png"))
J = pygame.image.load(os.path.join("assets", "blue_1.png"))
Z = pygame.image.load(os.path.join("assets", "red_1.png"))
O = pygame.image.load(os.path.join("assets", "yellow_1.png"))
I = pygame.image.load(os.path.join("assets", "tur_1.png"))
L = pygame.image.load(os.path.join("assets", "orange_1.png"))

colors = {
    "L": (orange,L),
    "J": (blue,J),
    "S": (green,S),
    "Z": (red,Z),
    "T": (pink,T),
    "I": (tur,I),
    "O": (yellow,O)
}
def returnShape(r,c,sh):
    shapes = {
        "L": [
            [(r,c),(r,c-1),(r,c+1),(r-1,c+1)],
            [(r,c),(r-1,c),(r+1,c),(r+1,c+1)],
            [(r,c),(r,c+1),(r,c-1),(r+1,c-1)],
            [(r,c),(r-1,c),(r+1,c),(r-1,c-1)]
        ],
        "J": [
            [(r,c),(r,c+1),(r,c-1),(r-1,c-1)],
            [(r,c),(r-1,c+1),(r-1,c),(r+1,c)],
            [(r,c),(r,c+1),(r,c-1),(r+1,c+1)],
            [(r,c),(r+1,c),(r-1,c),(r+1,c-1)]
        ],
        "S": [
            [(r,c),(r,c-1),(r-1,c),(r-1,c+1)],
            [(r,c),(r-1,c),(r,c+1),(r+1,c+1)]
        ],
        "O": [
            [(r,c),(r,c-1),(r-1,c-1),(r-1,c)]
        ],
        "I": [
            [(r,c),(r,c+1),(r,c+2),(r,c-1)],
            [(r,c+1),(r-1,c+1),(r+1,c+1),(r+2,c+1)],
            [(r+1,c),(r+1,c+1),(r+1,c+2),(r+1,c-1)],
            [(r,c),(r+1,c),(r+2,c),(r-1,c)]
        ],
        "Z": [
            [(r,c),(r,c+1),(r-1,c-1),(r-1,c)],
            [(r,c),(r-1,c),(r,c-1),(r+1,c-1)]
        ],
        "T": [
            [(r,c),(r,c+1),(r,c-1),(r-1,c)],
            [(r,c),(r-1,c),(r+1,c),(r,c+1)],
            [(r,c),(r,c+1),(r,c-1),(r+1,c)],
            [(r,c),(r,c-1),(r+1,c),(r-1,c)]
        ]
    }
    return shapes[sh]
board = [
    [0,0,0,0,0,0,0,0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

class Shape:
    def __init__(self,shape):
        self.shape = shape
        self.r = 1  #center row
        self.c = 5  #center column
        self.rotation = 0
        self.obj = self.getShape()
        self.stop = False

    def move(self):
        self.r+=1
        self.obj = self.getShape()

    def getShape(self):
        return returnShape(self.r,self.c,self.shape)

    def getPos(self):
        if self.shape == "0":
            return self.obj[0]
        else:
            return self.obj[self.rotation % len(self.obj)]

    def rotate(self):
        self.rotation += 1
        self.obj = self.getShape()
        self.obj = self.repairRotationBoarders()
        self.obj = self.checkIfShapesCover()

    def checkIfShapesCover(self):
        row = 0
        for i in self.getPos():
            r,c=i[0],i[1]
            if board[r][c]!=0:
                row+=1
        self.r -=row
        return self.getShape()

    def repairRotationBoarders(self):
        row, col = 0, 0
        for i in self.getPos():
            r, c = i[0], i[1]
            if r >= 20 and r > row:
                row = r
            if c >= 9 and c > col:
                col = c
            if c < 0:
                col = c
        if row > 0:
            self.r = self.r - (row - 19)
        if col > 0:
            self.c = self.c - (col - 9)
        elif col < 0:
            self.c += abs(col)
        return self.getShape()

    def draw(self):
        for i in self.getPos():
            win.blit(colors[self.shape][0], (n_size*i[1],n_size*i[0]))

    def check(self):
        moved = False

        # check if there is a shape in next row
        for i in self.getPos():
            r,c = i[0], i[1]
            if r+1==20:
                self.stop = True
            elif r<19:
                if board[r+1][c]!=0:
                    self.stop = True

        # move shape
        if not moved and not self.stop:
            self.move()

            moved = True

        # if stopped, update board
        if self.stop:
            for i in self.getPos():
                r, c = i[0], i[1]
                board[r][c] = self.shape


    def validRight(self):
        for i in self.getPos():
            r,c=  i[0],i[1]
            if c+1>9 or board[r][c+1]!=0:
                return False
        return True

    def validLeft(self):
        for i in self.getPos():
            r,c=  i[0],i[1]
            if c-1<0 or board[r][c-1]!=0:
                return False
        return True

def checkBoard(score):
    for i in range(0,20):
        if 0 not in board[i]:
            board.remove(board[i])
            board.insert(0,[0,0,0,0,0,0,0,0,0,0])
            score +=100
    return score


def drawGrid():
    for i in range(1,10):
        pygame.draw.line(win, (30,30,30), (n_size*i,0), (n_size*i,H))
    for i in range(1,20):
        pygame.draw.line(win, (30,30,30), (0, n_size * i), (W, n_size * i))
    pygame.draw.line(win, (30,30,30), (W,0),(W,H),3)


def drawBoard():
    for row in range(0,20):
        for col in range(0,10):
            if board[row][col] !=0:
                win.blit(colors[board[row][col]][0], (n_size*col,n_size*row))

def draw(shape,score):
    win.fill((0,0,0))
    drawGrid()
    shape.draw()
    drawBoard()

    font1 = pygame.font.SysFont('Comic Sans MS', 30)
    next = font1.render('Next shape:', False, (255,255,255))
    score = font1.render(f'Score:{score}', False, (255,255,255))
    win.blit(score, (W+60, 20))
    win.blit(next, (W+60, H//2-100))

def checkIfLost(shape):
    for el in board[1]:
        if el!=0:
            return True
    return False

def randomize(arr):
    res = []
    for _ in range(len(arr)):
        c = random.choice(arr)
        res.append(c)
        arr.remove(c)
    return res


def main():
    run = True
    clock = pygame.time.Clock()
    arr = ["S","L","J","I","Z","O","T"]
    arr = randomize(arr)
    nextarr= arr
    shuffle(nextarr)
    shuffle(arr)
    i=1
    shape = Shape(arr[0])
    delta = 0.5
    start = time.time()
    score = 0

    paused = False

    while run:
        clock.tick(60)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    shape.rotate()
                if event.key == pygame.K_RIGHT and shape.validRight():
                    shape.c += 1
                    shape.obj=shape.getShape()
                if event.key == pygame.K_LEFT and shape.validLeft():
                    shape.c -= 1
                    shape.obj=shape.getShape()
                if event.key == pygame.K_SPACE:
                    paused = not paused
                if event.key == pygame.K_r and checkIfLost(shape):
                    for i in range(len(board)):
                        for j in range(len(board[0])):
                            board[i][j] = 0
                    score = 0
                    arr = ["S","L","J","I","Z","O","T"]
                    shape = Shape(arr[0])
                    i = 1

        if paused:
            paus = font.render("Paused", False, (255,255,255))
            win.blit(paus, ((W+border)//2-paus.get_width()//2, H//2-paus.get_height()//2))
            pygame.display.update()
            continue

        # move object
        if time.time()>=start+delta:
            shape.check()
            start = time.time()
            score = checkBoard(score)
            if keys[pygame.K_DOWN]:
                score +=1
        if keys[pygame.K_DOWN]:
            delta = 0.05
        else:   delta = 1


        if not checkIfLost(shape):
            draw(shape,score)

        if i < 7:
            win.blit(colors[arr[i]][1], (W+100, H//2-20))
        else:
            win.blit(colors[nextarr[0]][1], (W+100, H//2-20))

        # change shape if stopped
        if shape.stop == True:
            shape = Shape(arr[i])
            i += 1
            if i==len(arr):
                arr= nextarr
                shuffle(nextarr)
                i=0

        if checkIfLost(shape):
            lost = font.render('Lost!', False, (255,255,255))
            win.blit(lost, ((W+border)//2-lost.get_width()//2, H//2-lost.get_height()//2))

        pygame.display.update()

main()