# Write a Python program to print "Hello, World!"

print("Hello World!")

# Calculate the sum of two numbers entered by the user

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a+b)

# Convert temperature from Celsius to Fahrenheit.

celcius = int(input("Enter Celcius Temperature: "))
farenheit = (celcius*9)/5 + 32
print(farenheit)

# Create variables for storing a person's name, age, and average test score

name = "Samriddh"
age = 19
avgTestScore = 80

# Concatenate two strings and print the result

str1 = "Hello World "
str2 = "Good Morning!"
result = str1 + str2
print(result)

#Create a list of fruits and access elements using indexing

fruits = ['apple','banana','orange','mango']
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

# Write a program that checks if a given number is positive, negative, or zero.

n = int(input("Enter your number: "))
if(n>0):
    print("Number is positive.")
elif(n==0):
    print("Number is zero.")
else:
    print("Number is negative.")

# Create a loop that prints the first 10 even numbers.
    
for i in range(1,11):
    print(2*i)

#Implement a program that finds the largest number in a list.(Method1)

nums = [1,223,4,1156,227,89]
nums.sort()
print(nums[-1])

#Implement a program that finds the largest number in a list.(Method2)

nums = [1,223,4,1156,227,89]
nums.sort()
nums.reverse()
print(nums[0])

#Implement a program that finds the largest number in a list.(Method3)
nums = [1,223,4,1156,227,89]
print(max(nums))

#Given a list of numbers, find the sum and average using built-in functions

nums = [1,23,4,56,7]
sum_of_nums = sum(nums)
avg_of_nums = sum_of_nums/len(nums)
print(sum_of_nums)
print(avg_of_nums)

# Create a list of fruits and add a new fruit to the list.

fruits = ["apple","banana","mango","watermelon"]
print(fruits)
fruits.append("orange")
print(fruits)

# Access elements in a tuple using indexing.

tupNum = (1,23,4,56,7)
print(tupNum[0])
print(tupNum[1])
print(tupNum[2])
print(tupNum[3])
print(tupNum[4])