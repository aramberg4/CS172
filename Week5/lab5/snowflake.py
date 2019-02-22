from Drawable import Drawable
import pygame


class Snowflake(Drawable):
    def __init__(self, x=0, ymax=0, color=(255, 255, 255), radius=5):
        super().__init__(x, y=0)
        # self.__x = x
        # self.__y = 0
        self.__color = color
        self.__radius = radius
        self.__yMax = ymax

    def getLoc(self):
        return (self._Drawable__x, self._Drawable__y)

    def setLoc(self, p):
        self._Drawable__x = p[0]
        self._Drawable__y = p[1]

    def getYMax(self):
        return self.__yMax

    def draw(self, surface):
        location = self.getLoc()
        pygame.draw.circle(surface, self.__color, location, self.__radius)

        # Line1:  (x-5,y)=>(x+5,y)
        # Line2:  (x,y-5)=>(x,y+5)
        # Line3:  (x-5,y-5)=>(x+5,y+5)
        # Line4:  (x-5,y+5)=>(x+5,y-5)
        x, y = location
        pygame.draw.line(surface, self.__color, (x - 5, y), (x + 5, y))
        pygame.draw.line(surface, self.__color, (x, y - 5), (x, y + 5))
        pygame.draw.line(surface, self.__color, (x - 5, y - 5), (x + 5, y + 5))
        pygame.draw.line(surface, self.__color, (x - 5, y + 5), (x + 5, y - 5))


if __name__ == "__main__":

    pygame.init()
    surface = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('My Drawable Objects')
    fpsclock = pygame.time.Clock()

    # list of drawable objects to be displayed
    drawables = []
    mySnowflake = Snowflake(10, (0, 0, 0), 1)
    drawables.append(mySnowflake)

    # game loop
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (
                    event.type == pygame.KEYDOWN
                    and event.__dict__['key'] == pygame.K_q):
                pygame.quit()
                exit()

        surface.fill((204, 229, 255))
        for drawable in drawables:
            drawable.draw(surface)

        pygame.display.update()
    fpsclock.tick(30)
