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
        
    

def hangman():
    display = []
    points = 0
    baseWord = input("Input the word to be guessed: ")
    mistakes = 5
    usedLetters = []
    setDisplay("reset")
    playGame()
    
    
def playGame():
    print(str(display))     
    letterInput = str(input("Input a letter that is in the word: ")).upper()
    #usedLetters.append(letterInput)
    if letterInput in baseWord:
        print(letterInput + " was in the word")
        setDisplay("edit", letterInput)
        points += 1
    else:
        print(letterInput + " was not in the word.")
        mistakes -= 1
     
     
     
        
print("Welcome to Hangman")
while gameState == False:
    print("#####first Loop")
    points = 0
    baseWord = input("Input the word to be guessed: ")
    wordGuessed = 5
    usedLetters = []
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
for x in range(25):
        print("#")
while mistakes > 0 and not points == len(list(baseWord)):
    playRound()
























#mainFrame = ttk.Frame(root, padding="3i, 3i")
#root.mainloop()
