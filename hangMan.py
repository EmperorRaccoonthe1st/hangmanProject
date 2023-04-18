from tkinter import *
from tkinter import ttk
#root = Tk()


baseWord = ""
usedLetters = []
display = []
letterInput = ""
gameState = True


def setDisplay(use, letter = ""):
    global baseWord, display
    listWord = list(baseWord)
    if use == "reset":
        display = []
        for i in baseWord:
            display.append("_")
    elif use == "edit":
        for x in range(len(display)):
            if str(letter).upper() == str(listWord[x]).upper():
                display[x] = str(listWord[x])
        
    

print("Welcome to Hangman")
while gameState == True:
    print("first Loop")
    points = 0
    baseWord = input("Input the word to be guessed: ")
    wordGuessed = 5
    setDisplay("reset")
    print(wordGuessed)
    while wordGuessed > 0:
        print(str(display))
        letterInput = str(input("Input a letter that is in the word: "))
        if letterInput.upper() not in usedLetters:
            #print("pass one")
            usedLetters.append(str(letterInput).upper())
            if letterInput.upper() in baseWord.upper():
                print("Pasted")
                print(letterInput + " was in the word")
                setDisplay("edit", letterInput)
                points += 1
                if points == len(list(baseWord)):
                    print("You Won!") 
                    prompt = str(input("What do you want to do? Play Again or Quit: ")).upper()
                    if prompt == "PLAY AGAIN":
                        print("Lets play again!")
                        break                       
                    elif prompt == "QUIT":
                        gameState = False
                        break               
            else:
                print(letterInput + " was not in the word")
                wordGuessed -= 1
                print("You have " + str(wordGuessed) + " many guesses left.")
    else:
        print("You ran out of guesses! Better luck next time")
        break
        
































#mainFrame = ttk.Frame(root, padding="3i, 3i")
#root.mainloop()
