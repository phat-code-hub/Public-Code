import re
reg=re.compile(r'[aeiouAEIOU]')
sentence=input('NHap: ').strip()
vowel_list=reg.findall(sentence)
print(len(vowel_list))