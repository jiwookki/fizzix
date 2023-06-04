import pygame
import random
import sys

class EndOfSimulation(Exception):
    pass


class BaseEngine:
    def __init__(self, objects, timescale, fps):
        self.objects = objects
        self.running = False
        self.deltaTime = 0.1
        self.timeScale = timescale
        self.FPS = fps
        self.CLOCK = pygame.time.Clock()
        self.everyframes = []
        self.objCounter = 2



    def _run_physics(self):
        for objectname in self.objects:

            # add cool physics here

            for checkobjectname in self.objects:

                if objectname != checkobjectname:

                    if self.objects[objectname].body.check_collision(self.objects[checkobjectname].body):



                        self.objects[objectname].body.fix_collision(self.objects[checkobjectname].body, self.deltaTime)

        for objectname in self.objects:
            #objects[objectname].body.add_momentum(pygame.Vector2(0, 0.01), deltaTime)
            self.objects[objectname].run(self.deltaTime)

    def _render_objects(self):
        pass # DIY rendering

    def _event_handling(self):
        pass # DIY event handling


    def every_frame(self):
        pass # DIY GP every frame thing
        for things in self.everyframes:
            things(self)
    
    def register_everyframe(self, func):
        self.everyframes.append(func)
        return func

    def run_frame(self):
        self._event_handling()
        self._run_physics()
        self._render_objects()
        self.every_frame()
        self.CLOCK.tick(self.FPS)
        self.deltaTime = self.CLOCK.get_time() * self.timeScale



    def run(self):
        self.running = True
        while self.running:
            self.run_frame()
    
    def add_force_to_body(self, bodyIndex, force):
        self.objects[bodyIndex].body.add_momentum(force, self.deltaTime)

    def get_body(self, bodyIndex):
        return self.objects[bodyIndex].body


class Engine(BaseEngine):
    def __init__(self, objects, timescale, fps, screen):
        super().__init__(objects, timescale, fps)
        self.SCREEN = screen

    def _render_objects(self):
        self.SCREEN.fill([0, 0, 0])
        for objectname in self.objects:
            self.objects[objectname].render(self.SCREEN)
        pygame.display.flip()

    def _event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                raise EndOfSimulation


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





        


