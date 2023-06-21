import pygame
import pygame.gfxdraw


class Renderer():
    # I would call this the Sprite class but pygame already has a sprite class so 
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def update_position(self, x, y):
        self.x = x
        self.y = y



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

    def __init__(self, point1, point2, length, color, line_width=0):
        '''
        Used to define a rectangle that can be rotated. 
        point1 and point2 are Vector2 objects that will be used to define one side of the rectangle. 
        The distance between point1 and point2 is the length of the rectangle. 
        From this information, point3 and point4 will be generated, at distance 'width'
        away from point1 and point2, and at 90 degree angle from point1 and point2 side. 
        '''
        super().__init__(point1[0], point1[1], color)

        self.points = [
            point1,
            point2,
            ((point2-point1).normalize().rotate(90) * length) + point2,
            ((point2-point1).normalize().rotate(90) * length) + point1
        ]
        
        self.line_width = line_width
        self.width = abs((point2-point1).magnitude())
        self.length = length
        self.angle = (point2-point1).as_polar()[1]
        print(self.width, self.length, self.angle)
    
    def update_position(self, x, y):
        for point in self.points:
            point.x += x
            point.y += y
            self.points[self.points.index(point)] = point

    def render(self, screen):
        pygame.draw.polygon(screen, self.color, self.points)

