import pygame
import object
import engine
# Created 19/03/2023 :/
# meh
def main():
    gameObjects = {
        "1" : object.CircleObject(430, 300, 25, 1, [0, 0, 255]), 
        "2" : object.CircleObject(50, 300, 25, 1, [255, 0, 0]),
        "3" : object.CircleObject(501, 300, 25, 1, [0, 255, 0]),
        "4" : object.CircleObject(565, 224, 25, 1, [0, 255, 255]),
        "5" : object.CircleObject(585, 301, 25, 1, [255, 0, 255])
    }
    screen = pygame.display.set_mode([900, 600], pygame.SCALED)

    gameEngine = engine.Engine(gameObjects, 0.3, 120, screen)
    gameEngine.add_force_to_body("2", pygame.Vector2(7.5, 0.5))
    gameEngine.run()


if __name__ == "__main__":
    main()