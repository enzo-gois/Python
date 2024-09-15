'''
QUESTÃO 1
'''
# n1 = float(input('DIgite o primeiro numero: '))
# n2 = float(input('Digite o segundo numero: '))
# n3 = float(input('Digite o terceiro numero: '))
# if n1 < n2 and n2 < n3:
#     print(n1,n2,n3)
# elif n1 < n3 and n3 < n2:
#     print(n1,n3,n2)
# elif n2 < n1 and n1 < n3:
#     print(n2,n1,n3)
# elif n2 < n3 and n3 < n1:
#     print(n2,n3,n1)
# elif n3 < n2 and n2 < n1:
#     print(n3,n2,n1)
# else:
#     print(n3,n1,n2)  

'''
QUESTÃO 2
'''
# t = 1 
# s = 0
# n1 = int(input('Digite um numero: '))
# n2 = int(input('Digite um segundo numero: '))
# if n1 < n2:
#     for i in range(n1,n2+1):
#         if i%2 == 0:
#             s+=i
#         if i%2 == 1:
#             t*=i
# else:
#     for i in range(n2,n1+1):
#         if i%2 == 0:
#             s+=i
#         if i%2 == 1:
#             t*=i
# print(f'Soma dos números pares: {s} ')
# print(f'Multiplicação dos ímpares: {t} ')

'''
QUESTÃO 3
'''
# c = s = 0
# lista = []
# while True:
#     n = float(input('Digite a nota: '))
#     if n >0:
#         lista.append(n)
#     if n < 0:
#         break
# print(f'Foram informados {len(lista)} números!')
# print(f'Os numéros digitados foram: {lista} ')
# print(f'Os numeros digitados na ordem inversa é: {lista[::-1]} ')
# print(f'A soma dos valores digitados pe igual a: {sum(lista)} ')
# media = sum(lista)/len(lista)
# print(f'A média dos valores digitados é igual a: {media} ')
# for i in range(len(lista)):
#     if lista[i] > media:
#         c+=1
#     if lista[i] < 7:
#         s+=1    
# print(f'Existem {c} valores acima da média calculada! ')
# print(f'Existem {s} valores menores que sete! ')


'''
QUESTÃO 4
'''
# cifra = ''
# lista = []
# alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# s = input('Digite uma string a ser ciptografada: ').upper()
# c = int(input('Digite o numero de rotações para a cifra: '))
# for i in range(len(s)):
#     cifra = alfabet.find(s[i])
#     lista.append(cifra)
# for i in range(len(lista)):
#     print(alfabeto[lista[i]+c],end='')
        







