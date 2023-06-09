from tkinter import *
from tkinter import ttk
root = Tk()


# functions

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
    global letter, baseWord, points, pointMax, mistakes, usedLetters, gameState
    if use == "set":
        letter = str(input("Guess a letter in the word: "))
        listLetter = list(letter)
        letter = ""
        for x in range(len(listLetter)):
            if isinstance(listLetter[x], str) == True:
                listLetter[x] = listLetter[x].upper()
            letter = letter + listLetter[x]
        #print("this is letter but all caps:", letter)
    if use == "check":
        strBaseWord = ""
        for x in range(len(baseWord)):
            strBaseWord = strBaseWord + str(baseWord[x])
        #print(strBaseWord)
        if letter in baseWord:
            points += 1
            setDisplay("edit", letter)
            print(letter, " was in the word!")
            #print("this is points after a sucsessful check:", points)
            #print("this is points:", points)
            if points == pointMax:
                    print(display)
                    print("The word was: ", strBaseWord)
                    print("You Won!!!!")
                    gameState = False
        elif letter == strBaseWord:
            print("The word was:", strBaseWord)
            print("You Won!!!!")
            gameState = False
            points = pointMax
        elif len(list(baseWord)) != len(list(letter)) > 1:
            print("You can only guess one letter at a time or the whole word")
            print("Try again")
        elif len(list(baseWord)) == len(list(letter)) > 1:
            print("You guessed the wrong word")
            print("You have", mistakes, "mistakes left.")
            if mistakes == 0:
                print("YOU LOSE")
                print("You ran out of guesses 😥")
                gameState = False
        else:
            mistakes -= 1
            print(letter, " is not in the word.")
            print("You have", mistakes, "try's left.")
            if mistakes == 0:
                print("YOU LOSE")
                print("You ran out of guesses 😥")
                gameState = False
    
        

def setPoints(use):
    global baseWord, points, pointMax
    #print("set pooints used")
    if use == "set":
        dusedLetters = [" "]
        dBaseWord = list(baseWord)
        for x in range(len(dBaseWord)):
            if not dBaseWord[x] in dusedLetters:
                pointMax += 1
            dusedLetters.append(dBaseWord[x])
    elif use == "reset":
        pointMax = 0


def playRound():
    global points, mistakes, letter, usedLetters, pointMax, gameState
    setDisplay("edit", " ")
    if not points == len(list(baseWord)):
        print(display)
        if not len(usedLetters) < 3:
            print("You alread used these letters:", usedLetters[2:])        
        setLetter("set")
        #print(usedLetters)
        #print("this is letter before it is checked if it is in usedletteres: ", letter, "and this is used letters: ", usedLetters)
        if letter not in usedLetters:
            usedLetters.append(letter)
            #print(letter, " letter passed the check if it has been in used letters")
            #print("this is used letters:", usedLetters)
            setLetter("check")
        else:
            if letter == "":
                print("You need to input a letter.")
            elif letter == " ":
                print("You cannot input SPACE.")
            else:
                print("You already used", letter)
    else: 
        print("You Wonnn!!!!!")
        gameState = False
        points = pointMax


def playGame():
    global gameState, baseWord, display, usedLetters, mistakes, pointMax, points
    print("Welcome to Hangman!")
    display = []
    mistakes = 0
    while True:
        try:
            mistakes = int(input("How many mistakes can your oponent make: "))
            print("#")
            print("#")
            break
        except:
            print("You must put an integer, try again.")
            print("#")
            print("#")
    points = 0
    usedLetters = [" ", ""]
    pointMax = 0
    baseWord = ""
    #baseWord = str(input("Put a word to be guessed: "))
    setBaseWord("set")
    setDisplay("reset")
    for x in range(25):
            print("#")
    setPoints("set")
    #print(pointMax)
    #print(mistakes)
    while gameState == True:
        playRound()
        #print(gameState)
        print("#")
        print("#")
    else:
        return False


def hangman():
    global gameState, yesList
    while playGame() == True:
        playGame()
        #print("first loop")
    else:
        #print("else on first loop")
        if str(input("Do you want to play again?: ")).lower() in yesList:
            gameState = True
            print("#")
            print("#")
            hangman()
        else:
            print("Alright, thank you for playing!")    
            
            
# varibles

gameState = True
yesList = ["yes", "yep", "yeah", "ya", "yup", "uh-huh", "okay", "alright", "certainly", "indeed", "affirmative", "roger that", "exactly", "absolutely", "sure thing", "you bet", "no problem", "right", "ok", "sure", "fine", "if you say so", "i'd love to", "bet", "y"]
display = []
mistakes = 5
points = 0
usedLetters = [" ", ""]
pointMax = 0
baseWord = ""


# mainLoop for interface game
# hangman()





# display

# root
root.title("Hangman")
root.geometry("475x475")
root.minsize(475, 475)
root.maxsize(475, 475)

# mainframe
mainFrameStyle = ttk.Style()
mainFrameStyle.configure("mainFrame.TFrame", background="Light Green")
mainFrame = ttk.Frame(root, style="mainFrame.TFrame")
mainFrame.grid(column=0, row=0, sticky="nsew")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
ttk.Label(mainFrame, text="Main Frame").grid(column=3, row=3, sticky="s")


# children frames

# wordDisplayFrame
wordDisplayFrameStyle = ttk.Style()
wordDisplayFrameStyle.configure("display.TFrame", background="Red")
wordDisplayFrame = ttk.Frame(mainFrame, padding="50p, 50p, 50p, 50p", relief="sunken", style="display.TFrame")
wordDisplayFrame.grid(column=0, row=0, sticky="wen")
ttk.Label(wordDisplayFrame, text="word display").grid(column=0, row=0)

# keyBoardFrame
keyBoardFrameStyle = ttk.Style()
keyBoardFrameStyle.configure("keyBoard.TFrame", background="Pink", sticky="S")
keyBoardFrame = ttk.Frame(mainFrame, padding="160p, 50p", style="keyBoard.TFrame", relief="raised")
keyBoardFrame.grid(column=0, row=1, sticky="sew")
mainFrame.rowconfigure(1, weight=1)
ttk.Label(keyBoardFrame, text="KeyBoard").grid(column=0, row=0)

# hangmanDisplayFrame
hangmanDisplayFrameStyle = ttk.Style()
hangmanDisplayFrameStyle.configure("hangmanDisplayFrame.TFrame", background="Blue")
hangmanDisplayFrame = ttk.Frame(mainFrame, padding="50p, 50p, 50p, 50p", relief="ridge", style="hangmanDisplayFrame.TFrame")
hangmanDisplayFrame.grid(column=0, row=1, sticky="ew")
ttk.Label(hangmanDisplayFrame, text="Hangman Display Frame").grid(column=0, row=0)



root.mainloop()
