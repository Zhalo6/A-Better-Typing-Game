import random



def generateWord():

  generate = True
  
  if generate == True:
    with open("wordlist.txt", "r") as file: 
      allText = file.read() 
      words = list(map(str, allText.split())) 
  
      # print random string 
      currentWord = random.choice(words)
      generate = False
      return currentWord