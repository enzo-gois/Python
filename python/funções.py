# def eu(parametro):
#     print('Eu estou lendo', parametro)
#     return('Eu acabei de ler', parametro)
# print(eu(12))

# def produto (p1,p2):
#     res = p1*p2
#     return res

# def divisao (p1,p2):
#     if p2 == 0:
#         return
#     res = p1/p2
#     return res

# b = float(input('Digite o valor da base: '))
# h = float(input('Digite o valor da altura: '))
# p = produto (b,h)
# area = divisao (p,2)
# print(f'A área do tringulo é igual a {area} ')

# def calculoIMC(peso,altura):
#     return peso/altura**2
# print(calculoIMC(62,1.70))

# def calcularPagamento(qtd_horas,valor_horas):
#     horas = float(qtd_horas)
#     taxa = float(valor_horas)
#     if horas <= 40:
#         salario = horas*taxa
#     else:
#         hora_excendente = horas -40
#         salario = 40*taxa+(hora_excendente*(1.5*taxa))
#     return salario

# resultado = calcularPagamento(20,100)
# print(resultado)

'''EXERCÍCIOS'''

'''QUESTÃO 1'''
# def soma (v1,v2,v3):
#     result = v1+v2+v3
#     return result
# print(soma(4,6,9))

'''QUESTÃO 2'''
# def positivoOuNegativo(argumento):
#     if argumento > 0:
#         return 'P'
#     else:
#         return 'N'
# print(positivoOuNegativo(-5))

'''QUESTÃO 3'''
def escadinha(valor):
    s = 0
    for i in range(valor):
        s+=1
        for c in range(i+1):
            print (s, end=' ')
        print()
#escadinha(5)

'''QUESTÃO 4'''
def reverso (numero):
    numero = numero[::-1]
    print(numero)
val = input('Digite um numero: ')
#reverso(val)

'''QUESTÃO 5'''
# def jafiz(num):
#     i = 1
#     c = 0
#     while (True):
#         d = num//i
#         if d != 0:
#             c+=1
#             i*=10
#         if d == 0:
#             break
#     print(c)
# valor = int(input('Digite um numero inteiro: '))
# jafiz(valor)

'''QUESTÃO 6'''

def calculo(v1,v2):
    for i in range(1,v2+1):
        d = (v1*(v1*(i-1)))
    print(d)
# num1 = int(input('Digite o valor da base: '))
# num2 = int(input('Digite o valor do expoente: '))
#calculo(num1,num2)

'''QUESTÃO 7'''
# romanos = (
#     (1000,"M"),
#     (900,"CM"),
#     (500,"D"),
#     (400,"CD"),
#     (100,"C"),
#     (90,"XC"),
#     (50,"L"),
#     (40,"XL"),
#     (10,"X"),
#     (9,"IX"),
#     (5, "V"),
#     (4, "IV")
#     (1,"I")
# )

# for quociente,romano in romanos:


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''QUESTÃO 1'''
# ampm = [0, 1, 2, 3, 4, '5', '6', '7', '8', '9', '10', '11', '12']
# lista = [0, 1, 2, 3, 4, '5', '6', '7', '8', '9', '10', '11', '12',
#          '13', 14, '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
# horas = (input('Digite as horas: '))
# minutos = (input('Digite os minutos: '))
# hora = horas + ':' + minutos
# def conversão():
#     for i in range(len(lista)):
#         if int(horas) > 12:
#             if horas == str(lista[i]):
#                 novo = str(lista[i-12]) + ':' + minutos
#                 return novo
#         elif int(horas) < 12 and int(horas) != 0:
#             if horas == str(lista[i]):
#                 novo = str(ampm[i-13]) + ':' + minutos
#                 return novo
#         elif int(horas) == 0 or int(horas) == 12:
#             novo = '12' + ':' + minutos
#             return novo
# def ap():
#     if int(horas) >= 12 or int(horas) == 0:
#         pm = ' PM'
#         return pm
#     else:
#         pm = ' AM'
#         return pm
# print(conversão()+ap())

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''QUESTÃO 2'''

import random
# def jogo():
#     sorteio = random.randint(1, 6) + random.randint(1, 6)
#     print(sorteio)
#     if sorteio == 7 or sorteio == 11:
#         print('Você tirou um natural e ganhou! ') 
#     if sorteio == 2 or sorteio == 3 or sorteio == 12:
#         print('Você tirou um CRAPS e perdeu! ')
#     if sorteio == 4 or sorteio == 5 or sorteio == 6 or sorteio == 8 or sorteio == 9 or sorteio == 10:
#         print(f'Voce pontuou {sorteio} por isso jogara denovo! ')
#         while True:
#             r = random.randint(1,6) + random.randint(1,6)
#             print(r)
#             if r == 7:
#                 print('Voce perdeu!')
#                 break
#             if r == sorteio:
#                 print('Voce ganhou! ')  
#                 break    
# jogo()

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''QUESTÃO 3'''

# string = input('Digite uma palavra: ')
# lista = []
# def embaralhar(parametro):
#     for i in range(len(parametro)):
#         lista.append(parametro[i])
#         random.shuffle(lista)
#     nova = (str(lista).replace(' ','').replace('[','').replace(']','').replace("'",'').replace(',',''))
#     print(nova)
#     print(type(nova))
# embaralhar(string)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# def embaralhar(parametro):
#     lista = []
#     for i in range(len(parametro)):
#         lista.append(parametro[i])
#     random.shuffle(lista)
#     print(lista)
# string = input('Digite uma string: ')
# embaralhar(string)


# pal = 'hoje'
# tamanho = len(pal)
# for i in range(tamanho-1,-1,-1):
#     print(pal[i])
