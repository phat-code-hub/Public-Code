vowels=('aeiou')
sentence=input('Words : ').strip().lower()
vowel_count=0
for letter in sentence:
    if letter in vowels:
        vowel_count +=1
print(vowel_count)