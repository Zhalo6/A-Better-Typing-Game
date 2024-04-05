import random

def generateWord():
 
  with open("wordlist.txt", "r") as file: 
    allText = file.read()
    words = list(map(str, allText.split()))
 
    currentWord = random.choice(words)
    return currentWord.lower()