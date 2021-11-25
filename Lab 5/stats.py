def getAvg(myArray):
    """Takes an array as and input and outputs the mean of all elements"""
    x = 0
    for i in myArray: #add up all of the elements
        x+=i
    return(x/len(myArray)) #calculate mean
def getMedian(myArray):
    """Takes an array as an input and outputs the median"""
    myArray.sort() #array needs to be in order for this to work
    arrayLen = len(myArray) #store the array length so that we don't have to call the function every time we need it
    if (arrayLen % 2)==1: #is arraylen odd?
        return(myArray[int((arrayLen+1)/2)])
    else:
        medPos = int(arrayLen/2)
        median = (myArray[medPos-1] + myArray[medPos])/2 #if the number of elements in even, the median lies between two values
        return(median)