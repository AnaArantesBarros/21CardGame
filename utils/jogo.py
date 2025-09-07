from utils.baralho import Baralho
from utils.jogadores import Jogador

class Jogo:
    def __init__(self, jogadores:list):
        self.baralho = Baralho()
        self.dealer = Jogador('dealer')
        self.jogadores = jogadores
        for jogador in jogadores:
            valores = self.baralho.tiraragem_inicial()
            jogador.adc_pontos([valores[0], valores[1]])
            
    def tirar_carta_para_jogador(self, jogador:Jogador):
        if jogador not in self.jogadores:
            print('Jogador não está no jogo!')
        else:
            jogador.adc_pontos(self.baralho.tirar())
            self.status = jogador.checar_estado()
            return self.status

if __name__ == '__main__':
    from baralho import Baralho
    from jogadores import Jogador

    jogador_ana = Jogador('Ana')
    jogador_vini = Jogador('Vini')

    novo_jogo = Jogo([jogador_ana,jogador_vini])
    novo_jogo.tirar_carta_para_jogador(jogador_ana)
    novo_jogo.tirar_carta_para_jogador(jogador_ana)
    novo_jogo.tirar_carta_para_jogador(jogador_ana)