# num1 = int(input('Digite um numero: '))
# num2 = int(input('Digite outro numero: '))
# num3 = int(input('Digte um terceiro numero: '))
# if num1 > num2 and num1 > num3:
#     if num2 > num3:
#         print (num3, num2, num1)
#     else:
#         print (num2, num3, num1)
# elif num2 > num1 and num2 > num3:
#     if num1 > num3:
#         print (num3, num1, num2)
#     else:
#         print (num1, num3, num2)
# elif num3 > num1 and num3 > num2:
#     if num1 > num2:
#         print(num2, num1, num3)
#     else:
#         print (num1, num2, num3)
#

# num1 = int(input("digite um numero: "))
# num2 = int(input("digite outro numero: "))
# num3 = int(input("digite outro numero: "))
# soma = (num1 + num2 + num3)
# print (soma)

# n = int(input('Digite um numero: '))
# result = 1
# for n in range(1,n+1):
#     result *= n
# print(result)


# n = 1
# par = impar = 0
# while n != 0:
#     n = int(input('Digite um valor: '))
#     if n != 0:
#         if n % 2 == 0:
#             par +=1
#         else:
#             impar +=1
# print('Voce digitou {} numeros pares e {} numeros impares!'. format(par, impar))

# n = int(input('Digite um numero para ver a tabuada: '))
# for i in range(1,11):
#     print('{} x {} = {}'.format(n, i, n*i))

# c = 0
# for i in range(1,501):
#     if i %2==1:
#         if i %3 == 0:
#             c+=i
# print(c)

# ano = int(input('Digite um ano: '))
# if ano %4 == 0:
#     print(f'O ano {ano} é bissexto! ')
# else:
#     print(f'o ano {ano} não é bissexto! ')

# for i in range(1,11):
#     for c in range(1,11):
#         print('{} x {} = {}'.format(i,c,i*c))

# seq = 1
# for i in range(1,11):
#     seq = (seq-1) + (seq-2)
#     print(seq)

# n = int(input('Digite um numero: '))
# s = 0
# for i in range(1,n):
#     if n % i == 0:
#         s+=i
# print(s)

# n = int(input('Digite um numero: '))
# h = 1
# s = 0
# for i in range(1,n+1):
#     h = 1 / i
#     s+=h
# print(s)

# lista = []
# s = 0
# c = 0
# n = int(input('Digite a quantidade de alunos: '))
# for i in range(0,n):
#     idade = int(input('Digite a idade: '))
#     altura = float(input('Digite a altura: '))
#     if idade >= 13:
#         lista.append(altura)
#     s+= altura
# media = s/n
# for t in range(len(lista)):
#     if t < media:
#         c+=1
# print(media)
# print(lista)
# print(f'{c} alunos com mais de 13 anos estão abaixo da média de altura! ')

# lista = []
# s = 0
# c = 0
# repetir = True
# while(True):
#     idade = int(input('Digite a idade: '))
#     if idade < 0:
#         break
#     altura = float(input('Digite a altura: '))
#     if idade >= 13:
#         lista.append(altura)
#     s+= altura
# media = s/(len(lista))
# for t in range(len(lista)):
#     if t < media:
#         c+=1
# print(media)
# print(lista)
# print(f'{c} alunos com mais de 13 anos estão abaixo da média de altura! ')

# mes = ['','janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setebro', 'outubro', 'novembro', 'dezembro']
# lista = []
# data = input('Digite a sua data de nascimento no formato Ex:dd/MM/aaaa: ')
# lista =data.split('/')
# print(f'Você nasceu em {lista[0]} de {mes[int(lista[1])]} de {lista[2]}')

# mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro' ]
# temperaturas = []
# acima_da_media = []
# t = 0
# for i in range(1,13):
#     temp = int(input(f'Digite a temperatura do mês {i}: '))
#     temperaturas.append(temp)
#     t += temp
# media = t/12
# for t in range(len(temperaturas)):
#     if t > media:
#         acima_da_media.append(t)
# print(temperaturas)
# print(media)
# print(acima_da_media)


