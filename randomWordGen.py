import random
words = []

def initWords():
  global words
  with open("wordlist.txt", "r") as file: 
    allText = file.read()
    words = list(map(str, allText.split()))
 
def generateWord(): 
    currentWord = random.choice(words)
    return currentWord.lower()