import pygame, sys
from pygame.locals import QUIT
from randomWordGen import *

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Monster Hunter')

class Hitbox(object):
  def __init__(self, rect_x, rect_y, rect_width, rect_height, text):
    self.rect_x = rect_x
    self.rect_y = rect_y
    self.rect_width = rect_width
    self.rect_height = rect_height   
    self.text = text   
    self.font = pygame.freetype.SysFont('Arial', 25)

  def draw(self):
    pygame.draw.rect(screen, (200, 200, 200), 
        (self.rect_x, self.rect_y, self.rect_width, self.rect_height))     
    self.font.render_to(screen, (self.rect_x, self.rect_y), self.text, (0, 0, 0))

def main():
  currentWord = generateWord()
  running = True
  while running:
      screen.fill('blue')
      head = Hitbox(10, 10, 25 + (10 * len(currentWord)), 50, currentWord)
      head.draw()
      pygame.display.flip()
      
      print(currentWord)
      
      inputText = input()

      if inputText == currentWord:
        currentWord = ''
        print("Correct!")
        currentWord = generateWord()
        
      elif inputText != currentWord:
        currentWord =''
        print("Loser")
        currentWord = generateWord()
   


  

if __name__ == "__main__":
    main()