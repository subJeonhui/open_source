import pygame
import random

path = "./src/Coins/"


def transformImage(image, scale, rotate):  # 이미지 변화 함수
    transScale = pygame.transform.scale(image, scale)
    return pygame.transform.rotate(transScale, rotate)

ImgCnt = 8
giftImage = [transformImage(pygame.image.load(path + 'coin_0'+str(i)+'.png'), (30, 30), 0) for i in range(1,ImgCnt+1)]
bomb_rotate = [0, 0, 0, 0]

gifts = []  #
getGifts = []  #
global SCREEN_WIDTH
global SCREEN_HEIGHT


def createGift(width, height):
    posX = random.randint(0, width - 30)  # 떨어질 X좌표
    posY = random.randint(50, height - 30)  # 떨어질 Y좌표
    rect = pygame.Rect(giftImage[0].get_rect())
    rect.top = posY
    rect.left = posX
    scale = 50
    return {'rect': rect, 'x': posX - 10, 'y': posY - 10, 'scale': scale, 'hit': False, 'cnt': 0}


def addGift():
    gifts.append(createGift(SCREEN_WIDTH, SCREEN_HEIGHT))


def init(width, height):
    global gifts
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    SCREEN_WIDTH = width
    SCREEN_HEIGHT = height
    gifts = []


def run(screen):
    global SCREEN_WIDTH
    global SCREEN_HEIGHT

    for g in gifts:
        g['cnt'] += 1
        if g['cnt'] >= 300:
            gifts.remove(g)

    for g in gifts:
        screen.blit(giftImage[(g['cnt']//2) % len(giftImage)], g['rect'])


def display(screen):
    for g in gifts:
        screen.blit(giftImage[(g['cnt']//2) % len(giftImage)], g['rect'])
