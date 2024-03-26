import pygame
from randomWordGen import *

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Monster Hunter')
     
def main():

  currentWord = generateWord()
  print(currentWord)

  inputText = input()

  if inputText == currentWord:
    currentWord = ''
    print("Correct!")

  if inputText != currentWord:
    currentWord =''
    print("Loser")
    
           
  pygame.display.update()

if __name__ == "__main__":
 while True:
    main()