import pygame
import pygame.gfxdraw
import math

class Renderer():
    # I would call this the Sprite class but pygame already has a sprite class so 
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def update_position(self, x, y):
        self.x = x
        self.y = y

    def update_rotation(angle):
        pass # the circle renderer does not need it



    def render(self, screen):
        raise NotImplementedError



class CircleRenderer(Renderer):

    def __init__(self, x, y, color, radius):
        super().__init__(x, y, color)
        self.radius = radius

    def render(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.radius)


class RectRenderer(Renderer):

    def __init__(self, x, y, color, width, height):
        super().__init__(x, y, color)
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
    
    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, width=1)


class RectangleRenderer(Renderer):
    def __init__(self, x, y, color, width, height, angle):
        '''represents general purpose rectangle renderer (i.e. one that can rotate).
        x, y are the coordinates of the center of the rectangle.
        width, height are the width and height of the rectangle.
        angle measures how rotated the rectangle is, measured from the center of the rectangle.
        '''
        super().__init__(x, y, color)
        self.center = pygame.Vector2(x, y)  
        self._hw = width/2 # half width
        self._hh = height/2 # half height
        self.angle = angle
        self._center_angle = math.atan(self._hh/self._hw)

        self._cradius = math.sqrt(self._hw*self._hw + self._hh*self._hh) # cradius = circumcenter radius
        self.ra = self.angle + self._center_angle

        print(f"circum radius = {str(self._cradius)}")
        print(f"A angle = {str(self.ra)}")
        print(f"center angle = {str(self._center_angle)}")


        self.points = self._calculate_points()
    
    def _get_corner_point(self, angle):
        return [self.x + self._cradius * math.cos(angle), self.y + self._cradius * math.sin(angle)]
    
    def _calculate_points(self):

        p1 = self._get_corner_point(self._center_angle + self.angle)
        p2 = self._get_corner_point(math.pi-self._center_angle + self.angle)
        p3 = self._get_corner_point(math.pi+self._center_angle + self.angle)
        p4 = self._get_corner_point(2*math.pi-self._center_angle + self.angle)

        return [p1,p2,p3,p4]

    def update_position(self, x, y):
        dx = x - self.x
        dy = y - self.y
        super().update_position(x, y)
        for i, p in enumerate(self.points):
            self.points[i] = [p[0]+dx, p[1]+dy]


    def update_rotation(self, angle):
        self.angle = angle
        self.ra = self.angle + self._center_angle
        self.points = self._calculate_points()
        

    def render(self, screen):
        pygame.draw.polygon(screen, self.color, self.points)

        
        





