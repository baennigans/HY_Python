import pygame

pygame.init()
display = pygame.display.set_mode((800,600))
myfont = pygame.font.SysFont('Comic Sans MS', 30)
pygame.display.set_caption("미사일게임-외계 우주선 6대")
score = 0

player = pygame.image.load("spaceship1.png")
playerX, playerY, playerDx, playerDy = 400, 550, 0, 0

enemy = pygame.image.load("enemy1.png")
enemyX = [ ]
enemyY = [ ]
enemyDx = [ ]
enemyDy = [ ]
enemyNumber = 6 

for i in range(enemyNumber):
    enemyX.append(20+i*60)
    enemyY.append(10)
    enemyDx.append(0.1)
    enemyDy.append(0.0)

missile = pygame.image.load('rocket1.png')
missileX, missileY, missileDx, missileDy = 0, 1000, 0, 0.1
missileState = "hidden"

gameover_font = pygame.font.SysFont('g마켓산스ttfmedium', 100)
gameover_text = gameover_font.render('GAME OVER', True, (255,0,0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerDx = -0.1
            if event.key == pygame.K_RIGHT:
                playerDx = 0.1
            if event.key == pygame.K_SPACE:
                if missileState == "hidden":
                    missileState = "fire"
                    missileX, missileY = playerX, playerY
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerDx = 0
    
    playerX += playerDx 
    if playerX <= 0 or playerX > 750:
        playerDx *= -1
        playerY += 0         
    
    display.fill((0, 0, 0))
    
    for i in range(enemyNumber):
        enemyX[i] += enemyDx[i]
        enemyY[i] += enemyDy[i]
        if enemyX[i] <= 0 or enemyX[i] > 750:
            enemyDx[i] *= -1
            enemyY[i] += 30
        rect1 = pygame.Rect(enemy.get_rect(topleft=(enemyX[i], enemyY[i])))
        rect2 = pygame.Rect(missile.get_rect(topleft=(missileX, missileY)))
        if rect1.colliderect(rect2) and missileState != "hidden":
            score += 1
            if score == enemyNumber:
                display.blit(gameover_text, (200, 250))
                pygame.display.update()
                pygame.time.delay(2000)
                running = False
                
            enemyX[i], enemyY[i], enemyDx[i], enemyDy[i] = 0, 1000, 0.1, 0.0         
        display.blit(enemy, (enemyX[i], enemyY[i]))
         
    if missileY <= 0:
        missileY = 1000
        missileState = "hidden"
    
    if missileState == "fire":
        missileY -= missileDy
                
    display.blit(player, (playerX, playerY))
    display.blit(missile, (missileX, missileY))
    text = myfont.render(f'score={score}', False, (255, 255, 255))
    
    display.blit(text, (10, 550))
    pygame.display.update()        
        
pygame.quit()