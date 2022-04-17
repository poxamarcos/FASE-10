salario = float(input('Qual é o valor do salario atual? '))
if salario > 1250:
    novo = salario + (salario * 10 /100)
    print('O salario passa a ficar {:.2f}'.format(novo))
if salario <= 1250:
    novo = salario + (salario*15/100)
    print('O salario passa a ficar {:.2f}'.format(novo))