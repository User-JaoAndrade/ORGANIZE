import random
import time
import os
import pandas as pd

# Função para limpar o terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que faz uma mini animação quando printa a string
def cute_animation(word, timer)-> None:
    for letter in word:
        print(letter, end='')
        time.sleep(timer)

# Função que mostra como jogar o jogo (perdi)
def how_to_play()-> None:
    clear_terminal()

    cute_animation(">>> HOW TO PLAY <<<\n\n"
               "You need to arrange a scrambled sentence into the correct order\n"
               "<FOR EXAMPLE: their may friends she help = she may help their friends>\n\n HAVE FUN :D", 0.02)
    cute_animation("\n\npress any button to continue...", 0.02)

    input()

# Função principal do jogo
def gameplay()-> None:
    frase_escolhida: str = random.choice(lista_de_frases) # Escolhendo a frase da lista de frases
    lista_de_palavras: list = frase_escolhida.split() # Dividindo a frase em uma lista de palavras
    random.shuffle(lista_de_palavras) # Embaralhando a frase
    frase_embaralhada: str = ' '.join(lista_de_palavras) # Criando a nova frase

    _try = 1 # variavel que conta as tentativas
    while _try <= 5:
        clear_terminal()
        cute_animation(">>> GAMEPLAY <<<\n\n", 0.02)
        cute_animation(f"Attempts {_try}/5\n"
                       f"Scrambled Sentence -> {frase_embaralhada} <-\n"
                        "Organized sentence -> ", 0.02)
        frase_usuario: str = input()

        if frase_usuario == frase_escolhida:
            cute_animation("\n\n>> CONGRATULATIONS <<\n"
                           "YOU GOT THE CORRECT SENTENCE\n"
                           "Grab a Cookie\n\n"
                           "press any button to continue...", 0.02)
            input()
            
            break
        else:
            cute_animation("\nWRONG", 0.02)
            cute_animation("...", 1)
            _try+=1
    else:
        cute_animation("\n\nYour attempts are over :( returning to the menu", 0.02)
        cute_animation("....", 1)


# INICIO DO PROGRAMA
if __name__ == "__main__":
    option: str = None
    lista_de_frases = pd.read_csv("frases.txt", header=None) # lendo o arquivo txt
    lista_de_frases = lista_de_frases[0].tolist() # Convertendo a coluna do txt para uma lista

    while option != 3:
        clear_terminal()

        cute_animation(">>> Game of forming sentences using Modal Verbs <<<", 0.02)
        print("\n")
        cute_animation("[1]Start Game\n"
                    "[2]How to play\n"
                    "[3]Quit Game\n\n-> ", 0.02)
        option = input()

        match option:
            case '1':
                gameplay()
            case '2':
                how_to_play()
            case '3':
                exit()