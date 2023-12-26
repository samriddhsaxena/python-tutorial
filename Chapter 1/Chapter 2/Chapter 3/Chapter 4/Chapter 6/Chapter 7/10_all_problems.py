#Program to print multiplication table of a given number using for loop
'''
num = int(input("Please enter your number for the table:\n"))
print('You will be provided the table of given number')

for i in range(1,11):
    print(str(num)+ "X"+str(i)+"="+str(i*num))
'''

#Program to greet people whose name start with S (WAY 1)
'''
l1=["Harry","Soham","Sachin","Rahul"]
print("options are harry, soham, sachin, rahul")
name=input('Enter your name\n')
if name=='soham':
    print('Good Morning')
elif name=='sachin':
    print("Good evening")
else:
    print("Invalid Response")
'''

#Program to greet people whose name start with S (WAY 2)
'''
l1=["Harry","Soham","Sachin","Rahul"]
for name in l1:
    if name.startswith('S'):
        print("Good Evening "+name)
'''

#Program to find whether the number is prime number or not
'''
num = int(input("Enter the number: \n"))
prime = True

for i in range(2,num):
    if(num%i==0):
        prime = False
        break
if prime:
    print("This number is prime.")
else:
    print("This number is not prime.")
'''

#Program to find the sum of first n natural numbers using while loop
'''
n = int(input("Enter your number:"))
sum1 = 0
while n>0:
    sum1 = sum1 + n
    n = n - 1
print("The sum of first n natural numbers is",sum1)
'''

#Program to calculate the factorial of given number using for loop
'''
from math import factorial


num = int(input("Enter your number:"))
factorial = 1
for i in range(1,num+1):
    factorial=factorial*1
print(f"The factorial of {num} this number is {factorial}")
'''

#Program to print * in a pattern 1
'''
n = 4

for i in range(4):
    print("*"*(i+1))
'''

#Program to print * in a pattern 2
'''
n=3

for i in range(3):
    print(" "*(n-i-1), end="")
    print("*"*(2*i+1), end="")
    print(" "*(n-i-1))
'''

#Program to print reverse multiplication table of a given number using for loop

num = int(input("Please enter your number for the table:\n"))
print('You will be provided the table of given number')

for i in range(11,1):
    print(str(num)+ "X"+str(i)+"="+str(i*num))