name = input("What is your name?")
age = input("What is your age in years?")
height = input("What is your height in metres?")
age_seconds = int(age)*365*24*60*60
height_feet = float(height)*3.28084
print("Hi " + name + ", you are " + str(age_seconds) + " seconds old and " + str(height_feet) + " feet tall!")
