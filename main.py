import tkinter as tk
from tkinter import messagebox

limit = (3, 3)
bord = [' ', 'X', 'O']
dashboard = []

def criarBord():
    dashboard.clear()
    for i in range(limit[0]):
        dashboard.append([0] * limit[1])

def isTurnValid(point):
    if len(point) != 2:
        return False

    for i in range(2):
        if point[i] <= 0 or point[i] > limit[i]:
            return False

    if dashboard[point[0] - 1][point[1] - 1] > 0:
        return False

    return True

def marcaJogada(jogador, posicao):
    dashboard[posicao[0]][posicao[1]] = jogador

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

def draw():
    # lógica para desenhar o tabuleiro (mantida como está)
    for i in range(len(dashboard)):
        print('|', end='')
    for j in range(len(dashboard[i])):
        print(bord[dashboard[i][j]], end='|')
    print()

def on_click(row, col):

    global jogador, jogadas

    if isTurnValid([row + 1, col + 1]):
        marcaJogada(jogador, [row, col])
        buttons[row * 3 + col].config(text=bord[jogador])
        if validaVitoria(jogador, [row, col]):
            messagebox.showinfo("Fim de jogo", f"Player {jogador} ganhou!")
            reiniciar_jogo()
            return
        jogador = jogador ^ 3
        jogadas -= 1
        if jogadas == 0:
            messagebox.showinfo("Fim de jogo", "Deu velha!")
            reiniciar_jogo()

def reiniciar_jogo():
    global jogador, jogadas
    criarBord()
    jogador = 1
    jogadas = 9
    for button in buttons:
        button.config(text=' ', state=tk.NORMAL)

def create_board():
    global buttons
    buttons = []
    for i in range(3):
        for j in range(3):
            button = tk.Button(root, text=' ', font=('Arial', 20), width=5, height=2,
                                command=lambda row=i, col=j: on_click(row, col))
            button.grid(row=i, column=j)
            buttons.append(button)

root = tk.Tk()
root.title("Jogo da Velha")

jogador = 1
jogadas = 9

create_board()
criarBord()

root.mainloop()
