from york_graphics import *
openWindow()
lineThickness=50 #size of each pixel
posOffset=0 #set the position of the image on the canvas

smileyFace = [[0,0,0,0,0,0,0,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,1,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0]]
testImage = [[0,1],[1,0]]
setLineThickness(lineThickness)
def drawFromArray(inputArray):
    ySize=len(inputArray) #height of image
    xSize=len(inputArray[0]) #width of image
    for y in range(ySize):
        for x in range(xSize):
            xPos=(x*lineThickness)+(lineThickness/2)+posOffset #shift image to the right by half a pixel to stop it being cut off by the border
            yPos=(y*lineThickness)+posOffset
            moveTo(xPos,yPos)
            if inputArray[y][x] == 0:
                setLineColour("white")
            else:
                setLineColour("black")
            drawLine(0,lineThickness)
drawFromArray(smileyFace)
while True:
    updateCanvas()