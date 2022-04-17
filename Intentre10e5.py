from random import randint
from time import sleep
pensou = randint(0, 5)
numero = int(input('Escolha um número entre 0 e 5: '))
print('Processando...')
sleep(3)

if numero == pensou:
    print('Parabéns, você acertou!!')
else:
    print (f'Você errou. Eu escolhi o número: {pensou}, e você digitou: {numero}')