import pygame
import gift
import person
import bomb
import random

# 글자 크기 설정
Big_font = None
Small_font = None
Mini_font = None
WIDTH, HEIGHT = 0, 0
cnt = 0

heartImg = pygame.transform.scale(pygame.image.load("./src/heart.png"), (30, 30))
heartR = pygame.Rect(heartImg.get_rect())


def init(width, height):
    global WIDTH, HEIGHT, cnt, Big_font, Small_font, Mini_font, message1, message2, message3, message4
    # 문구와 색상 설정
    WIDTH, HEIGHT = width, height
    cnt = 0
    # 글자 크기 설정
    Big_font = pygame.font.SysFont(None, 80, None, None)
    Small_font = pygame.font.SysFont(None, 40, None, None)
    Mini_font = pygame.font.SysFont(None, 20, None, None)
    message1 = Big_font.render("BOMB DODGE", True, (0, 0, 0))
    message2 = Small_font.render("Press the space bar to start the game..", True, (0, 191, 255))
    message3 = Mini_font.render("- Made by METHOD -", True, (102, 102, 102))

    message4 = Small_font.render("(r) view record", True, (150, 150, 150))


# 스페이스바를 누르지 않았을 경우 -> 처음 시작 화면
def startScreen(screen):
    global message1, message2, message3

    screen.fill((255, 255, 255))
    screen.blit(message1, (110, 230))
    screen.blit(message2, (45, 310))
    screen.blit(message3, (240, 500))
    screen.blit(message4, (210, 550))


def endScreen(screen, score):
    global WIDTH, HEIGHT
    screen.fill((255, 255, 255))
    game_over_image1 = Big_font.render('Game Over', True, (255, 0, 0))
    game_over_image2 = Small_font.render('Score: {}'.format(score), True, (255, 245, 0))
    game_over_image3 = Small_font.render("Press the space bar to main screen..", True, (0, 191, 255))
    screen.blit(game_over_image1,
                ((WIDTH - game_over_image1.get_width()) // 2, (HEIGHT - game_over_image1.get_height()) // 2))
    screen.blit(game_over_image2,
                ((WIDTH - game_over_image2.get_width()) // 2, ((HEIGHT - game_over_image2.get_height()) // 2) + 40))
    screen.blit(game_over_image3,
                (45, 450))
    screen.blit(message4, (210, 480))


def recordScreen(screen, record):
    screen.fill((255, 255, 255))
    MAX = 5
    if len(record) < 5:
        MAX = len(record)

    pr = []
    title = Big_font.render("Rank", True, (0, 0, 0))
    screen.blit(title, ((WIDTH - title.get_width()) // 2, 230))
    for i in range(MAX):
        pr.append(Small_font.render(str(record[i]), True, (0, 191, 255)))
        screen.blit(pr[i], ((WIDTH - pr[i].get_width()) // 2, 300 + 40 * i))
    mv = Small_font.render("Press the space bar to main screen..", True, (0, 191, 255))
    screen.blit(mv, (45, 550))


def pauseSceen(screen, score, heart):
    global WIDTH, HEIGHT

    if heart > 2:
        heartR.top, heartR.left = (10, WIDTH - 120)
        screen.blit(heartImg, heartR)
    if heart > 1:
        heartR.top, heartR.left = (10, WIDTH - 80)
        screen.blit(heartImg, heartR)
    if heart > 0:
        heartR.top, heartR.left = (10, WIDTH - 40)
        screen.blit(heartImg, heartR)

    font = pygame.font.SysFont("arial", 30, True, True)
    smallfont = pygame.font.SysFont("arial", 25, True, True)
    restart = smallfont.render("(r) restart", True, (0, 0, 0))
    exit = smallfont.render("(x) end game", True, (0, 0, 0))

    sc = font.render(str(score), True, (0, 0, 0))

    screen.blit(sc, (100 - sc.get_width(), 10))
    gift.display(screen)
    person.display(screen)
    bomb.display(screen)
    screenCover = pygame.Surface((WIDTH, HEIGHT))
    screenCover.set_alpha(128)
    screenCover.fill((150, 150, 150))
    screen.blit(screenCover, (0, 0))
    screen.blit(restart, ((WIDTH - restart.get_width()) // 2, 15))
    screen.blit(exit, ((WIDTH - exit.get_width()) // 2, 550))


def gameScreen(screen, score, heart, cnt, records):
    global WIDTH, HEIGHT

    gift.run(screen)
    person.run(screen)
    bomb.run(screen)
    pp = person.getPos()

    font = pygame.font.SysFont("arial", 30, True, True)

    pygame.draw.rect(screen, (255, 255, 255), [0, 0, WIDTH, 50])

    for g in gift.gifts:
        if (g['x'] - g['scale'] // 2 <= pp['x'] <= g['x'] + g['scale'] // 2) and (
                g['y'] - g['scale'] // 2 <= pp['y'] <= g['y'] + g['scale'] // 2):
            gift.gifts.remove(g)
            score += random.randint(1, 10) * 10

    for b in bomb.explosion:
        if b['hit']:
            continue
        if (b['rect'].left <= pp['x'] <= b['rect'].left + b['scale']) and (
                b['rect'].top <= pp['y'] <= b['rect'].top + b['scale']):
            heart -= 1
            b['hit'] = True
            if heart <= 0:
                file = open('record.txt', 'w')
                records.append(score)
                records.sort(key=lambda x: -int(x))
                file.write("\n".join(map(str, records)))
                file.write("\n")
                file.close()
                return score, heart, cnt, records, False
    if heart > 2:
        heartR.top, heartR.left = (10, WIDTH - 120)
        screen.blit(heartImg, heartR)
    if heart > 1:
        heartR.top, heartR.left = (10, WIDTH - 80)
        screen.blit(heartImg, heartR)
    if heart > 0:
        heartR.top, heartR.left = (10, WIDTH - 40)
        screen.blit(heartImg, heartR)

    smallfont = pygame.font.SysFont("arial", 25, True, True)
    pause = smallfont.render("(p) pause", True, (0, 0, 0))
    screen.blit(pause, ((WIDTH - pause.get_width()) // 2, 15))

    cnt += 1
    if cnt % 10 == 0:
        score += 10
    if cnt % 50 == 0:
        gift.addGift()
    if cnt % 100 == 0:
        bomb.addBomb()
    sc = font.render(str(score), True, (0, 0, 0))
    screen.blit(sc, (100 - sc.get_width(), 10))
    return score, heart, cnt, records, True
