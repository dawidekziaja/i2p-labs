def fib(n):
    """returns nth number in the fibonacci sequence"""
    if n==1:
        return(1) #First and second terms have to be defined here as recursive formula would
    elif n==2:    #try to calculate 0th and (-1)th terms
        return(1)
    else:
        return(fib(n-1)+fib(n-2))
print("Welcome to the Fibonacci Generator!\nIt will generate the nth number in the Fibonacci sequence for you.")
userNumber = input("Enter n: ")
print("The " + userNumber + "th Fibonacci number is = " + str(fib(int(userNumber))))