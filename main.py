import pygame
import math

# initialize pygame
pygame.init()

# Create the screen
SCREEN = pygame.display.set_mode((1300, 800))
pygame.display.set_caption("Menu")

BG = pygame.image.load("background.jpg")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("tt_ramillas.zip", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()


# caption and icon
pygame.display.set_caption("Hare Hound chase game")
icon = pygame.image.load('hare.png')
pygame.display.set_icon(icon)
confetti = pygame.image.load('confetti.png')

# hounds initial position
hound1Img = pygame.image.load('hound.png')
hound1X = 350
hound1Y = 100
hound1X_change = 0
hound1Y_change = 0

hound2Img = pygame.image.load('hound.png')
hound2X = 80
hound2Y = 370
hound2X_change = 0
hound2Y_change = 0

hound3Img = pygame.image.load('hound.png')
hound3X = 350
hound3Y = 625
hound3X_change = 0
hound3Y_change = 0

# hare initial position
hareImg = pygame.image.load('hare.png')
hareX = 1160
hareY = 370
hareX_change = 0
hareY_change = 0

board = pygame.image.load('board.jpg')
rect = (25, 45, 1245, 715)

def hare(x, y):
    SCREEN.blit(board, (25, 45))
    SCREEN.blit(hareImg, (x, y))

def hound(x, y):
    SCREEN.blit(hound1Img, (hound1X, hound1Y))
    SCREEN.blit(hound2Img, (hound2X, hound2Y))
    SCREEN.blit(hound3Img, (hound3X, hound3Y))

def isCollision1(hareX, hareY, hound1X, hound1Y):
    distance = math.sqrt(math.pow(hareX - hound1X, 2) + (math.pow(hound1Y - hareY, 2)))
    if distance < 110:
        return True
    else:
        return False

def isCollision2(hareX, hareY, hound2X, hound2Y):
    distance = math.sqrt(math.pow(hareX - hound2X, 2) + (math.pow(hound2Y - hareY, 2)))
    if distance < 110:
        return True
    else:
        return False

def isCollision3(hareX, hareY, hound3X, hound3Y):
    distance = math.sqrt(math.pow(hareX - hound3X, 2) + (math.pow(hound3Y - hareY, 2)))
    if distance < 110:
        return True
    else:
        return False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #keys for hare movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hareY_change = -0.3
            if event.key == pygame.K_DOWN:
                hareY_change = 0.3
            if event.key == pygame.K_LEFT:
                hareX_change = -0.3
            if event.key == pygame.K_RIGHT:
                hareX_change = 0.3
            if event.key == pygame.K_0:
                hareX_change = -0.3
                hareY_change = 0.3
            if event.key == pygame.K_1:
                hareX_change = -0.3
                hareY_change = -0.3
            if event.key == pygame.K_2:
                hareX_change = 0.3
                hareY_change = -0.3
            if event.key == pygame.K_3:
                hareX_change = 0.3
                hareY_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3:
                hareX_change = 0
                hareY_change = 0

        #keys for movement hound1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hound1Y_change = -0.3
            if event.key == pygame.K_DOWN:
                hound1Y_change = 0.3
            if event.key == pygame.K_RIGHT:
                hound1X_change = 0.3
            if event.key == pygame.K_2:
                hound1X_change = 0.3
                hound1Y_change = -0.3
            if event.key == pygame.K_3:
                hound1X_change = 0.3
                hound1Y_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_2 or event.key == pygame.K_3:
                hound1X_change = 0
                hound1Y_change = 0

        #keys for movement hound2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hound2Y_change = -0.3
            if event.key == pygame.K_DOWN:
                hound2Y_change = 0.3
            if event.key == pygame.K_RIGHT:
                hound2X_change = 0.3
            if event.key == pygame.K_2:
                hound2X_change = 0.3
                hound2Y_change = -0.3
            if event.key == pygame.K_3:
                hound2X_change = 0.3
                hound2Y_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_2 or event.key == pygame.K_3:
                hound2X_change = 0
                hound2Y_change = 0

        #keys for movements hound3

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hound3Y_change = -0.3
            if event.key == pygame.K_DOWN:
                hound3Y_change = 0.3
            if event.key == pygame.K_RIGHT:
                hound3X_change = 0.3
            if event.key == pygame.K_2:
                hound3X_change = 0.3
                hound1Y_change = -0.3
            if event.key == pygame.K_3:
                hound3X_change = 0.3
                hound3Y_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_2 or event.key == pygame.K_3:
                hound3X_change = 0
                hound3Y_change = 0



        SCREEN.fill((249, 210, 84))

    #changing the X, Y coordinates of the players

    hareX += hareX_change
    hareY += hareY_change
    hound1X += hound1X_change
    hound1Y += hound1Y_change
    hound2X += hound2X_change
    hound2Y += hound2Y_change
    hound3X += hound3X_change
    hound3Y += hound3Y_change

    #hare boundaries
    if hareX <= 80:
        hareX = 80
    if hareY <= 100:
        hareY = 100
    if hareY > 625:
        hareY = 625
    if hareX > 1160:
        hareX = 1160

    #hound1 boundaries
    if hound1X <= 80:
        hound1X = 80
    if hound1Y <= 100:
        hound1Y = 100
    if hound1Y > 625:
        hound1Y = 625
    if hound1X > 1160:
        hound1X = 1160

    #hound2 boundaries
    if hound2X <= 80:
        hound2X = 80
    if hound2Y <= 100:
        hound2Y = 100
    if hound2Y > 625:
        hound2Y = 625
    if hound2X > 1160:
        hound2X = 1160

    #hound3 boundaries
    if hound3X <= 80:
        hound3X = 80
    if hound3Y <= 100:
        hound3Y = 100
    if hound3Y > 625:
        hound3Y = 625
    if hound3X > 1160:
        hound3X = 1160

    collision1 = isCollision1(hareX, hareY, hound1X, hound1Y)
    if collision1:
        hareX += 160
        hareY += 0

    collision2 = isCollision2(hareX, hareY, hound2X, hound2Y)
    if collision2:
        hareX += 160
        hareY += 0

    collision3 = isCollision3(hareX, hareY, hound3X, hound3Y)
    if collision3:
        hareX += 160
        hareY += 0

    hare(hareX, hareY)
    hound(hound1X, hound1Y)
    hound(hound2X, hound2Y)
    hound(hound3X, hound3Y)

    font = pygame.font.Font('freesansbold.ttf', 64)
    textX = 450
    textY = 380
    if hareX >= 70 and hareX <= 110 and hareY >= 330 and hareY <= 450:
        disp = font.render("HARE WINS!", True, (38, 192, 255))
        screen.blit(confetti, (420, 200))
        screen.blit(disp, (textX, textY))


    pygame.display.update()