velocidade = int(input('Insira a velocidade em KM: '))
if velocidade > 80:
    print('Você foi multado! Pois ultrapassou o limite de 80km/h.')
    print(f'Você deve pagar R${(velocidade-80) *7}')
else: 
    print('Você manteve a velocidade permitida.')