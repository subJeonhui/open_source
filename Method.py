# 메소드(9팀) - 팀 프로젝트

import pygame
import random
import StartScreen
import bomb
import person
import gift

# 게임판 구성
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

StartScreen.init(SCREEN_WIDTH, SCREEN_HEIGHT)
bomb.init(SCREEN_WIDTH, SCREEN_HEIGHT)
person.init(SCREEN_WIDTH, SCREEN_HEIGHT)
gift.init(SCREEN_WIDTH, SCREEN_HEIGHT)
# 배경이미지
background = pygame.transform.scale(pygame.image.load("./src/bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT-50))

# 게임 플레이 총 시간
totalTime = 10
startTicks = pygame.time.get_ticks()


def runGame():
    run = True

    Game_Start = 0
    heart = 0
    score = 0
    cnt = 0

    file = open('record.txt', 'r')
    records = list(map(int, file.read().split()))
    file.close()

    while run:
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 50))
        dt = clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # game 실행 start -------------------
            if Game_Start == 0:  # 메인 화면
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Game_Start = 1
                        heart = 3
                        score = 0
                        cnt = 0
                        bomb.init(SCREEN_WIDTH, SCREEN_HEIGHT)
                    if event.key == 114:  # r키를 눌렀을 경우
                        Game_Start = 3
            elif Game_Start == 2:  # 엔딩 화면
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Game_Start = 0
                    if event.key == 114:  # r키를 눌렀을 경우
                        Game_Start = 3
            elif Game_Start == 3:  # 기록화면
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Game_Start = 0
            elif Game_Start == 1: # 게임화면
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        person.moveX(-1)
                    if event.key == pygame.K_RIGHT:
                        person.moveX(1)
                    if event.key == pygame.K_UP:
                        person.moveY(-1)
                    if event.key == pygame.K_DOWN:
                        person.moveY(1)
                    if event.key == 112:
                        Game_Start = 4
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        person.toX = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        person.toY = 0
            elif Game_Start == 4:
                if event.type == pygame.KEYDOWN:
                    if event.key == 114:
                        Game_Start = 1
                    if event.key == 120:
                        Game_Start = 2
        if Game_Start == 0:
            StartScreen.startScreen(screen)
        elif Game_Start == 1:
            score, heart, cnt, records, x = StartScreen.gameScreen(screen, score, heart, cnt, records)
            if not x:
                Game_Start = 2
            # 게임 실행 End -------------------------
        elif Game_Start == 2:
            StartScreen.endScreen(screen, score)
        elif Game_Start == 3:
            StartScreen.recordScreen(screen, records)
        elif Game_Start == 4:
            StartScreen.pauseSceen(screen, score, heart)

        pygame.display.update()
    pygame.quit()
    # 점수


runGame()
