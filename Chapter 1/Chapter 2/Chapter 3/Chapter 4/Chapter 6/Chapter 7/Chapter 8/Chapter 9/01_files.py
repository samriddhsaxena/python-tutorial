
f = open('Chapter 1\Chapter 2\Chapter 3\Chapter 4\Chapter 6\Chapter 7\Chapter 8\Chapter 9\sample.txt', 'r')
# data = f.read(5) #reads first 5 characters from the file
data = f.readline()
print(data)

data = f.readline()
print(data)
f.close()