import os
print(os.getcwd())
def bookTitle(title):
    print(f'{title[0].capitalize()}{len(title)}')
try:
    file=open(os.getcwd()+"\\SoloLearn\\filename.txt","r")
    lines=file.readlines()
    for line in lines:
        if ('\n' in line):
            bookTitle(line[:-1])
        else:
            bookTitle(line)
finally:
    file.close()