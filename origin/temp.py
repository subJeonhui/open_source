# 메소드(9팀) - 팀 프로젝트

from turtle import done
import pygame
import random
import bomb

# 게임판 구성
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

bomb.init(SCREEN_WIDTH, SCREEN_HEIGHT)

# 배경이미지
# background = pygame.image.load("background.png")

# 캐릭터
character = pygame.transform.scale(pygame.image.load("src/character.png"), (50,50))
characterSize = character.get_rect().size  # img크기 불러옴
characterWidth = characterSize[0]
characterHeight = characterSize[1]
characterXpos = (SCREEN_WIDTH / 2) - (characterWidth / 2)
characterYpos = SCREEN_HEIGHT - characterHeight

# 이동할 좌표
toX = 0
toY = 0

# 이동속도
characterSpeed = 10

# 난수 생성 - 똥 생성용
randomNumber = 30
poSpeed = 10

# 게임 플레이 총 시간
totalTime = 10
startTicks = pygame.time.get_ticks()


def runGame():
    global toX, toY, characterXpos, characterYpos
    run = True

    while run:
        screen.fill((255, 255, 255))
        dt = clock.tick(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    toX -= characterSpeed
                if event.key == pygame.K_RIGHT:
                    toX += characterSpeed
                if event.key == pygame.K_UP:
                    toY -= characterSpeed
                if event.key == pygame.K_DOWN:
                    toY += characterSpeed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    toX = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    toY = 0



        # 캐릭터 이동 & 프레임맞추기
        characterXpos += toX
        characterYpos += toY

        # 경계 설정-가로
        if characterXpos < 0:
            characterXpos = 0
        elif characterXpos > SCREEN_WIDTH - characterWidth:
            characterXpos = SCREEN_WIDTH - characterWidth

        # 경계 설정-세로
        if characterYpos < 0:
            characterYpos = 0
        elif characterYpos > SCREEN_HEIGHT - characterHeight:
            characterYpos = SCREEN_HEIGHT - characterHeight

        screen.blit(character, (characterXpos, characterYpos))

        bomb.run(screen)

        pygame.display.update()
    pygame.quit()


runGame()
