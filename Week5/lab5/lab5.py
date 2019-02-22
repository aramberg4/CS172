import pygame
#from Drawable import Drawable
from rectangle import Rectangle
import random
from snowflake import Snowflake

def main():
    pygame.init()
    random.seed()
    surface = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Lab 5')
    fpsclock = pygame.time.Clock()

    # list of drawable objects to be displayed
    drawables = []                 
    sky = Rectangle(0, 0, 850, 400, (5,120,190))
    drawables.append(sky)
    ground = Rectangle(0, 400, 850, 250, (0,250,10))
    drawables.append(ground)
    s1 = Snowflake(0,random.randint(400, 850))
    drawables.append(s1)

    # game loop
    continue_animation = True
    while True: 
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
                pygame.quit()
                exit()
            elif (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_SPACE):
                continue_animation = not continue_animation
                print('Toggle')
                print(continue_animation)

        if continue_animation:
            # append new snowflake to drawables with random x location
            xLoc = random.randint(0, 800)
            newSnowFlake = Snowflake(xLoc,random.randint(400, 850))
            drawables.append(newSnowFlake)

            for drawable in drawables:
                if(isinstance(drawable, Snowflake) and drawable.getLoc()[1] < drawable.getYMax()):
                    # increment the y coordinate of Snowflake
                    loc = drawable.getLoc()
                    newLoc = (loc[0], loc[1]+1)
                    drawable.setLoc(newLoc)
                drawable.draw(surface)

                    
            pygame.display.update()
    fpsclock.tick(30)
if __name__ == "__main__":
    main()