import pygame
from randomWordGen import *
from randomNumberGen import *

initWords()
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
  def __init__(self, colour, position, rect_width, rect_height, activeState):
    self.colour = colour
    self.rect_x = position[0]
    self.rect_y = position[1]
    self.updateWord()
    self.rect_width = rect_width
    self.rect_height = rect_height   
    self.activeState = activeState
    self.font = pygame.freetype.SysFont('Arial', 15)


  def draw(self):
    pygame.draw.rect(screen, self.colour, 
        (self.rect_x, self.rect_y, self.rect_width, self.rect_height))     
    self.font.render_to(screen, (self.rect_x + 12.5, self.rect_y + 15), self.text, (0, 0, 0))

  def updateWord(self):
    self.text = generateWord()

bgColour = 'blue'
screen.fill(bgColour)
currentTime = 100
running = True

health = 600
timeIncrease = 3

position1 = (160, 200)
position2 = (400, 200)
position3 = (650, 200)
position4 = (160, 450)
position5 = (400, 450)
position6 = (650, 450)

userText = ''
inputtext = ''
textInputted = False
font = pygame.freetype.SysFont('Arial', 25)
mainscreentitle = 'Monster Hunter'

hitbox = Hitbox(colour, position1, 100, 50, False)
hitbox.colour = activeColour
hitbox.activeState = True
fakeHitbox1 = Hitbox(colour, position2, 100, 50, False)
fakeHitbox2 = Hitbox(colour, position3, 100, 50, False)
fakeHitbox3 = Hitbox(colour, position4, 100, 50, False)
fakeHitbox4 = Hitbox(colour, position5, 100, 50, False)
fakeHitbox5 = Hitbox(colour, position6, 100, 50, False)
allHitboxes = [hitbox, fakeHitbox1, fakeHitbox2, fakeHitbox3, fakeHitbox4, fakeHitbox5]

def newWords():
  for i in allHitboxes:
    i.updateWord()

def newPositions():
  generateNum(len(allHitboxes))
  for i in allHitboxes:
    i.colour = colour
    i.activeState = False    
  allHitboxes[randomNumber].colour = activeColour
  allHitboxes[randomNumber].activeState = True

running = False

while not running:  
  screen.fill('black')
  mainscreen = font.get_rect(mainscreentitle, size = 50)
  mainscreen.center = (screenWidth // 2, 50)
  font.render_to(screen, mainscreen,  mainscreentitle, "white", size = 50)
  pygame.display.flip()
  for e in pygame.event.get():
    if e.type == pygame.MOUSEBUTTONDOWN:
      running = True
   
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

  screen.fill("blue")
  for i in allHitboxes:
    i.draw()

  healthRect = pygame.Rect(screenWidth // 2, 50, health, 50)
  healthRect.center = (screenWidth // 2, 50)
  pygame.draw.rect(screen, 'red', healthRect, 100)

  textRect = font.get_rect(userText, size = 50)
  textRect.center = (screenWidth // 2, screenHeight - 200)
  font.render_to(screen, textRect, userText, "white", size = 50)

  timerRect = font.get_rect(str(currentTime), size = 50)
  timerRect.center = (screenWidth - 50, screenHeight - 750)
  font.render_to(screen, timerRect, str(currentTime), "white", size = 50)
  
  pygame.display.flip()

  if textInputted:
    for i in allHitboxes:
      if i.activeState and inputtext == i.text:
        randomNumber = generateNum(len(allHitboxes))
        newWords()
        newPositions()
        inputtext = ''
        currentTime += timeIncrease
        textInputted = False
        health -= 60
        break
      
      if i.activeState and inputtext != i.text:
        randomNumber = generateNum(len(allHitboxes))
        newWords()
        newPositions()
        inputtext = ''
        textInputted = False
        break
    

    
   
  


   
  
  
  
