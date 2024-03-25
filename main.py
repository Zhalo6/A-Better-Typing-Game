import pygame
import random
from randomWordGen import generateWord

generate = True

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
     
generateWord()
         
pygame.display.update()