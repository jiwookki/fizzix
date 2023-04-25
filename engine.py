import pygame
import sys


class BaseEngine:
    def __init__(self, objects, timescale, fps):
        self.objects = objects
        self.running = False
        self.deltaTime = 0.1
        self.timeScale = timescale
        self.FPS = fps
        self.CLOCK = pygame.time.Clock()



    def _run_physics(self):
        for objectname in self.objects:

            # add cool physics here

            for checkobjectname in self.objects:

                if objectname != checkobjectname:

                    if self.objects[objectname].body.check_collision(self.objects[checkobjectname].body):

                        print(self.objects[checkobjectname].body.velocity)
                        print(objectname, checkobjectname)
                        self.objects[objectname].body.fix_collision(self.objects[checkobjectname].body, self.deltaTime)

        for objectname in self.objects:
            #objects[objectname].body.add_momentum(pygame.Vector2(0, 0.01), deltaTime)
            self.objects[objectname].run(self.deltaTime)

    def _render_objects(self):
        pass # DIY rendering

    def _event_handling(self):
        pass # DIY event handling

    def run(self):
        self.running = True
        while self.running:
            self._event_handling()
            self._run_physics()
            self._render_objects()
            self.CLOCK.tick(self.FPS)
            self.deltaTime = self.CLOCK.get_time() * self.timeScale


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

    def add_force_to_body(self, bodyIndex, force):
        self.objects[bodyIndex].body.add_momentum(force, self.deltaTime)


        


