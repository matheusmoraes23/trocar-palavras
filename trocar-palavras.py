#!/usr/bin/python
# -*- coding: utf-8 -*-

## Lista de frases

frase_facil = 'Mais __0__ um __1__ na __2__ do que dois __3__.'
frase_medio = \
    "Os __0__ são   __1__ junto com  os seus amiguinhos  __2__ e   __3__ . "
frase_dificil = \
    "Os __0__ serão os __1__ assim eu espero, a vida é uma __2__ __3__ ."

frases = [frase_facil, frase_medio, frase_dificil]

### Lista de resposta

respostas_facil = ['vale', 'pássaro', 'mão', 'voando']
respostas_medio = ['gatos', 'fofos', 'felino', 'canino']
respostas_dificil = ['últimos', 'primeiros', 'roda', 'gigante']

resposta_jogo = [respostas_facil, respostas_medio, respostas_dificil]

# Lista com nível,frases, espaço

nivel = ['fácil', 'médio', 'difícil']
espaco = ['__0__', '__1__', '__2__', '__3__']
erro = 'Resposta incorreta , Tente novamente !'


def jogar_nivel(user_level):
    if user_level == 'fácil':
        print (frase_facil)
        resposta_jogo = respostas_facil
        frases = frase_facil
        jogo(frases, nivel, resposta_jogo)
    if user_level == 'médio':
        resposta_jogo = respostas_medio
        print (frase_medio)
        frases = frase_medio
        jogo(frases, nivel, resposta_jogo)
    if user_level == 'difícil':
        resposta_jogo = respostas_dificil
        print (frase_dificil)
        frases = frase_dificil
        jogo(frases, nivel, resposta_jogo)


def jogo(frases, nivel, resposta_jogo):
    indice = 0
    contador = 3
    while indice <= len(resposta_jogo):
        user_resposta1 = \
            input('Que palavra completa o campo __{}__ ? '.format(indice)).lower()
        if user_resposta1 == resposta_jogo[indice]:
            print ('A frase esta assim:')
            print (trocar_palavras_game(frases, indice, resposta_jogo))
            indice += 1
            print ('Bom trabalho !')
        else:
            print ('Suas chances =>', contador)
            contador -= 1
            print (erro)
            if contador == -1:
                print ('Fim de jogo :(')
                boas_vinda(jogar_nivel, jogo)
                break
        if user_resposta1 == resposta_jogo[-1]:
            print ("Boa você terminou o game :D")
            print ('Tente outras dificuldades !')
            boas_vinda(jogar_nivel, jogo)


def trocar_palavras_game(frases, indice, resposta_jogo):
    resposta_troca = resposta_jogo[indice]
    blank = espaco[indice]
    while indice <= len(blank):
        nova_frase = frases.replace(blank, resposta_troca)
        return nova_frase
        break


def boas_vinda(jogar_nivel, jogo):
    print ("PROJETO PARA O  CURSO INTRODUÇÃO DA PROGRAMAÇÃO")
    print ("Escreva em letra minúscula e não se esqueça dos acentos")
    print ('Feito por Matheus Moraes')
    user_level = \
        input("Níveis para jogar => fácil // médio // difícil // sair : "
              )
    if user_level == 'sair':
        raise SystemExit
    if user_level not in nivel:
        print ("Tente fácil//médio//difícil...")
        return boas_vinda(jogar_nivel, jogo)
    else:
        jogar_nivel(user_level)


boas_vinda(jogar_nivel, jogo)
