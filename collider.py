import pygame
from enum import Enum
from pygame import math


class CollTypes(Enum):

    CIRCLE = "circle"
    RECT = "rect"


def check_collider_type(targetCollider, targetType):

    if targetCollider.type != targetType:
        raise TypeError(f"target collider is not of type {targetType.name}")
    else:
        return True


def circle_only(fun):

    def outfunction(self, targetCollider):
        if targetCollider.type == CollTypes.CIRCLE:
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
        
   

class RectCollider(Collider):
    
    def __init__(self, x, y, length, height):
        super().__init__(self, x, y)
        self._rect = pygame.Rect(x, y, length, height)
      


class CircleCollider(Collider):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
        self.type = CollTypes.CIRCLE

    def _check_circle_collision(self, circle):
        check_collider_type(circle, CollTypes.CIRCLE)
        if self.position.distance_to(circle.position) <= self.radius + circle.radius:
            return True
        else:
            return False
        
    def _overlap_delta_circle(self, circle):
        check_collider_type(circle, CollTypes.CIRCLE)
        return (circle.radius + self.radius) - (self.position.distance_to(circle.position))
        
    @circle_only
    def check_collision(self, targetCollider):
        return self._check_circle_collision(targetCollider)
    
    @circle_only
    def overlap_delta(self, targetCollider):
        return self._overlap_delta_circle(targetCollider)