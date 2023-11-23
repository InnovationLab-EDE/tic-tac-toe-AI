# (linha, coluna)
limit = (3, 3)
bord = [' ', 'X', 'O']
dashboard = []

def isTurnValid(point: list):
    if len(point) != 2:
        return False

    for i in range(2):
        if point[i] <= 0 or point[i] > limit[i]:
            return False

    if dashboard[point[0] - 1][point[1] - 1] > 0:
        return False

    return True

def playerTurn(jogador):
    print('Vez do player ', jogador, '(', bord[jogador], ')', sep='')

    point = []
    msg = "Informe a posicao (linha, coluna)(1..{lin}, 1..{col}): ".format(lin = limit[0], col =limit[1])

    while not isTurnValid(point):
        point = list(map(int, input(msg).split()))
    
    return (point[0] - 1, point[1] - 1)


def marcaJogada(jogador, posicao):
    dashboard[posicao[0]][posicao[1]] = jogador

def criarBord():
    dashboard.clear
    for i in range(limit[0]):
        dashboard.append([0] * limit[1])

def draw():
    for i in range(len(dashboard)):
        print('|', end='')
        for j in range(len(dashboard[i])):
            print(bord[dashboard[i][j]], end='|')
        print()

def validaVitoria(jogador, jogada):
    horizontal = [dashboard[jogada[0]][0], dashboard[jogada[0]][1], dashboard[jogada[0]][2]]
    vertical = [dashboard[0][jogada[1]], dashboard[1][jogada[1]], dashboard[2][jogada[1]]]
    diagonal1 = [dashboard[0][0], dashboard[1][1], dashboard[2][2]]
    diagonal2 = [dashboard[0][2], dashboard[1][1], dashboard[2][0]]

    result = False
    countH = 0
    countV = 0
    countD1 = 0
    countD2 = 0

    for i in range(3):
        if horizontal[i] == jogador:
            countH += 1
        if vertical[i] == jogador:
            countV += 1
        if diagonal1[i] == jogador:
            countD1 += 1
        if diagonal2[i] == jogador:
            countD2 += 1
        if countH == 3 or countV == 3 or countD1 == 3 or countD2 == 3:
            result = True

    # if len(set(horizontal)) == 1 and horizontal[0] == jogador:
    #     result = True
    # if horizontal[0] == jogador and horizontal[1] == jogador and horizontal[2] == jogador:
    #     result = True
    # if vertical[0] == jogador and vertical[1] == jogador and vertical[2] == jogador:
    #     result = True
    # if diagonal1[0] == jogador and diagonal1[1] == jogador and diagonal1[2] == jogador:
    #     result = True
    # if diagonal2[0] == jogador and diagonal2[1] == jogador and diagonal2[2] == jogador:
    #     result = True

    return result


def main():
    criarBord()
    jogadas = 9

    jogador = 1
    while jogadas > 0:
        draw()

        jogada = playerTurn(jogador)
        jogadas = jogadas - 1
        marcaJogada(jogador, jogada)
        if validaVitoria(jogador, jogada):
            draw()
            print('Player ', jogador, 'ganhou')
            break
        jogador = jogador ^ 3

    else:
        draw()
        print("Deu velha")

if __name__ == '__main__':
    main()
