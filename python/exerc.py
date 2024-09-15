# num = int(input('digite um numero:'))
# if num % 2 == 0:
#     if num > 0: 
#         print('O numero, {} , é par e positivo!'. format(num)) 
#     else:
#         print('O numero é par e negativo!')
# else:
#     if num > 0: 
#         print ('O numero é impar e positivo!')
#     else:
#         print('O numero é impar e negativo!')    

# num1 = int(input('Digite um numero: '))
# num2 = int(input('Digite outro numero: '))
# contador = 0

# if num1<num2:
#     while num1<=num2:
#         if num1%2 == 0:
#             contador+=1
#             print (contador)
#         num1+=1
# elif num2<num1:
#     while num2<=num1:
#         if num2%2 == 0:
#             contador+=1
#             print(contador)
#         num2+=1

# pes = hab = nf = count = maior = 0
# repetir = True

# while(repetir):
#     sal = int(input('Digite o salário: '))
#     if sal > 0:
#         hab+=1
#         pes+=sal    
#     elif sal < 0:
#         break
#     num = int(input('Digite o numero de filhos: '))
#     nf+=num
#     if sal <= 150:
#         count+=1
#     if sal > maior:
#         maior = sal

# print('A soma do salário dessas {} pessoas, equivale a {}'.format(hab,pes), end=', ')
# print('a media de salário dessa população é igual a {:.2f}'.format(pes/hab))
# print('A media do número de filhos é igual a {:.1f}'.format(nf/hab))
# print('O percentual de pessoas com salário menor que R$150,00 é igual a {} %'.format((count/hab)*100))
# print('O maior salário foi de {}'.format(maior))