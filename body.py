
from pygame import math
import collider


class Body():
    
    def __init__(self, x, y, length, mass):        
        self.x = x
        self.y = y
        self.length = length
        self.collider = None
        self.mass = mass
        self.velocity = math.Vector2(0, 0)
        self.uelocity = math.Vector2(0, 0)
    
    def add_momentum(self, vector, dT):    
        self.uelocity = self.uelocity + (vector / self.mass * dT)
    
    def run(self, dT):
        self.velocity = self.uelocity
        self.x += self.velocity.x * dT
        self.y += self.velocity.y * dT
        self.collider.update_position(self.x, self.y)
        
    
    def check_collision(self, targetBody):
        return self.collider.check_collision(targetBody.collider)
    
    def fix_collision(self, targetBody, dT):
        #print("fixed: " + str(self.velocity*((self.mass - targetBody.mass)/(self.mass + targetBody.mass)) + targetBody.velocity*(2*targetBody.mass**2/(self.mass+targetBody.mass))))
        print("targetbody uelocity is " + str(targetBody.uelocity))
        #print(targetBody.uelocity*(2*targetBody.mass**2/(self.mass+targetBody.mass)))
        collisiondelta = self.collider.overlap_delta(targetBody.collider)
        print(collisiondelta)
        self.x += collisiondelta[0] * (self.mass/(self.mass+targetBody.mass))
        self.y += collisiondelta[1] * (self.mass/(self.mass+targetBody.mass))
        
        self.uelocity = (self.uelocity*((self.mass - targetBody.mass)/(self.mass+targetBody.mass)) + targetBody.velocity*(2*targetBody.mass**2/(self.mass+targetBody.mass))).magnitude() * collisiondelta.normalize()
        #self.uelocity = targetBody.velocity
    

class CircleBody(Body):
    
    def __init__(self, x, y, radius, mass):
        super().__init__(x, y, radius, mass)
        self.collider = collider.CircleCollider(x, y, radius)
        

    

   
class SquareBody(Body):
    pass    
    
