from utils.jogo import Jogo, criar_jogadores


def start_game():
    print('Bem Vindo! Vamos começar nosso jogo! ')
    quantidade_jogadores = int(input('Quantas pessoas vão jogar? '))

    jogadores = criar_jogadores(quantidade_jogadores)
    novo_jogo = Jogo(jogadores)

    print('\nO que preferem fazer agora? ("comprar" ou "parar")')

    while any(jogador.status == "Jogando" for jogador in jogadores):
        for jogador in jogadores:
            if jogador.status != "Jogando":
                continue

            acao = input(f'Jogador {jogador.nome}, sua vez: ')

            if acao.lower() == 'comprar':
                novo_jogo.tirar_carta_para_jogador(jogador)
                jogador.checar_estado()

            elif acao.lower() == 'parar':
                jogador.status = 'Fora'

    print('\nFim de jogo! Aqui está o resultado:')
    for jogador in jogadores:
        print(f'{jogador.nome.title()}: {jogador.checar_estado(silencio = True)}')


start_game()
