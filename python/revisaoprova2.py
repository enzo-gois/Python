def cumsum(lista):
    nova = []
    for i in lista:
        nova.append(sum(lista[:i]))
    print(nova)

#cumsum([1, 2, 3, 4])

def tupla(t):
    nova = []
    tup = list(t)
    for i in tup:
        if i not in nova:
            nova.append(i)
    nova = tuple(nova)
    # print(nova)
    # print(nova[::-1])

t = (1, 2, 2, 3, 4, 3, 5)
tupla(t)


def menu():
    print('MENU: \n')
    print('[1] - Incluir novo nome')
    print('[2] - Incluir telefone')
    print('[3] - Excluir telefone')
    print('[4] - Excluir nome')
    print('[5] - Exibir agenda')
    print('[6] - consultar telefones')
    print('[7] - sair ')


def exibiragenda():
    print(agenda)


def consultarTelefones():
    nome = input('Digite um nome: ')
    if nomeExiste(nome):
        print(agenda[nome])
    else:
        print('O nome não existe na agenda! ')


def nomeExiste(nome):
    if nome in agenda:
        return True
    else:
        return False


def IncluirNovoNome():
    nome = input("Digite um nome: ")
    if nomeExiste(nome):
        print('O nome já existe na agenda: ')
    else:
        agenda[nome] = []


def inlcuirTelefone():
    nome = input('Digite um nome: ')
    telefone = input('Digite um telefone: ')
    if nomeExiste(nome):
        agenda[nome].append(telefone)
    else:
        agenda[nome] = [telefone]


def excluirNome():
    nome = input('Digite um nome: ')
    if nomeExiste(nome):
        agenda.pop(nome)
    else:
        print('O contato não existe na agenda!')


def excluirTelefone():
    nome = input('Digite um nome: ')
    telefone = input('Digite o telefone a ser excluido: ')
    if nomeExiste(nome):
        if telefone in agenda[nome]:
            del agenda[nome][agenda[nome].index(telefone)]
        else:
            print('O telefone não pertence ao contato mencionado!')
    else:
        print('O contato não existe na agenda!')


agenda = {}

# while True:
#     menu()
#     opcao = int(input('Digite uma opção: '))
#     if opcao == 1: IncluirNovoNome()
#     if opcao == 2: inlcuirTelefone()
#     if opcao == 3: excluirTelefone()
#     if opcao == 4: excluirNome()
#     if opcao == 5: exibiragenda()
#     if opcao == 6: consultarTelefones()
#     if opcao == 7: break


def inverter(elem):
    if len(elem) == 1:
        return elem[0]
    else:
        return str(elem[-1]) + str(inverter(elem[:-1]))
# print(inverter([1,2,3,4,5]))


x = open('Palavras.txt', 'w+')
x.write('enzo\nlucas\nprogramacao\nword\n')
x.close()

with open('Palavras.txt', 'r') as file:
    file.seek(0)
    nova = []
    c= 0
    for linha in file:
        c+=1
        values = linha.strip()
        nova.append(values)
        maior = 0
        maior_palavra = ''
        for i in range (len(nova)):
            if len(nova[i]) > maior: 
                maior = len(nova[i]) 
                maior_palavra = nova[i]
    #print(maior)
    #print(maior_palavra)
    #print(c)
