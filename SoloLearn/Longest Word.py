text=input().strip()
words=text.split(' ')
ord=0
longest=len(words[0])
for word in words:
    if len(word) >longest:
        ord=words.index(word,ord)
print(words[ord])