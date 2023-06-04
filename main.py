import pygame
import object
import fizzix_engine
import engine
import random
# Created 19/03/2023 :/
# meh


def main():

    
    print("fizzix iz kool")

    version = 0.4
    pygame.init()
    



    gameObjects = {
#        "1" : object.CircleObject(430, 335, 25, 10, [0, 0, 255]), 
#        "2" : object.CircleObject(50, 345, 15, 10, [255, 0, 0]),
#        "3" : object.CircleObject(501, 260, 25, 10, [0, 255, 0]),
#        "4" : object.CircleObject(565, 224, 25, 10, [0, 255, 255]),
#        "5" : object.CircleObject(585, 301, 25, 10, [255, 0, 255]),
        "border" : object.BorderObject(0, 0, 900, 600, [255, 255, 255])
    }
    gameObjects["2"] = object.CircleObject(random.randint(50, 850), random.randint(50, 550), 25, 50, [255, 255, 255])
    screen = pygame.display.set_mode([900, 600], pygame.SCALED)
    pygame.display.set_caption("fizzix version {}".format(str(version)))

    gameEngine = fizzix_engine.PhysicsTestEngine(gameObjects, 0.4, 0, screen)
    #ameEngine.add_force_to_body("2", pygame.Vector2(7.5, 0.5))
    try:
      while True:
        gameEngine.run_frame()
        b2 = gameEngine.get_body("2")
        
        gameEngine.add_force_to_body("2", pygame.Vector2(pygame.mouse.get_pos() - pygame.Vector2(b2.x, b2.y))/400)
    except engine.EndOfSimulation:
       print("im done now")


if __name__ == "__main__":
    main()