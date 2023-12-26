#Greatest numbers of all time
'''
num1 = int(input("Enter num1\n"))
num2 = int(input("Enter num2\n"))
num3 = int(input("Enter num3\n"))
num4 = int(input("Enter num4\n"))

if(num1>num4):
    f1 = num1
else:
    f1 = num4

if(num2>num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print(str(f1)+" is greatest")
else:
    print(str(f2)+" is greatest")
'''

#Find out whether student is pass or fail
'''
sub1 = int(input("Enter first subject marks\n"))
sub2 = int(input("Enter second subject marks\n"))
sub3 = int(input("Enter third subject marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail")

elif(sub1+sub2+sub3)/3<40:
    print("You are fail due to total percentage less than 40")

else:
    print("Congratulations! You passed the exam")
'''

#Program to identify spam
'''
text = input("Enter the text\n")
spam = False

if("make a lot of money"in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("subscribe this"in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")
'''

#Program to find whether a given username has less than 10 characters or not
'''
userName = input("Enter your username\n")
if(len(userName)<10):
    print("Your username has less than 10 characters")
else:
    print("Your username does not follow our rules.")
'''

#Program to find whether a given name is present in list or not
'''
names = ["harry","shubham", "aditi", "shipra"]
name = input("Enter the name to check\n")

if name in names:
    print("Your name is present")
else:
    print("Your name is not present in the list")
'''

#Program to calculate the grade of student from his marks
'''
marks = int(input("Enter your marks\n"))

if(marks>=90):
    print("Your grade is Ex")
elif(marks>=80):
    print("Your grade is A")
elif(marks>=70):
    print("Your grade is B")
elif(marks>=60):
    print("Your grade is C")
elif(marks>=50):
    print("Your grade is D")
else:
    print("You are fail.")
'''

#Program to find out whether a given post is talking about "Harry" or not

name = ["Harry","harry","HARRY","hARRY"]
post = input("Enter your post\n")

if post in name:
    print("Your post contains harry")
else:
    print("No harry found")