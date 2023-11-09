import os
import sys

dashboard =[[0, 0, 0],
            [0, 0, 0],  
            [0, 0, 0]]

def playerTurn(jogador):
    if jogador == 1:
        print('Vez do player 1')
        posicaoJogada = list(map(int, input("Informe a posicao que vc quer jogar (i,j): ").split()))
    else:
        print('Vez do player 2')
        posicaoJogada = list(map(int, input("Informe a posicao que vc quer jogar (i,j): ").split()))
    return posicaoJogada

def marcaJogada(jogador, posicao):
    dashboard[posicao[0]][posicao[1]] = jogador

def main():
    count = 0
    while True:
        jogador = 2
        if count % 2 == 0:
            jogador = 1
        
        for i in range(3):
            for j in range(3):
                print(dashboard[i][j], end='|')
            print()
        jogada = playerTurn(jogador)
        marcaJogada(jogador, jogada)
        count += 1


main()
