import pygame
import sys

# Created 19/03/2023 :/
# meh







class Collider():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def check_collision(self, targetCollider):
        pass
        
   
class RectCollider(Collider):
    
    def __init__(self, x, y, length, height):
        super().__init__(self, x, y)
        self._rect = pygame.Rect(x, y, length, height)
      
class CircleCollider(Collider):
    
    def 
    
    
    


class Body():
    
    def __init__(self, x, y, length, mass):        
        self.x = x
        self.y = y
        self.length = length
        self.collider = None
        self.mass = mass
        self.velocity = pygame.math.Vector2(0, 0)
        
    def render(self, screen):    
        pass
    
    def add_force(self, vector):    
        self.velocity = self.velocity + (vector/mass)
    
   
class SquareBody(Body):
    pass    
    
def main():
    
    SCREEN = pygame.display.set_mode([900, 600])
    CLOCK = pygame.time.Clock()
    bodies = {"body1" : Body(300, 300, 50, 10)}
    
    
    pygame.display.set_caption("random thing")
     
    while True:
        SCREEN.fill([0, 0, 0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        for bodyname in bodies:
            bodies[bodyname].render(SCREEN)
            
        pygame.display.flip()
        
        CLOCK.tick(30)
        







if __name__ == "__main__":
    main()
    
    
    
    