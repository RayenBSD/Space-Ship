import pygame as pg
from pygame import mixer
import random as rand

pg.init()
screenWidth = 700
screenHeight = 500
screen = pg.display.set_mode((screenHeight, screenWidth))
icon = pg.image.load("PyGame/Space Ship/spaceship.png")
pg.display.set_icon(icon)
pg.display.set_caption("Space Ship")

#backGround music
mixer.music.load("PyGame/Space Ship/background.wav")
mixer.music.play(-1)

heroX = 100
heroY = 600
width = 32
height = 32
heroStep = 5

numberOfEnemy = 10
enemyX = []
enemyY = []
enemyStep = []

bulletX = 1000
bulletY = 1000
bulletStep = -5
isShooted = False

scoreValue = 0

bg = pg.transform.scale(pg.image.load("PyGame/Space Ship/reea_mgsr_210901.jpg"), (500, 700))
hero = pg.image.load("PyGame/Space Ship/spaceship.png")
bullet = pg.image.load("PyGame/Space Ship/bullet.png")
enemy = []

for i in range(0, numberOfEnemy):
    enemy.append(pg.image.load("PyGame/Space Ship/space-ship.png"))
    enemyX.append(rand.randint(50, 450))
    enemyY.append(rand.randint(50, 500))
    enemyStep.append(rand.choice([-5, 5]))

def redraw():
    global enemyY, heroX, heroY, bulletY, score, scoreValue

    screen.blit(bg, (0, 0))

    screen.blit(hero, (heroX, heroY))

    screen.blit(bullet, (bulletX, bulletY))

    for i in range(numberOfEnemy):
        screen.blit(enemy[i], (enemyX[i], enemyY[i]))

    font = pg.font.Font("freesansbold.ttf", 32)
    score = font.render(f"Score: {str(scoreValue)}", True, (255, 255, 255))
    screen.blit(score, (10, 10))

    pg.display.update()

def move():
    global heroX, width, height, heroStep, enemyX, enemyY, enemyStep, bulletX, bulletY, isShooted, numberOfEnemy, scoreValue

    #hero
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and heroX - heroStep >= 0:
        heroX -= heroStep
    if keys[pg.K_RIGHT] and heroX + width + heroStep <= screenHeight:
        heroX += heroStep

    for i in range(0, numberOfEnemy):
        #Enemy
        if enemyX[i] + enemyStep[i] + 32 < screenHeight and enemyX[i] + enemyStep[i] > 0:
            enemyX[i] += enemyStep[i]
        else:
            enemyY[i] += 10
            enemyStep[i] *= -1
        #died
        if (bulletY <= enemyY[i] + 32 and bulletY >= enemyY[i]) and (bulletX <= enemyX[i] + 32 and bulletX >= enemyX[i]):
            bulletSound = mixer.Sound("PyGame/Space Ship/explosion.wav")
            bulletSound.play()
            enemyX[i] = rand.randint(50, 450)
            enemyY[i] = rand.randint(50, 500)
            bulletY = -32
            scoreValue += 1
        #lose
        if enemyY[i] + 32 >= heroY:
            quit()

    #Bullet
    if keys[pg.K_SPACE] and isShooted == False:
        bulletSound = mixer.Sound("PyGame/Space Ship/laser.wav")
        bulletSound.play()
        isShooted = True
        bulletX = heroX
        bulletY = heroY - 10

    if isShooted and bulletY  > -32:
        bulletY -= 10
    else:
        isShooted = False

while True:
    pg.time.delay(50)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
    move()
    redraw()