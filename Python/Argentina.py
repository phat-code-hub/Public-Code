RATE=50 # Accoding to the question
peso=int(input('Peso: '))
dollar=int(input('Dollar: '))
change_to_Peso=dollar*RATE
decide='Pesos'
if peso > change_to_Peso:
    decide='Dollars'
print(decide)
