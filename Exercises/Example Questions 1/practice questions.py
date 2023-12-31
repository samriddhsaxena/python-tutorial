# Write a Python program to calculate the area of a rectangle given its length and width
length = 20
breadth = 30
area = length*breadth
print(area)

# Create a program that takes a user's name and age as input and prints a greeting message
name = input("Enter your name: ")
age = (input("Enter your age: "))
greeting = "Good Morning "+ name+". Your age is "+age+"."
print(greeting)

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

# Given a list of numbers, find the sum and average

numbers = [1,23,4,56,7]
sum = 0
for i in range(len(numbers)):
    sum += numbers[i]
print("sum",sum)
avg = sum/len(numbers)
print("avg",avg)

# Create a program that takes a temperature in Celsius and converts it to Kelvin

celcius = int(input("Enter the temperature in celcius: "))
kelvin = celcius + 273.15
print('kelvin',kelvin)

# Given a list of names, concatenate them into a single string separated by spaces'
names = ['aditya','bhavesh','devansh','elizabeth','faizal']
finalList =""
for i in range(len(names)):
    finalList += names[i] + " "
print(finalList)

# Calculate the area and circumference of a circle given its radius

r = 10
area = 3.14*r*r
circum = 2*3.14*r
print("area",area)
print("circum", circum)

# Implement a program that converts a given number of minutes into hours and minute

givenMins = 184
hours = int(givenMins/60)
mins = givenMins%60
print(hours," hours ",mins," mins")

# Create a program that takes a year as input and checks if it is a leap year or not

year = int(input("Enter the year: "))
if((year%4==0 and year%100!=0) or (year%400==0)):
    print("The year is leap year.")
else:
    print("The year is not a leap year.")

# Given a list of integers, find all the even numbers and store them in a new list

integers = [1,23,4,56,7,89,10,112]
updatedList = []
for i in range(len(integers)):
    if(integers[i]%2==0):
        updatedList.append(integers[i])
    else:
        pass
print(updatedList)

# Create a program that generates the Fibonacci sequence up to a given number of terms/

def fibo(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibo_seq = fibo(n - 1)
        fibo_seq.append(fibo_seq[-1] + fibo_seq[-2])
        return fibo_seq
print(fibo(10))

# Given a list of names, print all names starting with the letter 'A'

names = ["Aditya","Priyanka","Anjali","Divya","Ankita","Jyoti"]
for i in names:
    if(i[0]=='A'):
        print(i)
    else:
        pass

# Implement a program that prints the multiplication table of a given number
    
n = int(input("Enter the number: "))
for i in range(1,11):
    print(n*i)

# Write a program that calculates the factorial of a given number
    
def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n - 1)

result = fac(5)
print(result)

# Given a list of words, count the number of words with more than five characters

list2 =["given","list","code","factorial","python","readme"]
count = 0
for i in list2:
    if len(i)>5:
        count+=1
print(count)

# Given a list of numbers, create a function to find the sum of all positive number
def sumFn():
    nums = [-1,23,4,56,-7]
    sum = 0
    for num in nums:
        if(num>0):
            sum+=num
        else:
            pass
    print(sum)
sumFn()

# Write a Python function to check if a given string is a palindrome

def paliFn(str):
    rev = str[::-1]
    if(rev == str):
        print("Yes it is palindrome.")
    else:
        print("Not a palindrome.")
paliFn("LALALAL")

# Create a function to find the square of each element in a given list

def sqFn():
    sqList = [1,2,3,4,5]
    for i in sqList:
        print(i**2)

sqFn()

# Calculate the area of a triangle given its base and height using a function

def areaofTri(base,height):
    area = 0.5*base*height
    return area
print("Area",areaofTri(1,2))

# Create a function that takes a list of strings and returns the list sorted alphabetically

def sortListFn():
    strList = ["area","outline","timeline","readme","examples","microsoft"]
    strList.sort()
    print(strList)
sortListFn()

# Write a function that takes two lists and returns their intersection (common elements)

def interFn(list1, list2):
    inter = set(list1) & set(list2)
    return inter
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = interFn(list1, list2)
print("Intersection:", result)

# Given a string, write a function to remove all vowels from it and return the modified string'

def remVowFn():
    modStr = ""
    str = input("Enter the string: ")
    for i in str:
        if((i=='a')or (i=='e')or (i=='i')or (i=='o')or (i=='u')):
            pass
        else:
            modStr = modStr+i
    print(modStr)
remVowFn()

# Write a Python program to find the length of the longest word in a sentence

def longestWordFn():
    sent = input("Enter the sentence: ")
    words = sent.split()
    longestWord = ""
    longestWordLen = 0
    for word in words: 
        currWordLen = len(word)
        if currWordLen>longestWordLen:
            longestWord = word
            longestWordLen = currWordLen
    print(longestWord)
    print(longestWordLen)
longestWordFn()

# Create a function that takes a sentence as input and returns the sentence in reverse orde

def revSent():
    sent = input("Enter the sentence: ")
    words = sent.split()
    rev = " ".join(words[::-1])
    print(rev)
revSent()

# Implement a program that takes a sentence and a word as input and checks if the word is present in the sentence.

def dupWordFn():
    sent = input("Enter the sentence: ")
    reqWord = input("Required word: ")
    words = sent.split()
    count = words.count(reqWord)
    if count > 1:
        print("Duplicate of '{}' present. Found {} times.".format(reqWord, count))
    elif count == 1:
        print("No duplicates of '{}' present. Found 1 time.".format(reqWord))
    else:
        print("No occurrences of '{}' in the sentence.".format(reqWord))

dupWordFn()

# Given two lists of numbers, concatenate them into a single list

list1 = [10,20,30,40]
list2 = [11,22,33,44]
res = list1 + list2
print(res)

# Write a program that finds the largest and smallest elements in a list

list1 = [10,20,30,40]
smallestNum = min(list1)
largestNum = max(list1)
print(smallestNum)
print(largestNum)

# Write a Python program to count the occurrences of each element in a given list

listOcc = [1,2,2,3,3,3,4,4,4,4]
occList = {}

for element in listOcc:
    if element in occList:
        occList[element] += 1
    else:
        occList[element] = 1
print("Occurrences of each element:")
for element, occList in occList.items():
    print(element,":",occList)

# Given a list of names, remove all duplicate names and print the unique names
    
names = ["adi","aditya","adipurush","adi","rahul","ramesh","rahul","ramesh"]
uniqueNames = []

for name in names:
    if name not in uniqueNames:
        uniqueNames.append(name)

for name in uniqueNames:
    print(name)

# Create a function that takes a list of strings and returns the list sorted by the length of the strings
    
def sortByLength(strings):
    return sorted(strings, key=len)

stringList = ["apple", "banana", "kiwi", "orange", "grape"]
sortedList = sortByLength(stringList)

print("Original List:", stringList)
print("Sorted List by Length:", sortedList)

# Write a program that checks if a given list is sorted in ascending order

ascList = ["just","looking","like","a","wow"]
updatedList = ascList.sort()

if ascList==sorted(ascList):
    print("Yes it is sorted.")
else:
    print("Not sorted.")

# Implement a function that takes two lists and returns their union (all unique elements from both lists)
    
def unionFn():
    listA = [1,2,3,4,5]
    listB = [4,5,6,7,8]
    unionSet = set(listA).union(set(listB))
    print(unionSet)
unionFn()