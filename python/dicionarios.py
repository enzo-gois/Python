# dicionario = {'chave1' : 1, 'chave2' : 2, 'chave3' : 3}
# print(dicionario)

# dicionario = dict () #ou dicionario = {} 
# dicionario ['chave1'] = 1
# dicionario ['chave2'] = 2
# dicionario ['chave3'] = 3
# print(dicionario)

# telefones = {}
# print(type(telefones))
# telefones ['Lucas'] = '(81) 9999-9999'
# print(telefones['Lucas'])

# telefones = {'Lucas' : '(81) 9999.9999', 'João' : '(81) 9999.8888', 'Maria' : '(82) 9999.7777'}
# telefones_aux = {'Carlos' : ['(81) 9999.8764', '(87) 9999.6374'], 'Joana' : ['(87) 9993.6483', '(87) 9993.2343']}
# print(telefones)
# print(telefones_aux)
# telefones.update(telefones_aux)
# print(telefones)
# print(telefones['Joana'][0])
# print(telefones['Joana'][1])

# telefones = {'Lucas' : '(81) 9999.9999', 'João' : '(81) 9999.8888', 'Maria' : '(82) 9999.7777'}
# for telefone in telefones:
#     print(telefone)
# print(telefones.keys())

# telefones = {'Lucas' : '(81) 9999.9999', 'João' : '(81) 9999.8888', 'Maria' : '(82) 9999.7777'}
# for n in telefones:
#     print(telefones[n])
# print(telefones.values())

'''REMOVENDO ELEMENTOS'''
# telefones = {'Lucas' : '(81) 9999.9999', 'João' : '(81) 9999.8888', 'Maria' : '(82) 9999.7777'}
# print(telefones)
# telefones.pop('Lucas')
# print(telefones)
# del telefones['João']
# print(telefones)

# telefones = {'Lucas' : '(81) 9999.9999', 'João' : '(81) 9999.8888', 'Maria' : '(82) 9999.7777'}
# print(telefones)
# if 'Carlos' in telefones:
#     telefones.pop('Carlos')
# else:
#     print('A chave não existe!')

# telefones = {'Lucas' : '(81) 9999.9999', 'João' : '(81) 9999.8888', 'Maria' : '(82) 9999.7777'}
# print(telefones.get('Lucas', "Não existe no dicionario! "))
# print(telefones.get('Sérgio', "Não existe no dicionario! "))

'''QUESTÃO 1''' 
# dicionario = {'Edielson' : 'Preto', 'Joel' : 'Cinza', 'Ian' : 'Roxo', 'Eu' : 'Cinza'}
# print(dicionario)
# print(dicionario.keys())
# print(dicionario.values())

'''QUESTÃO 2'''
# semana = {}
# semana ['Segunda'] = '- Matemática'; semana ['Terça'] = '- Informática e Inglês'; semana ['Quarta'] = '- Inovação e startup e Programação' 
# semana ['Quinta'] = '- Programação'; semana ['Sexta'] = '- Programação e Lógica da briza'
# for i in semana:
#     print(i,end=' ') ; print(semana[i])

'''QUESTÃO 3'''
filmes = {}


# nome = input('Digite o nome do filme: ')
# vilao = input('Digite o nome do vilao: ') 
# ano = input('Digite o ano do filme: ')
# filmes[nome] = [vilao,ano]
# print(filmes)


'''QUESTÃO 4'''
# dicionario = {}
# numeros = [] 
# nome = input('Digite um nome: ')
# numeros = int(input('Digite um numero de telefone para essa pessoa: '))
# dicionario [nome] = numeros
# print(dicionario)
# while True:
#     c = input('Deseja inserir um novo contato? s/n ')
#     if c == 's':
#         while c == 's':
#             nome = input('Digite um nome: ')
#             if nome == '':
#                 break
#             num = int(input('Quantos telefones essa pessoa possui: '))
#             for i in range(num):
#                 #numeros.append(input('Digite o telefone dessa pessoa: '))
#                 dicionario [nome] = numeros = input('Digite o telefone dessa pessoa: ')
#                 print(dicionario)
#     if c == 'n':
#         print(dicionario)

