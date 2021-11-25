from york_graphics import *
openWindow()
setLineThickness(25)
def drawRectangle(x,y,a,b): #function to draw rectangle at position x,y with size a,b
    moveTo(x,y)
    drawLine(a,0)
    moveTo(x+a,y)
    drawLine(0,b)
    moveTo(x+a,y+b)
    drawLine(-a,0)
    moveTo(x,y+b)
    drawLine(0,-b)
def drawTriangle(x,y,b,h): #draw triangle at x,y with base b and height h
    moveTo(x,y)
    drawLine(b,0)
    moveTo(x,y)
    drawLine((b/2),-h)
    moveTo(x+b,y)
    drawLine(-(b/2),-h)
def drawWindow(x,y,s): #draws a window at pos x,y with scale segment size s
    drawRectangle(x,y,s,s)   
    drawRectangle(x+s,y,s,s)
    drawRectangle(x,y+s,s,s)
    drawRectangle(x+s,y+s,s,s)

def drawHouse(x,y,sf): #draw house at pos (x,y) - position is taken from the top left corner of the main body of the house
#sf scales the house
#x=200 y=170
    drawRectangle(x,y,400*sf,400*sf) #draw house
    drawTriangle(x,y,400*sf,150*sf)  #draw roof

    drawWindow(x+50*sf,y+30*sf,50*sf)   #window1 -Drawing a window requires calling drawRectangle 4 times, put it in a function to make it neater

    drawWindow(x+250*sf,y+30*sf,50*sf) #window2

    drawWindow(x+50*sf,y+230*sf,50*sf) #window 3

    drawRectangle(x+250*sf,y+200*sf,100*sf,200*sf) #front door
drawHouse(200,170,1) 
while True:
    updateCanvas()