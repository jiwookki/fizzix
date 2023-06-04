import pygame
import object


from engine import *

class PhysicsTestEngine(Engine):
    def _event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                raise EndOfSimulation
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.timeScale = 1.2
                elif event.key == pygame.K_s:
                    self.timeScale = 12
                elif event.key == pygame.K_w:
                    self.timeScale = 0.012
                elif event.key == pygame.K_a:
                    print(str(self.objCounter))
                    self.objCounter += 1
                    self.objects[str(self.objCounter)] = object.CircleObject(random.randint(50, 850), random.randint(50, 550), 15, 10, [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE or event.key == pygame.K_s:
                    self.timeScale = 0.4



