import pygame
from pygame.locals import *
from randomWordGen import *
from randomNumberGen import *

pygame.init()
screenWidth = 1000
screenHeight = 800
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Monster Hunter')
speed = 1000
tick = pygame.USEREVENT
pygame.time.set_timer(tick, speed)

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

bgColour = 'blue'
screen.fill(bgColour)

startClock = 1
currentTime = 10

user_text = '' 

positionOne = (10, 10)
positionTwo = (250, 10)
positionThree = (500, 10)
positionFour = (10, 200)
positionFive = (250, 200)
positionSix = ( 500, 200)


def newWords():
  currentWord, fakeWord, fakeWord2, fakeWord3, fakeWord4, fakeWord5 = [generateWord() for i in range(6)]

  return currentWord, fakeWord, fakeWord2, fakeWord3, fakeWord4, fakeWord5
  
running = True

currentWord, fakeWord, fakeWord2, fakeWord3, fakeWord4, fakeWord5 = newWords()

user_text = ''
inputtext = ''
textInputted = False
font = pygame.freetype.SysFont('Arial', 25)

while running:

  for event in pygame.event.get():
    if event.type == pygame.USEREVENT:
      if event.type == tick:
          print(currentTime)
          currentTime = currentTime - 1
      if currentTime < 0:
        print("Time's up!")
        running = False

    if event.type == pygame.KEYDOWN:         
      if event.key == pygame.K_BACKSPACE: 
          user_text = user_text[:-1] 
      elif event.key == pygame.K_RETURN: 
        print(user_text)
        inputtext = user_text
        user_text = ''
        textInputted = True
      else: 
          user_text += event.unicode

  hitbox = Hitbox(10, 10, 25 + (14 * len(currentWord)), 50, currentWord)
  fakeHitbox1 = fakeHitbox(250, 10, 25 + (14 * len(fakeWord)), 50, fakeWord)
  fakeHitbox2 = fakeHitbox(500, 10, 25 + (14 * len(fakeWord2)), 50, fakeWord2)
  fakeHitbox3 = fakeHitbox(10, 200, 25 + (14 * len(fakeWord3)), 50, fakeWord3)
  fakeHitbox4 = fakeHitbox(250, 200, 25 + (14 * len(fakeWord4)), 50, fakeWord4)
  fakeHitbox5 = fakeHitbox(500, 200, 25 + (14 * len(fakeWord5)), 50, fakeWord5)

  pygame.draw.rect(screen, bgColour, (0, 0, screenWidth, screenHeight))   
  hitbox.draw()
  fakeHitbox1.draw()
  fakeHitbox2.draw()
  fakeHitbox3.draw()
  fakeHitbox4.draw()
  fakeHitbox5.draw()

  font.render_to(screen, (screenWidth // 2, screenHeight - 200), user_text, ('white'))
  
  pygame.display.flip()


  if textInputted == True:
    if inputtext == currentWord:
      print("Correct!")
      randomNumber = generateNum()
      currentWord, fakeWord, fakeWord2, fakeWord3, fakeWord4, fakeWord5 = newWords()
      inputtext = ''
      currentTime = 10
      textInputted = False
      
    elif inputtext != currentWord:
      print("?")
      randomNumber = generateNum()
      currentWord, fakeWord, fakeWord2, fakeWord3, fakeWord4, fakeWord5 = newWords()
      inputtext = ''
      textInputted = False


   
  
  
  
