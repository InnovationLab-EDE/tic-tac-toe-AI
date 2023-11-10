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
        

def main():    
    criarBord()

    jogador = 1
    while True:   
        draw()
        
        jogada = playerTurn(jogador)
        marcaJogada(jogador, jogada)
        jogador = jogador ^ 3


if __name__ == '__main__':
    main()
