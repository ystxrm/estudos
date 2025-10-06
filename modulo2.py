#manipular- add novos itens
salarios = [1500, 3000, 5000, 5500]
salarios_funcionarios = float(input('qual é seu salario: '))
salarios.append(salarios_funcionarios)
print(salarios)

#problema - Gastos totais com pagamentos de salários.
#dado uma lista de salários, calcule o total pago a todos

salarios = [1500, 3000, 5000, 5500]
total = 0
for salario in salarios:
    total = total + salario
print(total)

#primeiro projeto em python

numero = int(input('digite o fatorial que deseja calcular: '))
if numero > 0 and type(numero) == int:
    fatorial = 1
    for item in range(1, numero+1):
        print(f'{fatorial} * {item}')
        fatorial = fatorial * item
        print(f'{fatorial}')
        print(f'o fatorial de {numero} é {fatorial}')
    else:
        print('favor informar apenas numeros positivos')
