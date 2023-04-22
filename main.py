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
    def render(self, screen):
        self.renderer.render(screen)


    def run(self, dT):
        self.body.run(dT)
        self.renderer.update_position(self.body.x, self.body.y)
        
    
    


class CircleObject(Object):

    def __init__(self, x, y, radius, mass, color):
        super().__init__(x, y, radius, mass, color)
        self.body = CircleBody(x, y, radius, mass)
        self.renderer = renderer.CircleRenderer(x, y, color, radius)
    


def main():
    pygame.init()


    

    
    SCREEN = pygame.display.set_mode([900, 600])
    CLOCK = pygame.time.Clock()
    objects = {
        "1" : CircleObject(450, 300, 50, 1, [255, 255, 255]), 
        "2" : CircleObject(50, 300, 50, 10, [255, 255, 255])
    
    }
    
    deltaTime = 1
    fpsCounter = 0
    timeScale = 0.05
    simulation_is_running = True
    FPS = 0

    pygame.display.set_caption("fizzix fps:90")
    CLOCK.tick(FPS)

    objects["2"].body.add_momentum(pygame.Vector2(75, 0), deltaTime)
    checklist = objects
    pygame.time.wait(500)


    while simulation_is_running:
        SCREEN.fill([0, 0, 0])

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                

                

                simulation_is_running = False
                


        for x in range(0, 7):
          for objectname in objects:

            # add cool physics here

            for checkobjectname in objects:
                if objectname != checkobjectname:
                    if objects[objectname].body.check_collision(objects[checkobjectname].body):
                        objects[objectname].renderer.color = [255, 0, 0]
                        objects[objectname].body.fix_collision(objects[checkobjectname].body, deltaTime)
                    else:
                        objects[objectname].renderer.color = [255, 255, 255]
                
            
            


            objects[objectname].run(deltaTime)
            
        for objectname in objects:
            objects[objectname].render(SCREEN)
        pygame.display.flip()
        
        fpsCounter += 1
        if fpsCounter == 100:
            fpsCounter = 0
            pygame.display.set_caption("fizzix fps:"+str(round(CLOCK.get_fps(), 2)))

        deltaTime = (CLOCK.get_time() / 16.666666) * timeScale

        
        
        CLOCK.tick(FPS)
    body1 = objects["1"]
    body2 = objects["2"]
    print("Final results: ")
    print(f"Body 1 momentum: {body1.body.velocity[0] * body1.body.mass}, {body1.body.velocity[1] * body1.body.mass}")
    print(f"Body 2 momentum: {body2.body.velocity[0] * body2.body.mass}, {body2.body.velocity[1] * body2.body.mass}")

        




if __name__ == "__main__":
    print("Initializing fizzix v{}".format(version))
    main()
    
    
    
    