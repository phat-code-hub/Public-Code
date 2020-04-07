from collections import Counter
#word=input('Word: ').strip()
word="racecar"
length=len(word)
num=list(Counter(word).values())
print(num)
# if length % 2 ==0:
#     pass
# else:
#     ls=[n for n in repeat_times.values() if n % 2 == 0]
#     print(len(ls))