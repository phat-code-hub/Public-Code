word=input('word: ').strip().upper()
Isogram=True
for w in word:
    count=word.count(w)
    if count>1:
        Isogram=False
        break
print('true' if Isogram else 'false')