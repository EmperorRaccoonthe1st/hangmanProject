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
    global letter
    if use == "set":
        letter = str(input("Guesse a letter in the word: "))
        if isinstance(letter, str) == True:
            letter = letter.upper()
        


def playRound():
    global points, mistakes, letter

    if not points == len(list(baseWord)):
        print(display)
        print("You alread used these letters: ", usedLetters)
        setLetter("set")
        
        #print(usedLetters)
        if not letter.upper() in usedLetters:
            usedLetters.append(letter.upper())
            #print(letter, " is not in ", usedLetters)
            if letter.upper() in baseWord:
                points += 1
                setDisplay("edit", letter)
                print(letter, " was in the word!")
                #print(display)
                if points == len(list(baseWord)):
                    print("The word was: ", display)
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
#baseWord = str(input("Put a word to be guessed: "))
setBaseWord("set")
setDisplay("reset")
for x in range(25):
        print("#")
while mistakes > 0 and not points == len(list(baseWord)):
    playRound()
    print("#")
    print("#")
























#mainFrame = ttk.Frame(root, padding="3i, 3i")
#root.mainloop()
