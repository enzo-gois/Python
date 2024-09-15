# tupla = 1,3,2,3,5,1,1,3
# lista = list(tupla)
# nova = []
# count = 0
# for i in (lista):
#     if i not in nova:
#         nova.append(i)
# print(nova)

# lista = [2,1,1,2]
# print (list(set(lista)))

# lista = [9,5,6]
# tupla = ()
# for i in range(len(lista)):
#     tupla += (lista[i], lista[i]**3),
# #print(tupla)
# nova = list(tupla)
# print(nova)

'''
LISTA 29/09/2022
'''



# preco = float(input('Digite o preço do pão: '))
# print('Preço do pão: ')
# for i in range(1,51):
#     print(f'{i} - R$ {i*preco:.2f} ')



# string = input('Digite alguma coisa: ').lower()
# cont = ''
# cont = string.count(' ')
# print(f'Existem {cont} espaços em branco! ')
# cont = string.count('a')
# print(f'Existem {cont} caracteres A!')
# cont = string.count('e')
# print(f'Existem {cont} caracteres E!')
# cont = string.count('i')
# print(f'Existem {cont} caracteres I!')
# cont = string.count('o')
# print(f'Existem {cont} caracteres O!')
# cont = string.count('u')
# print(f'Existem {cont} caracteres U!')


'''cpf = input('Digite um cpf no formato xxx.xxx.xxx-xx : ').replace('.','').replace('-','')
lista = []
nova = []
nova2 = []
m = 10
for i in range(9):
    lista.append(int(cpf[i]))
for t in range(len(lista)):
    result = lista[t]*(m-t)
    nova.append(result)
lista.append(int(cpf[9]))
for c in range(10):
    result = lista[c]*(11-c)
    nova2.append(result)
p1 = sum(nova)%11
digito1 = 11 - p1
p2 = sum(nova2)%11
digito2 = 11 - p2
if digito2 > 10:
    digito2 = 0
if digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
    print('CPF VÁLIDO!')
else:
    print('CPF INVÁLIDO!')'''
# print(digito1, digito2)
# print(lista)
# print(nova)
# print(nova2)

# lista = ['onze','eu','programa','ezno','ue','python','amargorp']
# nova = []
# for i in range(len(lista)):
#     if lista[i] and lista[i][::-1] in lista:
#         if lista[i] and lista[i][::-1] not in nova:
#             nova.append(lista[i])
#             nova.append(lista[i][::-1])
# print(nova)

# t = f = []
# nova = []
# for i in range(20):
#     t.append(int(input('Digite um valor: ')))
# for i in range(len(t)):
#     if t[i] > 0:
#         nova.append(t[i])
# f = set(nova)
# f = list(f)
# print('pos:',nova)
# print('semdup:',f)

# tupla1 = (input('Digite os valores da tupla 1 separados por ,: ')).split(',')
# tupla2 = (input('Digite os valores da tupla 2 separados por ,: ')).split(',')
# fin = []
# for i in range(len(tupla1)):
#     fin.append(int(tupla1[i]))
#     fin.append(int(tupla2[i]))
# print(tuple(fin))
# print(tupla1)
# print(tupla2)

# tupla1 = (input('Digite os valores da tupla 1 separados por ,: ')).split(',')
# tupla2 = (input('Digite os valores da tupla 2 separados por ,: ')).split(',')
# fin = []
# for i in range(len(tupla1)):
#     if tupla1[i] not in fin:
#         fin.append(int(tupla1[i]))
#     if tupla2[i]  not in fin:
#         fin.append(int(tupla2[i]))
# print(tuple(fin))

num = int(input('Digite um numero inteiro: '))
i = 1
c = 0
print(num//i)
