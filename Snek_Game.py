# matthew aparte
# mpa18n

import random
import pygame
from PIL import Image


global s, food
IMAGE = 'MyMosaic.jpg' # put image name here. NOTE: must be .jpg
IM = Image.open(IMAGE)
resize = (800, 800)

fn = 'NEW_BG'
fext = '.jpg'
IM.thumbnail(resize)
IM.save('{}{}'.format(fn, fext))

image = 'NEW_BG.jpg'
im = Image.open(image)

w, h = im.size
ww = 20 - (w % 20)
hh = 20 - (h % 20)
w = w + ww
h = h + hh

xborder = w - 20
yborder = h - 20
xrows = int(xborder / 20)
yrows = int(yborder / 20)
C = 255


class cube(object):
    def __init__(self, start, X_Dir=1, Y_Dir=0, color=(0, 255, 0)):
        self.position = start
        self.X_Dir = 1
        self.Y_Dir = 0
        self.color = color

    def move(self, X_Dir, Y_Dir):
        self.X_Dir = X_Dir
        self.Y_Dir = Y_Dir
        self.position = (self.position[0] + self.X_Dir, self.position[1] + self.Y_Dir)

    def draw(self, surface):
        #global C
        disx = xborder // xrows
        disy = yborder // yrows
        i = self.position[0]
        j = self.position[1]
        #C = C - 20
        #shade = (0, C, 0)
        pygame.draw.rect(surface, self.color, (i * disx + 1, j * disy + 1, disx - 2, disy - 2))


class snake(object):
    body = []
    turns = {}

    def __init__(self, color, position):
        self.color = color
        self.head = cube(position)
        self.body.append(self.head)
        self.X_Dir = 0
        self.Y_Dir = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.X_Dir = -1
                    self.Y_Dir = 0
                    self.turns[self.head.position[:]] = [self.X_Dir, self.Y_Dir]

                elif keys[pygame.K_RIGHT]:
                    self.X_Dir = 1
                    self.Y_Dir = 0
                    self.turns[self.head.position[:]] = [self.X_Dir, self.Y_Dir]

                elif keys[pygame.K_UP]:
                    self.X_Dir = 0
                    self.Y_Dir = -1
                    self.turns[self.head.position[:]] = [self.X_Dir, self.Y_Dir]

                elif keys[pygame.K_DOWN]:
                    self.X_Dir = 0
                    self.Y_Dir = 1
                    self.turns[self.head.position[:]] = [self.X_Dir, self.Y_Dir]

        for i, c in enumerate(self.body):
            p = c.position[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.X_Dir == -1 and c.position[0] <= 0:
                    c.position = (xrows - 1, c.position[1])
                elif c.X_Dir == 1 and c.position[0] >= xrows - 1:
                    c.position = (0, c.position[1])
                elif c.Y_Dir == 1 and c.position[1] >= yrows - 1:
                    c.position = (c.position[0], 0)
                elif c.Y_Dir == -1 and c.position[1] <= 0:
                    c.position = (c.position[0], yrows - 1)
                else:
                    c.move(c.X_Dir, c.Y_Dir)

    def reset(self, position):
        self.head = cube(position)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.X_Dir = 0
        self.Y_Dir = 1

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.X_Dir, tail.Y_Dir
        global C
        C = C - 20
        shade = (0, C, 0)
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.position[0] - 1, tail.position[1]), shade))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.position[0] + 1, tail.position[1]), shade))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.position[0], tail.position[1] - 1), shade))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.position[0], tail.position[1] + 1), shade))

        self.body[-1].X_Dir = dx
        self.body[-1].Y_Dir = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            c.draw(surface)

def redrawWindow(surface):
    global s, food
    background = pygame.image.load(image)
    surface.blit(background, (0, 0))
    s.draw(surface)
    food.draw(surface)
    pygame.display.update()


def randomfood(xrows, yrows, item):
    position = item.body

    while True:
        x = random.randrange(xrows)
        y = random.randrange(yrows)
        if len(list(filter(lambda z: z.position == (x, y), position))) > 0:
            continue
        else:
            break

    return (x, y)


if __name__ != "__main__":
    win = pygame.display.set_mode((xborder, yborder))
    s = snake((255, 0, 0), (10, 10))
    food = cube(randomfood(xrows, yrows, s), color=(255, 0, 0))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(40)
        clock.tick(20)
        s.move()
        if s.body[0].position == food.position:
            s.addCube()
            food = cube(randomfood(xrows, yrows, s), color=(255, 0, 0))

        for x in range(len(s.body)):
            if s.body[x].position in list(map(lambda z: z.position, s.body[x + 1:])):
                #raise SystemExit
                pygame.quit()
        redrawWindow(win)


# references
# https://www.youtube.com/watch?v=5tvER0MT14s
# https://www.youtube.com/watch?v=6Qs3wObeWwc
# https://www.youtube.com/watch?v=cWHW9MnX_F4
