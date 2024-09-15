# arquivo = open("notas_estudantes","w")
# arquivo.write("Jose 10 15 20 30 40\n")
# arquivo.write("pedro 23 16 19 22\n")
# arquivo.write("suzana 8 22 1714 32 17 24 21 2 9 11 17\n")
# arquivo.write("gisela 12 28 2145 26 10\n")
# arquivo.write("joao 14 32 25 16 89\n")
# arquivo.close()

with open("notas_estudantes", "r") as file:
    file.seek(0)
    linha = file.readlines()
    for i in linha:
        print(linha)


'''QUESTÃO 01'''
# with open("notas_estudantes", "r") as file:
#     file.seek(0)
#     linha = file.readlines()
#     #print(type(linha))
#     for i in linha:
#         novo = i.split()
#         if len(novo) >= 8:
#             print(novo[0])

'''QUESTÃO 02'''
# c = 0
# with open("notas_estudantes", "r") as file:
#     file.seek(0)
#     linhas = file.readlines()
#     for i in linhas:
#         novo = i.split()
#         # print(novo)
#         inteiro = int(str(novo[1:]).replace("[","").replace("]",""))
#         print(inteiro)
