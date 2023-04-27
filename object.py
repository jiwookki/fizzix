import body
import renderer



class Object():

    def __init__(self, x, y, size=50, mass=1, color=[255, 255, 255], elasticity=5):
        self.body = body.Body(x, y, size, mass, elasticity=elasticity)
        self.renderer = renderer.Renderer(x, y, color)
    def render(self, screen):
        self.renderer.render(screen)


    def run(self, dT):
        self.body.run(dT)
        self.renderer.update_position(self.body.x, self.body.y)
        
    
    


class CircleObject(Object):

    def __init__(self, x, y, radius=50, mass=1, color=[255,255, 255], elasticity=0.9):
        super().__init__(x, y, size=radius, mass=mass, color=color, elasticity=elasticity)
        self.body = body.CircleBody(x, y, radius, mass)
        self.renderer = renderer.CircleRenderer(x, y, color, radius)

class BorderObject(Object):
    def __init__(self, x, y, width, height, color = [255, 255, 255]):
        super().__init__(x, y)
        self.body = body.Border(x, y, width, height)
        self.renderer = renderer.RectRenderer(x, y, color=color, width=width, height=height)

    