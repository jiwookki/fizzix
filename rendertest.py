import renderer
import pygame

pygame.init()
screen = pygame.display.set_mode([640, 480])

testrenderer = renderer.RectangleRenderer(pygame.Vector2(500, 400), pygame.Vector2(300, 200), 120, [255, 255, 255])

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    
    testrenderer.render(screen)
    pygame.display.flip()
    



