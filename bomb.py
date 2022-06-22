import pygame
import random

path = "./src/"

bomb_image = pygame.image.load('./src/bomb.png')
bomb_shadow = pygame.image.load('./src/bomb_shadow.png')
bomb_rotate = [0, 0, 0, 0]

bombs = []  # 폭탄들을 저장할 변수
explosion = []  # 폭파 지점
global SCREEN_WIDTH
global SCREEN_HEIGHT


def transformImage(image, scale, rotate):  # 이미지 변화 함수
    transScale = pygame.transform.scale(image, scale)
    return pygame.transform.rotate(transScale, rotate)


def createBomb(width, height):
    posX = random.randint(0, width)  # 떨어질 X좌표
    posY = random.randint(50, height)  # 떨어질 Y좌표
    rect = pygame.Rect(bomb_image.get_rect())
    rect.top = posY - 200  # 200 위부터 시작
    rect.left = posX
    speed = random.randint(5, 10)  # 속도
    shadow = pygame.Rect(bomb_shadow.get_rect())  # 폭탄 그림자
    shadow.top = posY
    shadow.left = posX
    # 떨어지는 효과
    scale = (0, 0)
    rotate = 0
    return {'rect': rect, 'x': posX, 'y': posY, 'scale': scale, 'speed': speed, 'shadow': shadow, 'rotate': rotate}


def addBomb():
    bombs.append(createBomb(SCREEN_WIDTH, SCREEN_HEIGHT))


def bomb_MoveEffect(bomb):
    bomb['rect'].top += bomb['speed']
    sc = (200 - ((bomb['y'] - bomb['rect'].top) if bomb['rect'].top < bomb['y'] else 200)) // 4
    bomb['scale'] = (sc, sc)
    bomb['rect'].left = bomb['x'] + ((50 - sc) / 2)
    bomb['shadow'].top = bomb['y'] + ((50 - sc) / 2)
    bomb['shadow'].left = bomb['x'] + ((50 - sc) / 2)
    bomb['rotate'] = (bomb['rotate'] + 1) % 3
    return bomb


def changeExplosion(bomb):
    bomb['rect'].top = bomb['y'] - 25
    bomb['rect'].left = bomb['x'] - 25
    return {'rect': bomb['rect'], 'cnt': 0, 'hit': False, 'scale': 50}


def explosionImage(cnt):  # 폭발 이미지
    return pygame.transform.scale(pygame.image.load('./src/bomb_explosion' + str(cnt // 3 + 1) + '.png'), (100, 100))


def init(width, height):
    global bombs
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    SCREEN_WIDTH = width
    SCREEN_HEIGHT = height
    bombs = []
    for _ in range(2):  # 처음 폭탄 수
        bombs.append(createBomb(SCREEN_WIDTH, SCREEN_HEIGHT))


def getPos():
    res = []
    for exp in explosion:
        res.append({'x': exp['rect'].left, 'y': exp['rect'].top, 'scale': 50, 'hit': False})
    return res


def run(screen):
    global SCREEN_WIDTH
    global SCREEN_HEIGHT

    for bomb in bombs:
        bomb = bomb_MoveEffect(bomb)
        if bomb['rect'].top > bomb['y']:
            explosion.append(changeExplosion(bomb))
            bombs.remove(bomb)
            bombs.append(createBomb(SCREEN_WIDTH, SCREEN_HEIGHT))

    for bomb in bombs:
        screen.blit(transformImage(bomb_shadow, bomb['scale'], bomb_rotate[bomb['rotate']]), bomb['shadow'])
        screen.blit(transformImage(bomb_image, bomb['scale'], bomb_rotate[bomb['rotate']]), bomb['rect'])
    for exp in explosion:
        screen.blit(explosionImage(exp['cnt']), exp['rect'])
        exp['cnt'] += 1
        if exp['cnt'] >= 15:
            explosion.remove(exp)


def display(screen):
    for bomb in bombs:
        screen.blit(transformImage(bomb_shadow, bomb['scale'], bomb_rotate[bomb['rotate']]), bomb['shadow'])
        screen.blit(transformImage(bomb_image, bomb['scale'], bomb_rotate[bomb['rotate']]), bomb['rect'])
    for exp in explosion:
        screen.blit(explosionImage(exp['cnt']), exp['rect'])
