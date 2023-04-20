from tkinter import *
from tkinter import ttk
#root = Tk()


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


def playRound():
    global points, mistakes
    print("#")
    print("#")
    if not points == len(list(baseWord)):
        print(display)
        letter = str(input("Guesse a letter in the word: "))
        #print(usedLetters)
        if not letter in usedLetters:
            usedLetters.append(letter)
            #print(letter, " is not in ", usedLetters)
            if letter in baseWord:
                points += 1
                setDisplay("edit", letter)
                print(letter, " was in the word!")
                #print(display)
                if points == len(list(baseWord)):
                    print("You Won!!!!")
            else:
                mistakes -= 1
                print(letter, " is not in the word.")
        else:
            print("You already used ", letter)

        

print("Welcome to Hangman!")
display = []
mistakes = 5
points = 0
usedLetters = []
baseWord = str(input("Put a word to be guessed: "))
setDisplay("reset")
while mistakes > 0 and not points == len(list(baseWord)):
    playRound()
























#mainFrame = ttk.Frame(root, padding="3i, 3i")
#root.mainloop()
