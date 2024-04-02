import pygame, sys
from randomWordGen import *

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Monster Hunter')
bgColour = 'blue'

class Hitbox(object):
  def __init__(self, rect_x, rect_y, rect_width, rect_height, text):
    self.rect_x = rect_x
    self.rect_y = rect_y
    self.rect_width = rect_width
    self.rect_height = rect_height   
    self.text = text   
    self.font = pygame.freetype.SysFont('Arial', 25)

  def draw(self):
    pygame.draw.rect(screen, ('red'), 
        (self.rect_x, self.rect_y, self.rect_width, self.rect_height))     
    self.font.render_to(screen, (self.rect_x + 12.5, self.rect_y + 15), self.text, (0, 0, 0))

class fakeHitbox(Hitbox):
  def draw(self):
    pygame.draw.rect(screen, ('grey'), 
        (self.rect_x, self.rect_y, self.rect_width, self.rect_height))     
    self.font.render_to(screen, (self.rect_x + 12.5, self.rect_y + 15), self.text, (0, 0, 0))

def main():

  currentWord = generateWord()
  fakeWord = generateWord()
  fakeWord2 = generateWord()
  fakeWord3 = generateWord()
  fakeWord4 = generateWord()
  fakeWord5 = generateWord()
  
  bgColour = 'blue'
  running = True
  while running:
      screen.fill(bgColour)
      hitbox = Hitbox(10, 10, 25 + (14 * len(currentWord)), 50, currentWord)
      fakeHitbox1 = fakeHitbox(250, 10, 25 + (14 * len(fakeWord)), 50, fakeWord)
      fakeHitbox2 = fakeHitbox(500, 10, 25 + (14 * len(fakeWord2)), 50, fakeWord2)
      fakeHitbox3 = fakeHitbox(10, 200, 25 + (14 * len(fakeWord3)), 50, fakeWord3)
      fakeHitbox4 = fakeHitbox(250, 200, 25 + (14 * len(fakeWord4)), 50, fakeWord4)
      fakeHitbox5 = fakeHitbox(500, 200, 25 + (14 * len(fakeWord5)), 50, fakeWord5)
      
      hitbox.draw()
      fakeHitbox1.draw()
      fakeHitbox2.draw()
      fakeHitbox3.draw()
      fakeHitbox4.draw()
      fakeHitbox5.draw()
      
      pygame.display.flip()
      
      inputText = input()

      if inputText == currentWord:
        currentWord = generateWord()
        fakeWord = generateWord()
        fakeWord2 = generateWord()
        fakeWord3 = generateWord()
        fakeWord4 = generateWord()
        fakeWord5 = generateWord()
        
      elif inputText != currentWord:
        currentWord = generateWord()
        fakeWord = generateWord()
        fakeWord2 = generateWord()
        fakeWord3 = generateWord()
        fakeWord4 = generateWord()
        fakeWord5 = generateWord()
   


  

if __name__ == "__main__":
  main()