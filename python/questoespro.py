'''QUESTÃO 1'''
# with open("notas_estudantes.txt",'r') as file:
#     file.seek(0)
#     for linha in file:
#         values = linha.split()
#         if len(values) > 7:
# print(values[0])

'''QUESTÃO 2'''

# with open("notas_estudantes.txt",'r') as file:
#     for line in file:
#         values = line.split()
#         sum = 0
#         for val in range(1,len(values)):
#             sum+=int(values[val])
#print(f'O estudante {values[0]} possui média {sum/(len(values)-1)} ')

'''QUETSÃO 3'''
# with open("notas_estudantes.txt",'r') as file:
#     file.seek(0)
#     for line in file:
#         values = line.split()
#         max = int(values[1])
#         min = int(values[1])
#         for val in range(2,len(values)):
#             if int(values[val]) > max: max = int(values[val])
#             if int(values[val]) < min: min = int(values[val])
#print(f'O estudante {values[0]} possui nota máxima {max} e nota minima {min} ')

s = 'gadf'
s = list(s)


def is_sorted(par):
    if s == sorted(s):
        print('Está na ordem correta! ')
    else:
        print('Está na ordem errada! ')
# is_sorted(s)


def is_palindrome(p):
    return p.replace(' ', '') == p[::-1].replace(' ', '')
#print(is_palindrome('subi no onibus'))

def most_frequent(s):
    ordem = dict()
    for i in s:
        ordem[i] = s.count(i)
    listafreq = []
    for x,freq in ordem.items():
        listafreq.append((freq,x))
    listafreq.sort(reverse=True)
    print(listafreq)
    for freq,x in listafreq:
        print(x,end='')
#most_frequent('bsdpywiqgfbçasiudofhgaiw')

def soma_list(t):
    c = 0
    for i in range(len(t)):
        c += sum(t[i])
    print(c)
#soma_list([[1,2],[3],[4,5,6]])

from math import factorial
def combinaao(n,p):
    c = factorial(n)/(factorial(p)*factorial(n-p))
    print(c)
#combinaao(10,4)

def funcao(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end='')
        print()
#funcao(5)