# saltos = []
# s = 0
# nome = input('Digite o nome do atleta: ')
# for i in range(0,5):
#     salto = float(input('Digite a distancia do salto: '))
#     saltos.append(salto)
#     s+=salto
# media = s/5
# print(f'Atleta: {nome} \n ')
# print(f'Primeiro Salto: {saltos[0]} ')
# print(f'Segundo Salto: {saltos[1]} ')
# print(f'Terceiro Salto: {saltos[2]} ')
# print(f'Quarto Salto: {saltos[3]} ')
# print(f'Quinto Salto: {saltos[4]} \n ')
# print('Resultado Final: ')
# print(f'Atleta: {nome} ')
# print(f'Saltos: {saltos[0]}, {saltos[1]}, {saltos[2]}, {saltos[3]}, {saltos[4]} ')
# print(f'Média dos Saltos: {media:.2f} ')

# vetor = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
# vetor2 = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
# n = int(input('Digite um numero entre 0 e 99: '))
# if n < 0 or n > 99:
#     print('NÚMERO INVÁLIDO! ')
# if n >= 0 and n <= 19:
#     print(vetor[n])
# if n > 20 and n <= 29:
#     print(vetor2[0], 'e', vetor[n-20])
# elif n == 20:
#     print(vetor2[0])
# if n > 30 and n <= 39:
#     print(vetor2[1], 'e', vetor[n-30])
# elif n == 30:
#     print(vetor2[1])
# if n > 40 and n <= 49:
#     print(vetor2[2], 'e', vetor[n-40])
# elif n == 40:
#     print(vetor2[2])
# if n > 50 and n <= 59:
#     print(vetor2[3], 'e', vetor[n-50])
# elif n == 50:
#     print(vetor2[3])
# if n > 60 and n <= 69:
#     print(vetor2[4], 'e',vetor[n-60] )
# elif n == 60:
#     print(vetor2[4])
# if n > 70 and n <= 79:
#     print(vetor2[5], 'e', vetor[n-70])
# elif n == 70:
#     print(vetor2[5])
# if n > 80 and n <=89:
#     print(vetor2[6], 'e', vetor[n-80])
# elif n == 80:
#     print(vetor2[6])
# if n > 90 and n <= 99:
#     print(vetor2[7], 'e', vetor[n-90])
# elif n == 90:
#     print(vetor2[7])

# p1 = []
# p2 = []
# p3 = []
# p4 = []
# count = count1 = count2 = count3 = count4 = 0
# while True:
#     m = (input('Digite o numero de identificação do mouse:\n 1: necessita da esfera\n 2: necessita de limpeza\n 3: necessita troca de cabo\n 4: quebrado'))
#     if int(m) == 1:
#         p1.append(m)
#         count1+=1
#         count+=1
#     if int(m) == 2:
#         p2.append(m)
#         count2+=1
#         count+=1
#     if int(m) == 3:
#         p3.append(m)
#         count3+=1
#         count+=1
#     if int(m) == 4:
#         p4.append(m)
#         count4+=1
#         count+=1
#     if int(m) == 0: break
# print(f'Quantidade de mouses: {count} ')
# print('SITUAÇÃO:                                   Quantidade           Percentual')
# print(f'1 - necessita da esfera                         {count1}                   {(count1/count)*100:.2f}% ')
# print(f'2 - necessita de limpeza                        {count2}                   {(count2/count)*100:.2f}% ')
# print(f'3 - necessita troca de cabo ou conector         {count3}                   {(count3/count)*100:.2f}% ')
# print(f'4 - quebrado ou inutilizado                     {count4}                   {(count4/count)*100:.2f}% ')


# n = int(input('Digite o termo: '))
# ultimo = 1
# penultimo = 1

# for i in range(2, n):
#     termo = ultimo + penultimo
#     penultimo = ultimo
#     ultimo = termo
# print(termo)

# def func(lista):
#     if len(lista) == 1:
#         return lista[0]
#     else:
#         return str(lista[-1]) + str(func(lista[0:-1]))
# print(func([1,3,5,7,9]))
