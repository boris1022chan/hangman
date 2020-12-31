import random 

dictionary = open('words.txt','r')
words = [i for i in dictionary]

choose_word = words[random.randint(0, len(words))]
word = []
for char in choose_word:
    word.append([char, "_ "])
del word[-1]

maxGuess=5
curGuess=0
while(curGuess < maxGuess):    
    ## display black space and guessed characters
    for item in word:
        print(item[1], end="")
    print()
    ## prompt input
    enter = input("Enter a character: ")
    haveChar = False
    complete = True
    for item in word:
        if enter == item[0]:
            item[1] = item[0]
            haveChar = True
        if item[1] == "_ ":
            complete = False
    ## Check if word is correctly guessed
    if complete:
        print("Good Job, You guessed the word")
        break
    ## if not correctly guessed, minus a guess chance
    if not haveChar:
        curGuess += 1
    print("Guess left: %s" % str(maxGuess - curGuess))

    print()

if curGuess == maxGuess:
    print("Too Bad, you fail to guess the word, the word is %s" % choose_word)

input("press any key to exit...")
