# Program to find greatest of three numbers
'''
def maximum(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m = maximum(34,76,32)
print("The value of maximum is "+str(m))
'''

# Program to convert celsius to farenheit
'''
def farah(cel):
    return(cel *(9/5))+32

c = 45
f = farah(c)
print("Farenheit Tempurature is "+str(f))
'''

# Program to prevent print() function to print new line at the end 
'''
print("hello", end=" ")
print('how', end=" ")
print('are', end=" ")
print('you', end=" ")
'''

#Program to print star pattern
'''
n = 3
for i in range(n):
    print("*" * (n-i))
'''

#Program to remove a given word from a string and strip at same time

def remove_and_strip(string, word):
    newStr = string.replace(word,"")
    return newStr.strip()

this = "    Harry is good   "
remove_and_strip(this, "Harry")
print(this)
# print(this)
# print(this.strip())