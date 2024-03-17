import pygame
from enum import Enum
from pygame import math


class CollTypes(Enum):

    CIRCLE = "circle"
    RECT = "rect"
    BORDER = "border"


def check_collider_type(targetCollider, targetType):

    if targetCollider.type != targetType:
        raise TypeError(f"target collider is not of type {targetType.name}")
    else:
        return True


def circle_only(fun):

    def outfunction(self, targetCollider):
        if targetCollider.type == CollTypes.CIRCLE or targetCollider.type == CollTypes.BORDER:
            return fun(self, targetCollider)
        else:
            raise NotImplementedError("i havent made anything other than circletocircle yet lol")
    return outfunction





class Collider():
    
    def __init__(self, x, y):
        self.position = math.Vector2(x, y)
        
    def check_collision(self, targetCollider):
        # Returns True if self overlaps with targetCollider.
        # Returns False if otherwise.
        raise NotImplementedError

    def overlap_delta(self, targetCollider):
        # Returns Vector2: amount of overlap between self and targetCollider.
        # If no overlap between self and targetCollider, return Vector2(0, 0).
        raise NotImplementedError
    
    def update_position(self, x, y):
        self.position = math.Vector2(x, y)
        
   

class RectangleCollider(Collider):
    
    def __init__(self, point1, point2, length):
        super().__init__(point1[0], point1[1])
        self.points = [
            point1,
            point2,
            ((point2-point1).normalize().rotate(90) * length) + point2,
            ((point2-point1).normalize().rotate(90) * length) + point1
        ]
    
    def _check_circle_collision(self, circle):
        pass
    
    def _check_rectangle_axis(self, rect1, rect2, axis):
        
    def _check_rectangle_collision(self, rectangle):
        # Use Separating Axis Theorem. compare against x and y axes
        
        

    def check_collision(self, targetCollider):
        if targetCollider.type == CollTypes.CIRCLE:
            return 
        

        
        
        


class BorderCollider(Collider):
    def __init__(self, x, y, length, height):
        super().__init__(x, y)
        self.length = length
        self.height = height
        self.type = CollTypes.BORDER

    def _ccsaxis(self, radius, x, sx, length):
        if x + radius > sx + length:
            return 1
        elif x - radius < sx:
            return -1
        else:
            return 0

    def _check_circle_collision(self, targetColl):
        if self._ccsaxis(targetColl.radius, targetColl.position[0], self.position[0], self.length) != 0 or self._ccsaxis(targetColl.radius, targetColl.position[1], self.position[1], self.height) != 0:
            return True
        else:
            return False
        

    def _get_circle_overlap(self, targetColl):
        overlap = pygame.Vector2(0, 0)
        selfx = self.position[0]
        selfy = self.position[1]

        targetCollX = targetColl.position[0]
        targetCollY = targetColl.position[1]
        ccsx = self._ccsaxis(targetColl.radius, targetCollX, selfx, self.length)
        ccsy = self._ccsaxis(targetColl.radius, targetCollY, selfy, self.height)
        if ccsx == 1:
            overlap.x = (targetCollX + targetColl.radius) - (selfx + self.length)
        elif ccsx == -1:
            overlap.x = selfx - (targetColl.radius - targetCollX)
        if ccsy == 1:
            overlap.y = (targetCollY + targetColl.radius) - (selfy + self.height) 
        elif ccsy == -1:
            overlap.y = selfy - (targetColl.radius - targetCollY)
        return overlap
        
        
        
        
    

    @circle_only
    def check_collision(self, targetCollider):
        return self._check_circle_collision(targetCollider)

        


class CircleCollider(Collider):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
        self.type = CollTypes.CIRCLE

    def _check_circle_collision(self, circle):
        if circle.type == CollTypes.CIRCLE:
          if self.position.distance_to(circle.position) <= self.radius + circle.radius:
            return True
          else:
            return False

        
    def _overlap_delta_circle(self, circle):
        check_collider_type(circle, CollTypes.CIRCLE)
        #return (circle.position - self.position).normalize()*-(self.position.distance_to(circle.position))
        return -(circle.position - self.position).normalize() * (self.radius + circle.radius - self.position.distance_to(circle.position))/2

    def check_collision(self, targetCollider):
        if targetCollider.type == CollTypes.CIRCLE:
            return self._check_circle_collision(targetCollider)
        elif targetCollider.type == CollTypes.BORDER:
            return targetCollider._check_circle_collision(self)
    

    def overlap_delta(self, targetCollider):
        if targetCollider.type == CollTypes.CIRCLE:
            return self._overlap_delta_circle(targetCollider)
        elif targetCollider.type == CollTypes.BORDER:
            return -1 * targetCollider._get_circle_overlap(self)