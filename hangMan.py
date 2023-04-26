from tkinter import *
from tkinter import ttk
#root = Tk()


def setDisplay(use, letter = ""):
    global baseWord, display, points
    listWord = list(baseWord)
    if use == "reset":
        display = []
        for i in range(len(baseWord)):
            if baseWord[i] != " ":
                display.append("_")
            else:
                display.append(" ")
                points += 1
    elif use == "edit":
        for x in range(len(display)):
            if str(letter).upper() == str(listWord[x]).upper():
                display[x] = str(listWord[x])


def setBaseWord(use):
    global baseWord
    if use == "set":
        baseWord = list(input("Input a word to be guessed: "))
        for x in range(len(baseWord)):
            if isinstance(baseWord[x], str) == True:
                #print(baseWord[x])
                baseWord[x] = baseWord[x].upper()
    #print(baseWord)


def setLetter(use):
    global letter, baseWord, points, pointMax, mistakes, usedLetters
    if use == "set":
        letter = str(input("Guesse a letter in the word: "))
        if not letter in usedLetters:
            usedLetters.append(letter)
        if isinstance(letter, str) == True:
            letter = letter.upper()
    if use == "check":
        strBaseWord = ""
        for x in range(len(baseWord)):
            strBaseWord = strBaseWord + str(baseWord[x])
        print(strBaseWord)
        if letter.upper() in baseWord:
            points += 1
            setDisplay("edit", letter)
            print(letter, " was in the word!")
            if points == pointMax:
                    print("The word was: ", display)
                    print("You Won!!!!")
        elif letter.upper() in strBaseWord:
            print("The word was: ", display)
            print("You Won!!!!")
            points = pointMax
        else:
            mistakes -= 1
            print(letter, " is not in the word.")
    
        

def setPoints(use):
    global baseWord, points, pointMax
    if use == "set":
        dusedLetters = []
        dBaseWord = list(baseWord)
        for x in range(len(dBaseWord)):
            if not dBaseWord[x] in dusedLetters:
                pointMax += 1
            dusedLetters.append(dBaseWord[x])
    elif use == "reset":
        pointMax = 0


def playRound():
    global points, mistakes, letter
    setDisplay("edit", " ")
    if not points == len(list(baseWord)):
        print(display)
        print("You alread used these letters: ", usedLetters)
        setLetter("set")
        #print(usedLetters)
        if not letter.upper() in usedLetters:
            setLetter("check")
        else:
            print("You already used ", letter)

        

print("Welcome to Hangman!")
display = []
mistakes = 5
points = 0
usedLetters = []
pointMax = 0
#baseWord = str(input("Put a word to be guessed: "))
setBaseWord("set")
setDisplay("reset")
for x in range(25):
        print("#")
setPoints("set")
while mistakes > 0 and points != pointMax:
    playRound()
    print("#")
    print("#")
























#mainFrame = ttk.Frame(root, padding="3i, 3i")
#root.mainloop()
