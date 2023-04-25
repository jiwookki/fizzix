import pygame
import object

# Created 19/03/2023 :/
# meh

    
version = "0.2"
    

    


def main():
    pygame.init()
    

    
    SCREEN = pygame.display.set_mode([900, 600], flags=pygame.SCALED)
    CLOCK = pygame.time.Clock()
    objects = {
        "1" : object.CircleObject(430, 300, 25, 1, [0, 0, 255]), 
        "2" : object.CircleObject(50, 300, 25, 1, [255, 0, 0]),
        "3" : object.CircleObject(501, 300, 25, 1, [0, 255, 0]),
        "4" : object.CircleObject(565, 224, 25, 1, [0, 255, 255]),
        "5" : object.CircleObject(585, 301, 25, 1, [255, 0, 255]),
    
    }
    
    
    deltaTime = 0.1
    fpsCounter = 0
    timeScale = 0.1
    simulation_is_running = True
    FPS = 0

    pygame.display.set_caption("fizzix fps:90")
    CLOCK.tick(FPS)

    objects["2"].body.add_momentum(pygame.Vector2(20, 0.5), deltaTime)

    pygame.time.wait(500)


    while simulation_is_running:
        SCREEN.fill([0, 0, 0])

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:

                simulation_is_running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_p:
                    FPS = 24
                elif event.key == pygame.K_w:
                    objects["2"].body.add_momentum(pygame.Vector2(0, -4), deltaTime)
                elif event.key == pygame.K_s:
                    objects["2"].body.add_momentum(pygame.Vector2(0, 4), deltaTime)
                elif event.key == pygame.K_a:
                    objects["2"].body.add_momentum(pygame.Vector2(-4, 0), deltaTime)
                elif event.key == pygame.K_d:
                    objects["2"].body.add_momentum(pygame.Vector2(4, 0), deltaTime)
                    
                else:
                


                    simulation_is_running = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    FPS = 90
                    timeScale = 0.4


        for objectname in objects:

            # add cool physics here

            for checkobjectname in objects:

                if objectname != checkobjectname:

                    if objects[objectname].body.check_collision(objects[checkobjectname].body):

                        print(objects[checkobjectname].body.velocity)
                        print(objectname, checkobjectname)
                        objects[objectname].body.fix_collision(objects[checkobjectname].body, deltaTime)
            


        for objectname in objects:
            #objects[objectname].body.add_momentum(pygame.Vector2(0, 0.01), deltaTime)
            objects[objectname].run(deltaTime)




        pygame.display.flip()
        
        fpsCounter += 1
        if fpsCounter == 100:
            fpsCounter = 0
            pygame.display.set_caption("fizzix fps:"+str(round(CLOCK.get_fps(), 2)))

        deltaTime = CLOCK.get_time() * timeScale

        
        
        CLOCK.tick(FPS)


    body1 = objects["1"]
    body2 = objects["2"]
    print("Final results: ")
    print(f"Body 1 momentum: {body1.body.velocity[0] * body1.body.mass}, {body1.body.velocity[1] * body1.body.mass}")
    print(f"Body 2 momentum: {body2.body.velocity[0] * body2.body.mass}, {body2.body.velocity[1] * body2.body.mass}")
    print(f"Body 1 umomentum: {body1.body.uelocity[0] * body1.body.mass}, {body1.body.uelocity[1] * body1.body.mass}")
    print(f"Body 2 umomentum: {body2.body.uelocity[0] * body2.body.mass}, {body2.body.uelocity[1] * body2.body.mass}")

        




if __name__ == "__main__":
    print("Initializing fizzix v{}".format(version))
    main()
    
    
    
    