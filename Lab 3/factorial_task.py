def factorial(n):
    x=1
    for i in range(1,n+1):
        x = x*i
    return(x)
inputNum = input("Please enter the number: ")
print("The factorial of " + inputNum + " is " + str(factorial(int(inputNum))))