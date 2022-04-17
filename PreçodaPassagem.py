distancia = int(input('Qual a distância da sua viagem? '))
if distancia <= 200:
    print (f"""Você está prestes a fazer uma viagem de {distancia}KM.
    E o preço da sua passagem será de R$:{distancia*0.50}""")
else:
    print(f"""Você está prestes a fazer uma viagem de {distancia}KM.
    E o preço da passagem será de R$: {distancia*0.45}""")