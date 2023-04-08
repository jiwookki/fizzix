import pygame
from enum import Enum
from pygame import math


class CollTypes(Enum):

    CIRCLE = "circle"
    RECT = "circle"


def check_collider_type(targetCollider, targetType):
    if targetCollider.type != targetType:
        raise TypeError(f"target collider is not of type {targetType.name}")
    else:
        return True




class Collider():
    
    def __init__(self, x, y):
        self.position = math.Vector2(x, y)
        
    def check_collision(self, targetCollider):
        pass
        
   

class RectCollider(Collider):
    
    def __init__(self, x, y, length, height):
        super().__init__(self, x, y)
        self._rect = pygame.Rect(x, y, length, height)
      


class CircleCollider(Collider):
    
    def __init__(self, x, y, radius):
        super().__init__(self, x, y)
        self.radius = radius
        self.type = CollTypes.CIRCLE

    def _check_circle_collision(self, circle):
        check_collider_type(circle, CollTypes.CIRCLE)
        if self.position.distance_to(circle.position) <= self.radius + circle.radius:
            return True
        else:
            return False
        
    def check_collision(self, targetCollider):
        if targetCollider.type == CollTypes.CIRCLE:
            return self._check_circle_collision(targetCollider)
        else:
            raise NotImplementedError("i havent made anything other than circletocircle yet lol")