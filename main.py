import pygame
from pygame import math
import sys
import collider
import renderer

# Created 19/03/2023 :/
# meh

    
version = "0.1"
    


class Body():
    
    def __init__(self, x, y, length, mass):        
        self.x = x
        self.y = y
        self.length = length
        self.collider = None
        self.mass = mass
        self.velocity = math.Vector2(0, 0)
    
    def add_momentum(self, vector, dT):    
        self.velocity = self.velocity + (vector / self.mass * dT)
    
    def run(self, dT):
        self.x += self.velocity.x * dT
        self.y += self.velocity.y * dT
        self.collider.update_position(self.x, self.y)
    
    def check_collision(self, targetBody):
        return self.collider.check_collision(targetBody.collider)
    
    def fix_collision(self, targetBody, dT):
        self.add_momentum(self.collider.overlap_delta(targetBody.collider)*self.mass/2, dT)
    

class CircleBody(Body):
    
    def __init__(self, x, y, radius, mass):
        super().__init__(x, y, radius, mass)
        self.collider = collider.CircleCollider(x, y, radius)
        

    

   
class SquareBody(Body):
    pass    
    

class Object():

    def __init__(self, x, y, size, mass, color):
        self.body = Body(x, y, size, mass)
        self.renderer = renderer.Renderer(x, y, color)

    def run(self, screen, dT):
        self.body.run(dT)
        self.renderer.update_position(self.body.x, self.body.y)
        self.renderer.render(screen)
    


class CircleObject(Object):

    def __init__(self, x, y, rad, mass, color):
        self.body = CircleBody(x, y, rad, mass)
        self.renderer = renderer.CircleRenderer(x, y, color, rad)
    


def main():
    pygame.init()


    

    
    SCREEN = pygame.display.set_mode([1800, 1200])
    CLOCK = pygame.time.Clock()
    objects = {
        "1" : CircleObject(450, 100, 50, 10, [255, 255, 255]), 
        "2" : CircleObject(250, 70, 50, 10, [255, 255, 255])
    
    }
    
    deltaTime = 1
    fpsCounter = 0
    timeScale = 1
    FPS = 0

    pygame.display.set_caption("fizzix fps:90")
    CLOCK.tick(FPS)

    objects["2"].body.add_momentum(pygame.Vector2(100, 0), deltaTime)
    checklist = objects

    while True:
        SCREEN.fill([0, 0, 0])

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:

                sys.exit()

        for objectname in objects:

            # add cool physics here

            for checkobjectname in objects:
                if objectname != checkobjectname:
                    if objects[objectname].body.check_collision(objects[checkobjectname].body):
                        objects[objectname].renderer.color = [255, 0, 0]
                        objects[objectname].body.fix_collision(objects[checkobjectname].body, deltaTime)
                    else:
                        objects[objectname].renderer.color = [255, 255, 255]
                
            
            objects[objectname].body.add_momentum(pygame.Vector2(0, 1), deltaTime)


            objects[objectname].run(SCREEN, deltaTime)
            
            
        pygame.display.flip()
        
        fpsCounter += 1
        if fpsCounter == 30:
            fpsCounter = 0
            print(CLOCK.get_fps())
            print(deltaTime)
            pygame.display.set_caption("fizzix fps:"+str(round(CLOCK.get_fps(), 2)))

        deltaTime = (CLOCK.get_time() / 16.666666) * timeScale

        
        
        CLOCK.tick(FPS)

        




if __name__ == "__main__":
    print("Initializing fizzix v{}".format(version))
    main()
    
    
    
    