#!/usr/bin/env python3
import random
import time
import threading
from york_graphics import *
openWindow(width=504, height=1000, title="A Card Game")
debug=False
setTextProperties(size=36)
CardXSize=72
CardYSize=108
XOffset=(CardXSize/2)-1
YOffset=(CardYSize/2)-1

class Card: #making each card an object simplifies the drawing and game logic 
    def __init__(self,suit,colour,value,image,pos,paired):
        self.suit = suit
        self.colour = colour
        self.value = value #value of card 0-12  
        self.image = image
        self.pos = pos #xy coordinate of card on 7x7 grid
        self.paired = paired #has the card already been paired with another? determines if card is clickable/what texture it uses
    def draw(self):#draw card at its xy position
        moveTo(XOffset+CardXSize*self.pos[0],YOffset+CardYSize*self.pos[1])
        drawImage(self.image)

def drawExtra(image,position): #draw one of the extra assets (back of card, black.png) at a coordinate on the 7x7 grid
    x=position[0]
    y=position[1]
    moveTo(XOffset+CardXSize*x,YOffset+CardYSize*y)
    drawImage(image)

def getClickCoords(): #returns the 7x7 grid xy coordinates of a mouse click
    click = waitForMouseClick()
    click = (int(click[0]/CardXSize),int(click[1]/CardYSize)) #convert pixel coordinates to 7x7 grid coordinates
    if click[0]>6 or click[1]>6:
        return(getClickCoords())#if click is outside 7x7 grid, call function again
    if click==(3,3):
        return(getClickCoords())#if click is on 3,3 (empty space), call function again
    else:
        return(click)

def drawBack():#function to draw cards face down 
    if debug==True:#face up if in debug mode
        for card in cards:
            if card.paired==True:#if card is paired, draw the card face down
                drawExtra(back2,card.pos)
            else:
                card.draw()
    else:
        for card in cards:
            if card.paired==True:
                drawExtra(back2,card.pos) #back of card turns blue if card has been paired
            else:
                drawExtra(back1,card.pos)
    drawExtra(blackpng, (3,3))#draw a black square in centre
        
def flipOnClick(delay): #flips a card for (delay) seconds
    clickPos = getClickCoords()
    card1 = [x for x in cards if x.pos == clickPos][0] #search through the cards to find which one has the coordinates clickPos
    if card1.paired == True:
        return(flipOnClick(delay)) #call self if card is already paired
    card1.draw()
    updateCanvas()
    time.sleep(delay)
    drawBack()
    return(card1) #returns the card object of the card clicked

def simpleTimer(gameTime): #very simple timer, runs as a thread
    for i in range(0,gameTime): 
        print(60-i) #drawing things with the graphics library in two different threads causes instability, so a simple print() is used
        time.sleep(1)

def runGame(gameType, gameMode):
    score=0
    drawBack()
    gameStart=time.time()
    if gameMode == 2:
        timer = threading.Thread(target=simpleTimer, args=(60,)) #needs to be a separate thread from runGame(), as this stops every time it waits for user input
        timer.start()
    while score < 24:
        #show score
        moveTo(251,877)
        drawImage("cards/scoreboard.png")
        moveTo(340,900)
        setLineColour("white")
        drawText(str(score))
        if (gameMode == 2) and ((time.time()-gameStart) > 60): #if the game is in race mode - end the game when 60 seconds has passed
            endGame(score)

        #draw cards and get selection
        updateCanvas()
        card1 = flipOnClick(0.5)

        #draw selected card in bottom left corner
        moveTo(27+XOffset,909)
        drawImage(card1.image)

        updateCanvas()
    
        #check if values match
        card2 = flipOnClick(0.5)
        if gameType == 0:
            card1Match = card1.value
            card2Match = card2.value
        elif gameType == 1:
            card1Match = card1.suit
            card2Match = card2.suit
        elif gameType == 2:
            card1Match = card1.colour
            card2Match = card2.colour
        if card1Match==card2Match and card1!=card2: #cards have the same value but are not the same card
            card1.paired=True
            card2.paired=True
            moveTo(251,877)
            drawImage("cards/scoreboard.png")#redraw bottom scoreboard to clear score without clearing entire canvas
            drawBack()
            score=score+1
    if gameMode == 1:
        score = int(5000/int(time.time()-gameStart)) #If the gamemode was 
    endGame(score)

def endGame(score):
    moveTo(251,499)
    drawImage("cards/endgame.png")
    moveTo(340,900)
    drawText("Score :" + str(score))
    updateCanvas()
    time.sleep(0.1)
    waitForMouseClick()
    exit()

def mainMenu():
    menu=1
    moveTo(251,499)
    menus=["cards/menu1_1.png","cards/menu1_2.png","cards/menu1_3.png","cards/menu2_1.png","cards/menu2_2.png","cards/menu2_3.png"]
    menuPos=0
    drawImage(menus[menuPos])
    updateCanvas()
    while menu==1:
        key=waitForKeyPress()
        if key=="Down" and (menuPos<2):
            menuPos=menuPos+1
        elif key=="Up" and (menuPos>0):
            menuPos=menuPos-1
        elif key=="Return":
            menu=2
        drawImage(menus[menuPos])
        updateCanvas()
    gameType=menuPos
    menuPos=3
    drawImage(menus[menuPos])
    updateCanvas()
    while menu==2:
        key=waitForKeyPress()
        if key=="Down" and (menuPos<5):
            menuPos=menuPos+1
        elif key=="Up" and (menuPos>3):
            menuPos=menuPos-1
        elif key=="Return":
            menu=3
        drawImage(menus[menuPos])
        updateCanvas()
    gameMode=menuPos-3
    return((gameType,gameMode))

##SETUP##

#create an object for each card
cards=[]
for i in range(1,13):
    cards.append(Card("Spades","Black", i,"cards/image_part_"+str(i).zfill(3)+".png",(0,0),False))
    cards.append(Card("Hearts","Red",i,"cards/image_part_"+str(i+13).zfill(3)+".png",(0,0),False))
    cards.append(Card("Diamonds","Red",i,"cards/image_part_"+str(i+26).zfill(3)+".png",(0,0),False))
    cards.append(Card("Clubs","Black",i,"cards/image_part_"+str(i+39).zfill(3)+".png",(0,0),False))
back1="cards/Card_Back_1.png"
back2="cards/Card_Back_2.png"
blackpng="cards/black.png"
#Create a set of "extra" cards

#create a list of each coordinate on a 7x7 grid, then shuffle it
coordList=[]
for x in range(7):
    for y in range(7):
        coordList.append((x,y))
coordList.remove((3,3)) #remove 3,3 from set of coordinates as this is always blank
random.shuffle(coordList)
#assign each card a unique and random set of coordinates
i=0
for card in cards:
    card.pos = coordList[i] #assign each card a set of coordinates from the coordList
    i=i+1


#Main Program

menuOptions = mainMenu()
runGame(menuOptions[0],menuOptions[1])
