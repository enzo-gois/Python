'''QUESTAÕ 1'''
# def aocubo(p):
#     novo = []
#     for i in p:
#         x = (i,i**3)
#         novo.append(x)
#     return (novo)
#print(aocubo([1,2,3]))


'''QUESTÃO 2'''
# def elevado(m,n):
#     if n == 0:
#         return 1
#     else:
#         return m * elevado(m,n-1)
# m = int(input('Digite um numero: '))
# n = int(input('Digite a base: '))
#print(elevado(m,n))

'''QUESTÃO 3'''

arquivo = open("backup.txt","w")
arquivo.close()

''' A '''
dic = {}

def inserirNovoUsuario():
    while True:
        nome = input('Digite um nome: ')
        dic[nome] = []
        s = input('Deseja adicionar um apelido: s/n ')
        if s == 's':
            nick = input('Digite o apelido: ')
            dic[nome].append(nick)
        else:
            dic[nome] = ['n/a']
        idade = int(input('Digite sua idade: '))
        dic[nome].append(idade)
        cpf = input('Digite seu CPF: ')
        dic[nome].append(cpf)
        return (dic)

''' C '''
def visualizarUsuarios():
    for i,c in dic.items():
        print(f'Nome: {i}   apelido: {c[0]}   idade: {c[1]}   cpf: {c[2]}')

''' D '''
def visualizarBackup():
    with open("backup.txt","r") as file:
        file.seek(0)
        for i in file:
            i = file.readline()
            print(i)
            
def usuariosBackup():
    for i,c in dic.items():
        print(f'Nome: {i}   apelido: {c[0]}   idade: {c[1]}   cpf: {c[2]}')
    with open("backup.txt","r") as file:
        file.seek(0)
        for i in file:
            i = file.readline()
            print(i)

''' E '''
def menu():
    print('MENU: \n')
    print('[1] - Inserir uma nova pessoa ')
    print('[2] - Visualizar usuários cadastrados ')
    print('[3] - Visualizar apenas backup')
    print('[4] - visualizar usuarios e backup')
    print('[5] - Sair')


while True:
    menu()
    c = int(input('Digite um numero: '))
    if c == 1: inserirNovoUsuario()
    if c == 2: visualizarUsuarios()
    if c == 3: visualizarBackup()
    if c == 4: usuariosBackup()
    if c == 5: break
    ''' B '''
    if len(dic.keys()) == 5:
        with open("backup.txt","a+") as file:
            for i,c in dic.items():
                file.write(f'Nome: {i}   apelido: {c[0]}   idade: {c[1]}   cpf: {c[2]} \n')
    

        