import stats
numberList = input("Please input some numbers separated by commas: ")
numberList=numberList.split(",") #turn the input string into a list of strings
try:
    for i in range(len(numberList)):
        numberList[i] = float(numberList[i])
except ValueError: #if not all elements can be typecast as a float, user input must be invalid
    print("Run the program again and enter some comma separated numbers")
    quit()
print("The mean of your values is " + str(stats.getAvg(numberList)))