import renderer
import pygame
import math

pygame.init()
screen = pygame.display.set_mode([640, 480])

testrenderer = renderer.RectangleRenderer(200, 200, (255, 255, 255), 100, 75, 0)

clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    print(math.degrees(testrenderer.angle))
    testrenderer.render(screen)
    testrenderer.update_rotation(testrenderer.angle + 0.01)
    
    pygame.display.flip()
    clock.tick(60)
    



