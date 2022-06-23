# dependências
import time
import os
from time import sleep
from turtle import clear

def main():
    # ligando o sistema
    print('Ligando o Sistema . . .')

    time.sleep(0.8)

    os.system("cls")

    # Coletando o Nome

    print('Qual é o seu nome?') # pergunta o nome
    nome = input() # declarando variável nome

    time.sleep(0.8)

    os.system("cls")

    print('Olá,' + nome)

    time.sleep(0.8)

    os.system("cls")

    print('Quantas letras tem o seu nome:')

    time.sleep(0.8)

    print (len(nome)) # printando a informação enviada pelo usuário

    time.sleep(0.8)

    os.system("cls")

    # Coletando a Idade

    print('Qual é a sua idade?') # pergunta a idade
    idade = input() # declarando variável idade

    time.sleep(0.8)

    os.system("cls")

    print(f"Você vai ter {str(int(idade) + 1)} em um ano.") # qual vai ser sua idade em um ano

    time.sleep(0.8)

    os.system("cls")

    # mostrando os dados completos do usuário

    print("\n")
    print('==========================================')
    print(f"Nome: {str(nome)}")
    print(f"Quantidade de letras no nome: {str(len(nome))}")
    print(f"Idade: {str(int(idade))}")
    print(f"Idade em um ano: {str(int(idade) + 1)}")
    print('==========================================')
    print("\n")

# fim do código..

    closeOrContinue = input("Deseja fechar? S ou N: ")
    if closeOrContinue == "N":
        main()
    elif closeOrContinue == "S":
        exit()

main()
