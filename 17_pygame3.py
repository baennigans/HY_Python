# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 15:24:07 2024

@author: User
"""

import pygame

pygame.init()
display = pygame.display.set_mode((800,600))

player = pygame.image.load("spaceship1.png")
playerX, playerY, playerDx, playerDy = 400, 550, 0, 0

enemy = pygame.image.load("enemy1.png")
enemyX, enemyY, enemyDx, enemyDy = 0, 10, 0.1, 0.1

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key ==pygame.K_LEFT:
                playerDx = 0
                
    playerX += playerDx          

    enemyX += enemyDx
    if enemyX <= 0 or enemyX > 750:
        enemyDx *= -1
        enemyY += 30
                
    display.fill((0, 0, 0))
    display.blit(player, (playerX, playerY))
    display.blit(enemy, (enemyX, enemyY))
    pygame.display.update()        
        
pygame.quit()