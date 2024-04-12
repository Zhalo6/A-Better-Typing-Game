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
  def __init__(self, colour, position, rect_screenWidth, rect_screenHeight, activeState):
    self.colour = colour
    self.rect_x = position[0]
    self.rect_y = position[1]
    self.updateWord()
    self.rect_screenWidth = rect_screenWidth
    self.rect_screenHeight = rect_screenHeight   
    self.activeState = activeState
    self.font = pygame.freetype.SysFont('Arial', 15)


  def draw(self):
    pygame.draw.rect(screen, self.colour, 
        (self.rect_x, self.rect_y, self.rect_screenWidth, self.rect_screenHeight))     
    self.font.render_to(screen, (self.rect_x + 12.5, self.rect_y + 15), self.text, (0, 0, 0))

  def updateWord(self):
    self.text = generateWord()

class textBoxCreation(object):
  def __init__(self, text, size, xPos, yPos, colour, drawlocation):
    self.text = text
    self.size = size
    self.xPos = xPos
    self.yPos = yPos
    self.colour = colour
    self.drawlocation = drawlocation

  def draw(self):
    self.name = font.get_rect(self.text, size = self.size)
    self.name.center = (self.xPos, self.yPos)
    font.render_to(self.drawlocation, self.name, self.text, self.colour, size = self.size)

bgColour = 'blue'
screen.fill(bgColour)
titlescreen = True
running = False
endscreen = False

difficulty = 2
currentTime = 30 // difficulty
health = 600
healthdrain = (health // (10 * difficulty))
timeIncrease = (3 * difficulty)

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

while titlescreen:  
  screen.fill('black')
  mainscreen = font.get_rect(mainscreentitle, size = 50)
  mainscreen.center = (screenWidth // 2, 50)
  font.render_to(screen, mainscreen,  mainscreentitle, "white", size = 50)
  pygame.display.flip()
  for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
          titlescreen = False
          running = True
   
while running:

  for event in pygame.event.get():
    if event.type == pygame.USEREVENT:
      if event.type == tick:
          currentTime = currentTime - 1
      if currentTime <= 0:
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

  inputTextRect = textBoxCreation(userText, 50, screenWidth // 2, screenHeight - 200, "white", screen)
  inputTextRect.draw()

  timerRect = font.get_rect(str(currentTime), size = 50)
  timerRect.center = (screenWidth - 50, screenHeight - 750)
  font.render_to(screen, timerRect, str(currentTime), "white", size = 50)

  if (health <= 0):
    running = False
    endscreen = True
  
  pygame.display.flip()

  if textInputted:
    for i in allHitboxes:
      if i.activeState and inputtext == i.text:
        randomNumber = generateNum(len(allHitboxes))
        newWords()
        newPositions()
        inputtext = ''
        textInputted = False
        currentTime += (timeIncrease + (currentTime // 30))
        health -= healthdrain
        print(health)
        break
      
      if i.activeState and inputtext != i.text:
        randomNumber = generateNum(len(allHitboxes))
        newWords()
        newPositions()
        inputtext = ''
        textInputted = False
        currentTime -= (timeIncrease + (currentTime // 3))
        break

while endscreen:
  screen.fill('black')
  endscreenText = 'You Win!'
  endscreenRect = font.get_rect(endscreenText, size = 50)
  endscreenRect.center = (screenWidth // 2, screenHeight // 2)
  font.render_to(screen, endscreenRect, endscreenText, "white", size = 50)
  pygame.display.flip()
