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

hitbox = Hitbox('orange', position1, 100, 50)
fakeHitbox1 = Hitbox('red', position2, 100, 50)
fakeHitbox2 = Hitbox('red', position3, 100, 50)
fakeHitbox3 = Hitbox('red', position4, 100, 50)
fakeHitbox4 = Hitbox('red', position5, 100, 50)
fakeHitbox5 = Hitbox('red', position6, 100, 50)
allHitboxes = [hitbox, fakeHitbox1, fakeHitbox2, fakeHitbox3, fakeHitbox4, fakeHitbox5]

def newWords():
  for i in allHitboxes:
    i.updateWord()

def newPositions():
  generateNum()
  print(randomNumber)
  if (randomNumber == 1):
    hitbox.rect_x, hitbox.rect_y = position1[0], position1[1]
    fakeHitbox1.rect_x, fakeHitbox1.rect_y = position2[0], position2[1]
    fakeHitbox2.rect_x, fakeHitbox2.rect_y = position3[0], position3[1]
    fakeHitbox3.rect_x, fakeHitbox3.rect_y = position4[0], position4[1]
    fakeHitbox4.rect_x, fakeHitbox4.rect_y = position5[0], position5[1]
    fakeHitbox5.rect_x, fakeHitbox5.rect_y = position6[0], position6[1]
  if (randomNumber == 2):
    hitbox.rect_x, hitbox.rect_y = position2[0], position2[1]
    fakeHitbox1.rect_x, fakeHitbox1.rect_y = position3[0], position3[1]
    fakeHitbox2.rect_x, fakeHitbox2.rect_y = position4[0], position4[1]
    fakeHitbox3.rect_x, fakeHitbox3.rect_y = position5[0], position5[1]
    fakeHitbox4.rect_x, fakeHitbox4.rect_y = position6[0], position6[1]
    fakeHitbox5.rect_x, fakeHitbox5.rect_y = position1[0], position1[1]
  if (randomNumber == 3):
    hitbox.rect_x, hitbox.rect_y = position3[0], position3[1]
    fakeHitbox1.rect_x, fakeHitbox1.rect_y = position4[0], position4[1]
    fakeHitbox2.rect_x, fakeHitbox2.rect_y = position5[0], position5[1]
    fakeHitbox3.rect_x, fakeHitbox3.rect_y = position6[0], position6[1]
    fakeHitbox4.rect_x, fakeHitbox4.rect_y = position1[0], position1[1]
    fakeHitbox5.rect_x, fakeHitbox5.rect_y = position2[0], position2[1]
  if (randomNumber == 4):
    hitbox.rect_x, hitbox.rect_y = position4[0], position4[1]
    fakeHitbox1.rect_x, fakeHitbox1.rect_y = position5[0], position5[1]
    fakeHitbox2.rect_x, fakeHitbox2.rect_y = position6[0], position6[1]
    fakeHitbox3.rect_x, fakeHitbox3.rect_y = position1[0], position1[1]
    fakeHitbox4.rect_x, fakeHitbox4.rect_y = position2[0], position2[1]
    fakeHitbox5.rect_x, fakeHitbox5.rect_y = position3[0], position3[1]
  if (randomNumber == 5):
    hitbox.rect_x, hitbox.rect_y = position5[0], position5[1]
    fakeHitbox1.rect_x, fakeHitbox1.rect_y = position6[0], position6[1]
    fakeHitbox2.rect_x, fakeHitbox2.rect_y = position1[0], position1[1]
    fakeHitbox3.rect_x, fakeHitbox3.rect_y = position2[0], position2[1]
    fakeHitbox4.rect_x, fakeHitbox4.rect_y = position3[0], position3[1]
    fakeHitbox5.rect_x, fakeHitbox5.rect_y = position4[0], position4[1]
  if (randomNumber == 6):
    hitbox.rect_x, hitbox.rect_y = position6[0], position6[1]
    fakeHitbox1.rect_x, fakeHitbox1.rect_y = position1[0], position1[1]
    fakeHitbox2.rect_x, fakeHitbox2.rect_y = position2[0], position2[1]
    fakeHitbox3.rect_x, fakeHitbox3.rect_y = position3[0], position3[1]
    fakeHitbox4.rect_x, fakeHitbox4.rect_y = position4[0], position4[1]
    fakeHitbox5.rect_x, fakeHitbox5.rect_y = position5[0], position5[1]
    

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
      print("Correct!")
      randomNumber = generateNum()
      newWords()
      newPositions()
      inputtext = ''
      currentTime = 10
      textInputted = False
      
    elif inputtext != hitbox.text:
      print("?")
      randomNumber = generateNum()
      newWords()
      newPositions()
      inputtext = ''
      textInputted = False


   
  
  
  
