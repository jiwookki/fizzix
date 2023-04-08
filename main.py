import pygame
from pygame import math
import sys
import collider
# Created 19/03/2023 :/
# meh






        
        

        

class Renderer():
    # I would call this the Sprite class but pygame already has a sprite class so 
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def render(self, screen):
        pass



class CircleRenderer():
    def __init__(self, x, y, color, radius):
        super().__init__(self, x, y, color)
        self.radius = radius
    def render(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.radius)




    
    
    


class Body():
    
    def __init__(self, x, y, length, mass):        
        self.x = x
        self.y = y
        self.length = length
        self.collider = None
        self.mass = mass
        self.velocity = math.Vector2(0, 0)
        
    def render(self, screen):    
        pass
    
    def add_force(self, vector):    
        self.velocity = self.velocity + (vector/self.mass)
    
    def run(self, dT):
        pass
    

class CircleBody(Body):
    
    def __init__(self, x, y, radius, mass):
        super().__init__(self, x, y, radius, mass)
        self.collider = collider.CircleCollider(x, y, radius)
        

    

   
class SquareBody(Body):
    pass    
    

class Object():
    def __init__(self, x, y, size, mass, color):
        self.body = Body(x, y, size, mass)
        self.renderer = Renderer(x, y, color)
    def run(screen):


    

def main():
    pygame.init()
    
    SCREEN = pygame.display.set_mode([900, 600])
    CLOCK = pygame.time.Clock()
    bodies = {"body1" : CircleBody(300, 300, 50, 10)}
    
    
    pygame.display.set_caption("random thing")
     
    while True:
        SCREEN.fill([0, 0, 0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        for bodyname in bodies:
            bodies[bodyname].render(SCREEN)
            
        pygame.display.flip()
        
        CLOCK.tick(60)
        







if __name__ == "__main__":
    main()
    
    
    
    