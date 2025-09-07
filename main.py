from utils.jogo import Jogo
from utils.jogadores import Jogador

def criar_jogadores(quantidade_jogadores:int):
  lista_nomes = []
  for j in range(1, int(quantidade_jogadores)+1):
    print(f'Insira o nome do jogador {j}:')
    nome = input()
    lista_nomes.append(Jogador(nome)) 

  return lista_nomes

def turno():
    ''
def start_game():
    print('Bem Vindo! Vamos comecar nosso jogo! ')
    print('Quantas pessoas väo jogar?')
    quantidade_jogadores = input()

    jogadores = criar_jogadores(quantidade_jogadores)

    novo_jogo = Jogo(jogadores)
    print('\n O que preferem fazer agora? ("comprar" ou "parar")')
    status_jogo = ''
    while status_jogo != 'Venceu' or status_jogo != 'Perdeu':
        for jogador in jogadores:
           acao = input(f'Jogador {jogador.nome}: \n')
           if acao.lower() == 'comprar':
              status_jogo = novo_jogo.tirar_carta_para_jogador(jogador)
           if acao.lower() == 'stop':
              status_jogo = novo_jogo.tirar_carta_para_jogador(jogador)

    #novo_jogo.tirar_carta_para_jogador()

    



start_game()
    