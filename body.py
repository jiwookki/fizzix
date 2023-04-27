
from pygame import math
import pygame.mixer
import collider

pygame.mixer.init()

collide = pygame.mixer.Sound("ballhit.wav")


class Body():
    
    def __init__(self, x, y, length, mass, elasticity=1):        
        self.x = x
        self.y = y
        self.length = length
        self.collider = None
        self.mass = mass
        self.velocity = math.Vector2(0, 0)
        self.uelocity = math.Vector2(0, 0)
        self.elasticity = elasticity
    
    def add_momentum(self, vector, dT):    
        self.velocity = self.velocity + (vector / self.mass * dT)
    
    def run(self, dT):
        self.uelocity = self.velocity
        self.x += self.uelocity.x * dT
        self.y += self.uelocity.y * dT
        self.collider.update_position(self.x, self.y)
        
    
    def check_collision(self, targetBody):
        return self.collider.check_collision(targetBody.collider)
    
    def fix_collision(self, targetBody, dT):
        
        print("targetbody uelocity is " + str(targetBody.uelocity))
        
        collisiondelta = self.collider.overlap_delta(targetBody.collider)
        print(collisiondelta)
        self.x += collisiondelta[0] * (self.mass/(self.mass+targetBody.mass))
        self.y += collisiondelta[1] * (self.mass/(self.mass+targetBody.mass))
        
        #self.velocity = (self.velocity*((self.mass - targetBody.mass)/(self.mass+targetBody.mass)) + targetBody.uelocity*(2*targetBody.mass/(self.mass+targetBody.mass))).magnitude() * collisiondelta.normalize()
        self.velocity = ((self.elasticity*targetBody.mass*(targetBody.uelocity-self.uelocity) + self.mass*self.uelocity + targetBody.mass*targetBody.uelocity) / (self.mass + targetBody.mass)).magnitude() * collisiondelta.normalize()
        collide.play()
        
    

class CircleBody(Body):
    
    def __init__(self, x, y, radius, mass):
        super().__init__(x, y, radius, mass)
        self.collider = collider.CircleCollider(x, y, radius)
        


    

   
class SquareBody(Body):
    pass    
    

class StaticBody(Body):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mass = 2**64 - 1
        self.collider = None
        self.velocity = pygame.math.Vector2(0, 0)
        self.uelocity = pygame.math.Vector2(0, 0)

    def fix_collision(self, targetBody, dT):
        pass    


class Border(StaticBody):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.collider = collider.BorderCollider(x, y, width, height)
    
    

    

    


    