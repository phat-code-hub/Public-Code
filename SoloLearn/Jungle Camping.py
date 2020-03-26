voice=['Grr','Rawr','Ssss','Chirp']
name=['Lions','Tigers','Snakes','Birds']
animals=dict(zip(voice,name))
animal_voice=input('What did you hear ? ').strip()
voices=animal_voice.split()
animal=[]
for voice in voices:
    animal.append(animals[voice.strip()])
animal_name=' '.join(animal)
print(animal_name.strip())