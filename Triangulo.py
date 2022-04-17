print('-=' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-='* 20)
a = float(input('Primeiro segmento:  '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print(f'Os segmentos {a}, {b}, {c}, podem formar um triângulo!')
else: 
    print(f'Os segmentos {a}, {b}, {c}, não podem formar um triângulo !')
