myDict = {
    "Fast": "In a quick manner",
    "Harry": "A Coder",
    "Marks": [1,2,5],
    "anotherDict":{"Harry":"Player"},
    1:2
}

#Dictionary Items
print(list(myDict.keys())) #Prints the keys of the dictionary
print(myDict.values()) #Prints the values of the dictionary
print(myDict.items()) #Prints the (key, values) for all contents of the dictionary
print(myDict)
updateDict = {
    "Lovish":"Friend",
    "Shubham":"Another Friend",
    "Divya": "One more friend",
    "Harry":"A Dancer"
}
myDict.update(updateDict) #Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("Harry")) #prints the value for harry
print(myDict["Harry"]) #prints the value for harry

print(myDict.get("Harry2")) #returns None as harry2 is not present in dictionary
# print(myDict["Harry2"]) #Throws an error as harry2 is not present in dictionary
