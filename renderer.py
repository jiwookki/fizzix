import pygame


class Renderer():
    # I would call this the Sprite class but pygame already has a sprite class so 
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def update_position(self, x, y):
        self.x = x
        self.y = y



    def render(self, screen):
        raise NotImplementedError



class CircleRenderer(Renderer):

    def __init__(self, x, y, color, radius):
        super().__init__(x, y, color)
        self.radius = radius

    def render(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.radius, width=0)