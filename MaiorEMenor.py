primeiro = int(input("Digite o primeiro valor: "))
segundo = int(input('Digite o segundo valor: '))
terceiro = int(input('Digite o terceciro valor: '))

#VERIFICA O MENOR
menor = primeiro
if segundo < primeiro:
    menor = segundo
if terceiro < primeiro:
    menor = terceiro
print(f'O menor número é {menor}')

#VERIFICA O MAIOR
maior = primeiro
if segundo > primeiro:
    maior = segundo
if terceiro > primeiro: 
    maior = terceiro
print(f'O maior número é {maior}')