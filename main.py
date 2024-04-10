import pygame
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
activeColour = 'orange'
colour = 'gray'

class Hitbox(object):
  def __init__(self, colour, position, rect_width, rect_height):
    self.colour = colour
    self.rect_x = position[0]
    self.rect_y = position[1]
    self.rect_width = rect_width
    self.rect_height = rect_height   
    self.updateWord()
    self.font = pygame.freetype.SysFont('Arial', 15)

  def draw(self):
    pygame.draw.rect(screen, self.colour, 
        (self.rect_x, self.rect_y, self.rect_width, self.rect_height))     
    self.font.render_to(screen, (self.rect_x + 12.5, self.rect_y + 15), self.text, (0, 0, 0))

  def updateWord(self):
    self.text = generateWord()

bgColour = 'blue'
screen.fill(bgColour)
currentTime = 10
running = True
startmenu = True
maingameplay = False

position1 = (10, 10)
position2 = (250, 10)
position3 = (500, 10)
position4 = (10, 250)
position5 = (250, 250)
position6 = (500, 250)

userText = ''
inputtext = ''
textInputted = False
font = pygame.freetype.SysFont('Arial', 25)

hitbox = Hitbox(colour, position1, 100, 50)
hitbox.colour = activeColour
fakeHitbox1 = Hitbox(colour, position2, 100, 50)
fakeHitbox2 = Hitbox(colour, position3, 100, 50)
fakeHitbox3 = Hitbox(colour, position4, 100, 50)
fakeHitbox4 = Hitbox(colour, position5, 100, 50)
fakeHitbox5 = Hitbox(colour, position6, 100, 50)
allHitboxes = [hitbox, fakeHitbox1, fakeHitbox2, fakeHitbox3, fakeHitbox4, fakeHitbox5]

def newWords():
  for i in allHitboxes:
    i.updateWord()

def newPositions():
  generateNum(len(allHitboxes))
  print(randomNumber)
  for i in allHitboxes:
      i.colour = colour
      allHitboxes[randomNumber].colour = activeColour

   
while running:

  for event in pygame.event.get():
    if event.type == pygame.USEREVENT:
      if event.type == tick:
          currentTime = currentTime - 1
      if currentTime == 0:
        running = False

    if event.type == pygame.KEYDOWN:         
      if event.key == pygame.K_BACKSPACE: 
          userText = userText[:-1] 
      elif event.key == pygame.K_RETURN: 
        inputtext = userText
        userText = ''
        textInputted = True
      else: 
          userText += event.unicode

  pygame.draw.rect(screen, bgColour, (0, 0, screenWidth, screenHeight))   
  hitbox.draw()
  fakeHitbox1.draw()
  fakeHitbox2.draw()
  fakeHitbox3.draw()
  fakeHitbox4.draw()
  fakeHitbox5.draw()

  textRect = font.get_rect(userText, size = 50)
  textRect.center = (screenWidth // 2, screenHeight - 200)
  font.render_to(screen, textRect, userText, "white", size = 50)

  timerRect = font.get_rect(str(currentTime), size = 50)
  timerRect.center = (screenWidth - 50, screenHeight - 750)
  font.render_to(screen, timerRect, str(currentTime), "white", size = 50)
  
  pygame.display.flip()

  if textInputted == True:
    if inputtext == hitbox.text:
      randomNumber = generateNum(len(allHitboxes))
      newWords()
      newPositions()
      inputtext = ''
      currentTime = 10
      textInputted = False
      
    elif inputtext != hitbox.text:
      randomNumber = generateNum(len(allHitboxes))
      newWords()
      newPositions()
      inputtext = ''
      textInputted = False


   
  
  
  
