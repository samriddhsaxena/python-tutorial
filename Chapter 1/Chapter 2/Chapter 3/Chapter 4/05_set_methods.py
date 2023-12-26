#Creating an empty set
b = set()
print(type(b))

# Adding values to the set
b.add(4)
b.add(5)
b.add((4,5,6))

# b.add({4:5}) #Cannot add list or dictionary to sets
print(b)

#Length of the set
print(len(b)) #prints the length of the set

#Removal of an item
b.remove(5) #removes 5 from set b
# b.remove(15) #throws an error while trying to remove 15 which is actually not present in set b
print(b)

print(b.pop())