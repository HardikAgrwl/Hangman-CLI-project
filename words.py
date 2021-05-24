import random

def choose_word():
    with open("words.txt" , "r") as file:
        allText = file.read()
        words = list(map(str,allText.split()))
        return (random.choice(words))
