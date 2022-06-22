from turtle import done
import pygame
import random
import sys

# 게임판 구성
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("폭탄 피하기")

# 시작 화면 구성
def start():
    # 글자 크기 설정
    Big_font = pygame.font.SysFont(None, 80)
    Small_font = pygame.font.SysFont(None, 40)
    Mini_font = pygame.font.SysFont(None, 20)
    # 문구와 색상 설정
    message1 = Big_font.render("BOMB DODGE",True,(0,0,0))
    message2 = Small_font.render("Press the space bar to start the game..",True,(0,191,255))
    message3 = Mini_font.render("- Made by METHOD -",True,(102,102,102))
    
    Game_Start = False
    Game_Over = False
    
    while True:
        for event in pygame.event.get():
            # 게임 나가기
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 스페이스바를 누를 시
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Game_Start = True
        # 스페이스바를 누르지 않았을 경우 -> 처음 시작 화면
        if Game_Start == False and Game_Over == False:
            screen.fill((255,255,255))
            screen.blit(message1, (110, 230))
            screen.blit(message2, (45, 310))
            screen.blit(message3, (240, 500))
            pygame.display.update()
        #스페이스바를 눌렀을 경우 -> 게임 화면으로 변환 (현재는 검은 화면으로 보임)
        elif Game_Start == True and Game_Over == False:
            screen.fill((0,0,0))
            pygame.display.update()
            # 게임 종료시 Game_Over = True
        # elif Game_Start == True and Game_Over == True:
            # 게임 종료 화면 출력

start()
