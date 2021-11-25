#Differentiate polynomial ax^m + bx^n + cx^0
inputvals = []
for i in ["a","b","c","m","n","o"]:
    inputvals.append(int(input("Please enter a value for " + i + ": ")))
#print(inputvals)
def differentiate_term(a, m): #differentiates individual term, returns string to be printed
    x_coeff=a*m
    x_power=m-1
    return(str(x_coeff)+"x^"+str(x_power)) # formatted string
def integrate_term(a,m): #integrates individual term
    x_power=m+1
    x_coeff=a/x_power
    return(str(x_coeff)+"x^"+str(x_power)) # returns formatted string
def y_intercept(value):
    return( int(value[0])*0^int(value[3]) + int(value[1])*0^int(value[4]) + int(value[2])*0^int(value[5]) ) # sets x to 0 and finds value of y, returns int
userchoice = input("What would you like to do? (i/d/y/help)") # let user choose what to do with polynomial
if userchoice == "d":
    print("Your differentiated polynomial is:")
    print(differentiate_term(inputvals[0],inputvals[3]) + " + " + differentiate_term(inputvals[1],inputvals[4]) + " + " + differentiate_term(inputvals[2],inputvals[5])) #calls differentiate function and formats string nicely
elif userchoice == "i":
    print("Your integrated polynomial is:")
    print(integrate_term(inputvals[0],inputvals[3]) + " + " + integrate_term(inputvals[1],inputvals[4]) + " + " + integrate_term(inputvals[2],inputvals[5]))
elif userchoice == "y":
    print("Your y-intercept point is: " + str(y_intercept(inputvals)))
else:
    print("Please run program again\nChoose:\n i to integrate\nd to differentiate\ny to find y-intercept") # user gave invalid input or used 
