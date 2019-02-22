import pygame
from Drawable import Drawable

# derived class that represents a Rectangle
class Rectangle(Drawable):
    def __init__(self, x = 0, y = 0, width = 1, height =1, color = (0,0,0)):
        super().__init__(x, y)
        self.__width = width
        self.__height = height
        self.__color = color

    def __str__(self):
        return "A rectangle " + super().__str__()

    # getters
    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    # setters
    def setWidth(self, w):
        self.__width = w

    def setHeight(self, h):
        self.__height = h

    def draw(self, surface):
        location = self.getLoc()
        pygame.draw.rect(surface, self.__color, [location[0] - 15, location[1] - 10, self.getWidth(), self.getHeight()])

if __name__ == "__main__":

    pygame.init()
    surface = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('My Drawable Objects')
    fpsclock = pygame.time.Clock()

    # list of drawable objects to be displayed
    drawables = []                 
    myRect = Rectangle(0, 0, 50, 50, (0,0,0))
    drawables.append(myRect)

    # game loop
    while True: 
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
                pygame.quit()
                exit()

        surface.fill((204, 229, 255))
        for drawable in drawables:
            drawable.draw(surface)
        
        pygame.display.update()
    fpsclock.tick(30)