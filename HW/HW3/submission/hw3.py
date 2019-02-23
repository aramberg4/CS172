#File Name:   hw3.py
#Purpose:     Program that runs the main game loop.
#Author:      Austin Ramberg
#User id:     afr38
#Date:        February 22, 2019

import pygame
from ball import Ball
from block import Block
from text import Text

# function to initialize our list of blocks
def initializBlocks():
    blockList =[]
    #first block column
    block1 = Block((600,370),True,30,(0,0,255))
    blockList.append(block1)
    block2 = Block((600,340),True,30,(0,0,255))
    blockList.append(block2)
    block3 = Block((600,310),True,30,(0,0,255))
    blockList.append(block3)
    #next column
    block4 = Block((630,370),True,30,(0,0,255))
    blockList.append(block4)
    block5 = Block((630,340),True,30,(0,0,255))
    blockList.append(block5)
    block6 = Block((630,310),True,30,(0,0,255))
    blockList.append(block6)
    #next column
    block7 = Block((660,370),True,30,(0,0,255))
    blockList.append(block7)
    block8 = Block((660,340),True,30,(0,0,255))
    blockList.append(block8)
    block9 = Block((660,310),True,30,(0,0,255))
    blockList.append(block9)

    return blockList

# function that determines if two objects intersect
def intersect(rect1, rect2) :
    if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y) :
        return True
    return False

# main function
def main():
    # initialize variables
    pygame.init()
    surface = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('HW 3')
    fpsclock = pygame.time.Clock()
    continue_animation = True
    ball_launched = False
    ballX = 40
    ballY = 400
    score = 0
    blockList = initializBlocks()

    # game loop
    while True: 
        # event handling
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
                pygame.quit()
                exit()
            elif (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_SPACE):
                continue_animation = not continue_animation
                print('Toggle')
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                initialX, initialY = pygame.mouse.get_pos()
            elif(event.type == pygame.MOUSEBUTTONUP):
                finalX, finalY = pygame.mouse.get_pos()
                xv = finalX - initialX
                yv = initialY - finalY
                ball_launched = not ball_launched

        if continue_animation:
            # draw environment           
            surface.fill((204, 229, 255))
            pygame.draw.line(surface, (0,0,0),(0,400),(800,400), 5)          
            scoreMsg = 'Score: '+str(score)
            scoreText = Text((0,0), True, scoreMsg, 25, (0,0,0))
            scoreText.draw(surface)

            #draw ball
            ball = Ball((int(ballX),int(ballY)),True, 0, 15, (255,0,0))
            ball.draw(surface)

            # draw blocks
            blocksKnocked = 0
            for block in blockList:
                if intersect(block.get_rect(),ball.get_rect()):
                    block.setVisible(False)
                block.draw(surface)
                if not block.getVisible():
                    # Calculate score
                    blocksKnocked += 10
                    score = blocksKnocked

            #update ball position 
            dt = 0.1
            g = 6.67
            R = 0.7
            eta = 0.5
            if ball_launched:
                ballX += dt*xv
                ballY -= dt*yv
                if ballY > 400:
                    yv = -R*yv
                    xv = eta*xv
                else:
                    yv = yv - g*dt

            pygame.display.flip()
            pygame.display.update()
    fpsclock.tick(30)
if __name__ == "__main__":
    main()