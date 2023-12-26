#Program to open file and indentify whether 'twinkle' word is present or not
'''
f = open('Chapter 1\Chapter 2\Chapter 3\Chapter 4\Chapter 6\Chapter 7\Chapter 8\Chapter 9\poems.txt')
t = f.read()
if 'twinkle' in t:
    print("Twinkle is present.")
else:
    print("Twinkle is not present.")
f.close()
'''

#Program to update hi-score (incomplete)
'''
def game():
    return 64

score = game()
with open('Chapter 1\Chapter 2\Chapter 3\Chapter 4\Chapter 6\Chapter 7\Chapter 8\Chapter 9\hi-score.txt') as f:
    hiscore = int(f.read())

if hiscore<score:
    with open('Chapter 1\Chapter 2\Chapter 3\Chapter 4\Chapter 6\Chapter 7\Chapter 8\Chapter 9\hi-score.txt', 'w') as f:
        f.write(str(score))
'''

#Program to generate multiplication tables separately in different files
'''
for i in range(2,21):
    with open(f"Chapter 1\Chapter 2\Chapter 3\Chapter 4\Chapter 6\Chapter 7\Chapter 8\Chapter 9\\tables\Multiplication_table_of{i}",'w') as f:
        for j in range(1,11):
            f.write(f"{i}X{j}={i*j}\n")
            if j!=10:
                f.write('')
'''

#Program to update a word 'Donkey' with ###### to censor it.
'''
with open("Chapter 1\Chapter 2\Chapter 3\Chapter 4\Chapter 6\Chapter 7\Chapter 8\Chapter 9\sample.txt") as f:
    content = f.read()

content = content.replace("donkey", "######")

with open("Chapter 1\Chapter 2\Chapter 3\Chapter 4\Chapter 6\Chapter 7\Chapter 8\Chapter 9\sample.txt","w") as f:
    content = f.write(content)
'''

#Program to mine a log file and find out whether it contains python
'''
with open("Chapter 1\Chapter 2\Chapter 3\Chapter 4\Chapter 6\Chapter 7\Chapter 8\Chapter 9\log.txt") as f:
    content = f.read()

if 'python' in content.lower():
    print("Yes Python is present")
else:
    print("No python is not present.")
'''

#Program to identify the line number same question as above

content =""
i = 1
with open("Chapter 1\Chapter 2\Chapter 3\Chapter 4\Chapter 6\Chapter 7\Chapter 8\Chapter 9\log.txt") as f:
    i+=1
    while content:
        content = f.readline()
        print(content)

        if 'python' in content.lower():
            print("Yes Python is present")
        else:
            print("No python is not present.")