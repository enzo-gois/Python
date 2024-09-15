'''RECURSÃO'''

def listSum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listSum(numlist[1:])

#print(listSum([1,3,5,7,9]))


#numero = int(input('Digite um numero: '))
def listSum(num):
    if num == 1 or num == 0: #caso base
        return 1
    else:
        return num * listSum(num-1)
#print(listSum(numero))

'''EXERCICIOS'''

'''QUESTÃO 1'''
#m = int(input('Digite um valor para m: '))
#n = int(input('Digite um valor para n: '))

def div(m,n):
    if m < n:
        return 0
    else:
        return 1 + div(m-n,n)
#print(div(m,n))

'''QUESTÃO 2'''
def div(m,n):
    if n == 0 :
        return 1
    else:
        return m * div(m,n-1)
#rint(div(2,3))

'''QUESTÃO 3'''

def fibon(m):
    if m == 1 or m ==2:
        return 1
    else:
        return fibon(m-1) + fibon(m-2)
#print(fibon(5))

'''QUESTÃO 4'''

def binario(n):
    if n < 2:
        return n
    else:
        return (n % 2) + binario(n//2)*10
#print(binario(10))

'''QUESTÃO 5'''

# def func(lista):
#     if len(lista) == 1:
#         return lista[0]
#     else:
#         return str(lista[-1]) + str(func(lista[0:-1]))
# print(func([1,3,5,7,9]))

'''QUESTÃO 6'''


def vezes(n1, n2):
    if len(n1) <= 0:
        return 0
    if n2 == n1[-1]:
        return 1 + vezes(n1[0:-1], n2)
    else:
        return 0 + vezes(n1[0:-1], n2)

n1 = [7, 6, 2, 0, 2, 1, 1, 9, 2]
n2 = 2
lem = len(n1)
#print(vezes([7, 6, 2, 0, 2, 1, 1, 9, 2], n2))

'''QUESTÃO 7'''

# def mdc(a,b):
#     if a%b == 0: return b
#     else: return mdc(b,a%b)
# print(mdc(18,24))

'''QUESTÃO 8'''

def harmonico(n):
    if n == 1: return "Entrada inválida"
    if n == 2: return 1
    else: return 1/(n-1) + harmonico(n-1)
print(harmonico(4))