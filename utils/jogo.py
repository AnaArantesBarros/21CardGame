from baralho import Baralho
class Jogo:
    def __init__(self, jogadores:list):
        self.baralho = Baralho()
        for jogador in jogadores:
            jogador.adc_pontos(self.baralho.tiraragem_inicial())

if __name__ == '__main__':
    from baralho import Baralho
    from jogadores import Jogador

    jogador_ana = Jogador('Ana')
    jogador_vini = Jogador('Vini')

    novo_jogo = Jogo([jogador_ana,jogador_vini])
    