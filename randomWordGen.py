import random



def generateWord():

  generate = True
  
  if generate == True:
    
    with open("wordlist.txt", "r") as file: 
      allText = file.read()
      words = list(map(str, allText.split()))
   
      currentWord = random.choice(words)
      generate = False
      return currentWord.lower()