#Variavel
Nome_completo='Arthur de Oliveira Tome'
print(Nome_completo)
# Numeros Inteiros(int)
idade = 15
# Números Decimais(float)
nota = 5.4
# Texto(string)(str)
Nome_da_empresa = 'visual pvc'
# booleanos(True or False)(bool)
pode_acessar = False

print(pode_acessar)

#Problema 1:
#Escreva um programa que retorne o valor hora de um funcionário.
#Com base no seu salario mensal e hora trabalhadas por mês.

valor_salarial = input('digite seu salario: ')
horas_trabalhadas = input('digite sua hora trabalhada por dia: ')
valor_salarial_por_hora = float(valor_salarial)/int(horas_trabalhadas)
print(valor_salarial_por_hora)

#condicionais-if,elif,else

trabalho_terminado = False
if trabalho_terminado == True:
    print('bora!')
else:
    print('nao bora!')

    #como lidar com mais que 2 condições

advertencia = 0
if advertencia >= 3:
    print('Você esta Suspenso')
elif advertencia == 2 :
    print('você esta advertido, mas toma cuidado que na proxima você estara suspenso')
elif advertencia == 1 :
    print('Esta é sua primeira advertencia')
else:
    print('Você não esta advertido')

#While

#syntaxe
#while condicao:
#codigo a ser executado


        #caso real

usuario=''
senha = ''
tentativas = 0
while (senha != '12345' and usuario != 'Arthur O.') and tentativas <3:
        usuario= input('digite seu usuario: ')
        senha= input('digite sua senha: ')
tentativas +=1

if usuario != 'Arthur O.' and senha != '12345':
    print('aguarde 30 minutos')
else:
    print('login feito com sucesso')

    #listas
    precos = [20, 30, 40, 1500]
#python tabalha também com indice igual js, onde o 0 e contado como primeiro e o 1 e contado como o segundo da lista, assim sucessivamente, exemplo:
    print(precos[0]) #aqui aparece o primeiro que é o '20'.

    print(precos[1])# o segundo valor da lista.

    print(precos[2])# o terceiro valor da lista, e assim sucessivamente.

    #encontrando o indice automaticamente
    paises = ['Brasil', 'Argentina', 'Cuba', 'Alemanha'] #lembrando tem que colocar aspas em cada nome da lista, apenas nomes, números não são necessarios.
    print(paises.index('Cuba')) #aqui ele ira encontrar o indice automaticamente que será 2


