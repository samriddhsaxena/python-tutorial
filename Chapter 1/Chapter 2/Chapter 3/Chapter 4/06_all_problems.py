#Program to create a dictionary of Hindi words with values as their english translation
'''
myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item",
}
print("Options are ",myDict.keys())
a = input("Enter the Hindi word\n")
# print("The meaning of your word is:",myDict[a]) 
print("The meaning of your word is:",myDict.get(a)) #please use this for no errors
'''

#Program to input eight numbers from the user and display all the unique numbers(once)
'''
num1 = int(input("Enter num 1\n"))
num2 = int(input("Enter num 2\n"))
num3 = int(input("Enter num 3\n"))
num4 = int(input("Enter num 4\n"))
num5 = int(input("Enter num 5\n"))
num6 = int(input("Enter num 6\n"))
num7 = int(input("Enter num 7\n"))
num8 = int(input("Enter num 8\n"))

s = {num1,num2,num3,num4,num5,num6,num7,num8}
print(s)
'''

#What will be the length of the followinf set s:
'''
s = {20,20.0,"20"}
print(s)
print(len(s))
'''

#Create a dictionary

favLang = {}
a = input("Enter your favourite language Shubham\n")
b = input("Enter your favourite language Ankita\n")
c = input("Enter your favourite language Sonali\n")
d = input("Enter your favourite language Harshita\n")
favLang["Shubham"] = a
favLang["Ankita"] = b
favLang["Sonali"] = c
favLang["Harshita"] = d

print(favLang)