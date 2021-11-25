def getFactiorial(x):
    """Outputs Factorial of a number through recursion"""
    if x>1: #check is required to stop at 1 and not infinitely loop
        return(x*getFactiorial(x-1))
    else:
        return(x)
print(getFactiorial(7))