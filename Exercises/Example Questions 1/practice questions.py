# Write a Python program to calculate the area of a rectangle given its length and width
length = 20
breadth = 30
area = length*breadth
print(area)

# Create a program that takes a user's name and age as input and prints a greeting message
# name = input("Enter your name: ")
# age = (input("Enter your age: "))
# greeting = "Good Morning "+ name+". Your age is "+age+"."
# print(greeting)

# Write a program to check if a number is even or odd
a = int(input("Enter the number to be checked: "))
if(a%2==0):
    print("The number is even.")
else:
    print("The number is odd.")

# Calculate the compound interest for a given principal amount, interest rate, and time period
prinAmt = 50000
rate = 10
time = 5
amt = prinAmt*((1+(rate/100))**time)
compoundInt = amt - prinAmt
print(compoundInt)

# Write a program that converts a given number of days into years, weeks, and days
totalDays = 747
years = int(totalDays/365)
remYears = int(totalDays%365)
weeks = int(remYears/7)
days = int(remYears%7)
print (years,"years ",weeks,"weeks ",days,"days ")

# Given a list of integers, find the sum of all positive numbers
listOfInt = [1,2,3,4,5]
sum = 0
for i in range(5):
    sum+=listOfInt[i]
print(sum)

# Implement a program that swaps the values of two variables.
a = 2
b = 4
print(a,b)
temp = a
a = b
b = temp
print(a,b)