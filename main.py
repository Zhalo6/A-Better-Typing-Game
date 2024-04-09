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
  def __init__(self, rect_x, rect_y, rect_width, rect_height):
    self.rect_x = rect_x
    self.rect_y = rect_y
    self.rect_width = rect_width
    self.rect_height = rect_height   
    self.updateWord()
    self.font = pygame.freetype.SysFont('Arial', 15)

  def draw(self):
    pygame.draw.rect(screen, ('red'), 
        (self.rect_x, self.rect_y, self.rect_width, self.rect_height))     
    self.font.render_to(screen, (self.rect_x + 12.5, self.rect_y + 15), self.text, (0, 0, 0))

  def updateWord(self):
    self.text = generateWord()



bgColour = 'blue'
screen.fill(bgColour)
currentTime = 10
running = True


userText = ''
inputtext = ''
textInputted = False
font = pygame.freetype.SysFont('Arial', 25)
hitbox = Hitbox(10, 10, 100, 50)
fakeHitbox1 = Hitbox(250, 10, 100, 50)
fakeHitbox2 = Hitbox(500, 10, 100, 50)
allHitboxes = [hitbox, fakeHitbox1, fakeHitbox2]





def newWords():
  for i in allHitboxes:
    i.updateWord()

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
          userText = userText[:-1] 
      elif event.key == pygame.K_RETURN: 
        print(userText)
        inputtext = userText
        userText = ''
        textInputted = True
      else: 
          userText += event.unicode


  pygame.draw.rect(screen, bgColour, (0, 0, screenWidth, screenHeight))   
  hitbox.draw()
  fakeHitbox1.draw()
  fakeHitbox2.draw()

  textRect = font.get_rect(userText, size = 50)
  textRect.center = (screenWidth // 2, screenHeight - 200)
  font.render_to(screen, textRect, userText, "white", size = 50)

  
  
  pygame.display.flip()


  if textInputted == True:
    if inputtext == hitbox.text:
      print("Correct!")
      randomNumber = generateNum()
      newWords()
      inputtext = ''
      currentTime = 10
      textInputted = False
      
    elif inputtext != hitbox.text:
      print("?")
      randomNumber = generateNum()
      newWords()
      inputtext = ''
      textInputted = False


   
  
  
  
