import pygame

SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0
characterXpos = 0
characterYpos = 0

# 캐릭터
# character = [pygame.transform.scale(pygame.image.load("./src/c1/character" + str(i) + ".png"), (50, 50)) for i in
#              range(1, 7)]
character = [pygame.transform.scale(pygame.image.load("./src/character"+str(i)+".png"), (50, 50)) for i in range(10)]
characterSize = character[0].get_rect().size  # img크기 불러옴
characterWidth = characterSize[0]
characterHeight = characterSize[1]


def init(width, height):
    global SCREEN_WIDTH, SCREEN_HEIGHT, characterXpos, characterYpos
    SCREEN_WIDTH, SCREEN_HEIGHT = width, height
    characterXpos = (SCREEN_WIDTH / 2) - (characterWidth / 2)
    characterYpos = SCREEN_HEIGHT - characterHeight


# 이동할 좌표
toX = 0
toY = 0

# 이동속도
characterSpeed = 5

f = 0
moveIndex = 0

direct = 0


def moveX(x):
    global toX, direct
    direct = x
    toX += (x * characterSpeed)


def moveY(y):
    global toY
    toY += (y * characterSpeed)


def getPos():
    return {'x': characterXpos, 'y': characterYpos, 'scale': characterSize[0]}


def run(screen):
    global SCREEN_WIDTH, SCREEN_HEIGHT, characterXpos, characterYpos, toX, toY, f, moveIndex, direct
    # 캐릭터 이동 & 프레임맞추기
    if toX != 0 or toY != 0:
        f += 1
        if f % 3 == 0:
            moveIndex += 1
    characterXpos += toX
    characterYpos += toY

    # 경계 설정-가로
    if characterXpos < 0:
        characterXpos = 0
    elif characterXpos > SCREEN_WIDTH - characterWidth:
        characterXpos = SCREEN_WIDTH - characterWidth

    # 경계 설정-세로
    if characterYpos < 50:
        characterYpos = 50
    elif characterYpos > SCREEN_HEIGHT - characterHeight:
        characterYpos = SCREEN_HEIGHT - characterHeight

    if direct == 1:
        screen.blit(character[moveIndex % len(character)], (characterXpos, characterYpos))
    else:
        screen.blit(pygame.transform.flip(character[moveIndex % len(character)], True, False),
                    (characterXpos, characterYpos))


def display(screen):
    global SCREEN_WIDTH, SCREEN_HEIGHT, characterXpos, characterYpos, toX, toY, f, moveIndex, direct
    if direct == 1:
        screen.blit(character[moveIndex % len(character)], (characterXpos, characterYpos))
    else:
        screen.blit(pygame.transform.flip(character[moveIndex % len(character)], True, False),
                    (characterXpos, characterYpos))
