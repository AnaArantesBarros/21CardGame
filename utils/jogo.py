from baralho import Baralho
from jogadores import Jogador

class Jogo:
    def __init__(self, jogadores:list):
        self.baralho = Baralho()
        self.dealer = Jogador('dealer')
        self.jogadores = jogadores
        for jogador in jogadores:
            jogador.adc_pontos(self.baralho.tiraragem_inicial())
            
    def tirar_carta_para_jogador(self, jogador:Jogador):
        if jogador not in self.jogadores:
            print('Jogador não está no jogo!')
        else:
            jogador.adc_pontos(self.baralho.tirar())


if __name__ == '__main__':
    from baralho import Baralho

    jogador_ana = Jogador('Ana')
    jogador_vini = Jogador('Vini')

    novo_jogo = Jogo([jogador_ana,jogador_vini])
    novo_jogo.tirar_carta_para_jogador(jogador_ana)
    novo_jogo.tirar_carta_para_jogador(jogador_ana)
    novo_jogo.tirar_carta_para_jogador(jogador_ana)