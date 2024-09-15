# s = 'Lógica de programação!'

# print(s[0])
# print(s[0:6])
# print(s[:6])
# print(s[-1])
# print(s[-12:-1])
# print(s[-12:])

# s = 'Lógica de programação!'
# i = 0
# while i != len(s):
#     print(s[i], end='-')
#     i+=1

# s = 'Lógica de programação!'
# i = 0
# while i != len(s):
#     print(s[-1])
#     i+=1

# s = 'Lógica de progamação'
# for i in range (len(s)):
#     print(s[i])

# s = 'Lógica de programação!'
# for i in range (len(s)):
#     print(s[-i-1], end='-')

# s = input('Digite um nome: ')
# s1 = input('Digite outro nome: ')
# print('{} possui {} caracteres!'.format(s, len(s)))
# print('{} possui {} caracteres!'.format(s1, len(s1)))
# if len(s) == len(s1):
#     print('As palavras possuem o mesmo numero de caracteres!')
# else:
#     print('Elas não possuem o mesmo numero de caracteres!')
# if s == s1:
#     print('O conteúdo das duas strings é igual!')
# else:
#     print('O conteúdo das duas strings são diferentes!')


# s = input('Digite um nome: ')
# for i in range (len(s)):
#     print(s.upper()[-i-1],end='')

# s = input('Digite um nome: ')
# for i in range(len(s)):
#     print(s[:i+1])

# s = input('Digite um nome: ')
# for i in range(len(s)):
#    print(s[i:])


# s = input('Digite uma string: ')

# # for i in range (len(s)):
# #     print(s[i], end=' ')
# if s == (s[::-1]):
#     print('é um palíndromo!')
# else:
#     print('Não é um palíndromo!')

# s = input('Digite um nome: ')
# for i in range (len(s)):
#     if s == (s[-i-1]):


# s = input('Digite uma cadeia de DNA: ').upper()
# print(f'ENTRADA: {s} ')
# s = s.replace('A', 't')
# s = s.replace('T', 'a')
# s = s.replace('C','g')
# s = s.replace('G', 'c')
# print(f'SAIDA: {s.upper()}')

# lista = []
# acima_da_media = []
# menor_sete = []
# s = 0
# m = 1
# c = 0
# while (True):
#     n = int(input('Digite um numero: '))
#     if n > 0:
#         lista.append(n)
#         s+=n
#         c+=1
#     if n < 0:
#         break
# m = s/c
# for i in range(len(lista)):
#     if lista[i] > m:
#         acima_da_media.append(lista[i])
#     if lista[i] < 7:
#         menor_sete.append(lista[i])

# print(f'Os numeros digitados foram: {lista} ')
# print(f'Os numeros digtados apresentados de traz para frente é: {lista[::-1]}')
# print(f'A soma dos numeros digitados é igual a {s} ')
# print(f'A media dos numeros digitados é igual a {m} ')
# print(f'Os valores digitados que estão acima da media são {acima_da_media} ')
# print(f'Dentre os valores digitados que são menores que sete são: {menor_sete} ')
# print('=-'*20)
# print('O PROGRAMA ACABOU!!!! ')
# print('=-'*20)

# n = int(input('Digite um numero: '))
# s = 1
# for i in range (1,n+1):
#     for c in range(1,i+1):
#         print(s, end = ' ')
#         s+=1
#     print()

# lista = []
# maiorIndex = s = 0
# menorIndex = 10
# nome = input('Digite o nome do atleta: ')
# for i in range(0,7):
#     n = float(input(f'Digite o valor do salto: '))
#     lista.append(n)
#     if i == 0:
#         maior = menor = lista[i]
#     else:
#         if lista[i] > maior:
#             maior = lista[i]
#         if lista[i] < menor:
#             menor = lista[i]
# print(f'Atleta: {nome} ')

# for t in range(len(lista)):
#     print(f'Nota: {lista[t]} ')

# for i in range(len(lista)):
#     if lista[i] == maior:
#         del lista[i]

# for c in range(len(lista)):
#     if lista[c] == menor:
#         del lista[c]

# for g in range(len(lista)):
#     s += lista[g]

# print(f'=-'*20)
# print(f'RESULTADO FINAL')
# print(f'=-'*20)
# print(f'Atleta: {nome} ')
# print(f'Melhor nota: {maior} ')
# print(f'Pior nota: {menor} ')
# m = s/5
# print(f'Média: {m} ')

# lista = []
# for i in range(7):
#     lista.append(int(input('Nota do jurado: ')))

