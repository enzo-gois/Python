
# arquivo = open("palavras_forca","w")
# arquivo.close()

import random

def dica():
    lista = []
    with open("palavras_forca", "r", encoding="utf-8") as file:
        linhas = file.readlines()
        for linha in linhas:
            linha = linha.strip()
            lista.append(linha)
            sorteada = random.choice(lista)
            sorteada = sorteada.split()
        return sorteada

def jogando():
    palavra = dica()
    dica_palavra = palavra[1]
    palavra_secreta = palavra[0].upper()
    print(f'A dica é: {dica_palavra} ')
    print('A palavra é: ', "_ " * len(palavra_secreta))
    print()
    digitadas = []
    chances = 6

    while True:
        chute = input("Digite um letra: ").upper()
        digitadas.append(chute)
        chutes = ''
        for letras_chutadas in palavra_secreta:
            if letras_chutadas in digitadas:
                chutes+= letras_chutadas
            else: 
                chutes+= '_ '
        if chutes == palavra_secreta:
            print(f'A palavra era {chutes} ')
            print('Parabéns você Ganhou!')
            break
        else:
            print(f'A palavra esta assim: {chutes} ')
        if chute not in palavra_secreta:
            chances-=1
            print(f'Ainda restam {chances} tentativas! ')
        if chances == 0:
            print('Voce perdeu! FORCA!')
            break
        print()

jogando()

