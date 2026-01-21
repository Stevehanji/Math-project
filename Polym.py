import pygame
pygame.init()


screen_width = 1500
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
running = True

while running:
    screen.fill((100,100,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

pygame.quit()