from utils.baralho import Baralho
from utils.jogadores import Jogador

class Jogo:
    def __init__(self, jogadores:list):
        self.baralho = Baralho()
        #self.dealer = Jogador('dealer')
        self.jogadores = jogadores
        for jogador in jogadores:
            print(f'{jogador.nome.title()} : ')
            valores = self.baralho.tiraragem_inicial()
            jogador.adc_pontos([valores[0], valores[1]])
            
    def tirar_carta_para_jogador(self, jogador:Jogador):
        if jogador not in self.jogadores:
            print('Jogador não está no jogo!')
        else:
            jogador.adc_pontos(self.baralho.tirar())
            self.status = jogador.checar_estado(silencio = True)
            return self.status

def criar_jogadores(quantidade_jogadores:int):
  lista_nomes = []
  for j in range(1, int(quantidade_jogadores)+1):
    print(f'Insira o nome do jogador {j}:')
    nome = input()
    lista_nomes.append(Jogador(nome)) 
  #lista_nomes.append(Jogador('Dealer'))
  print('\n')
  return lista_nomes


if __name__ == '__main__':
    from baralho import Baralho
    from jogadores import Jogador

    jogador_ana = Jogador('Ana')
    jogador_vini = Jogador('Vini')

    novo_jogo = Jogo([jogador_ana,jogador_vini])
    novo_jogo.tirar_carta_para_jogador(jogador_ana)
    novo_jogo.tirar_carta_para_jogador(jogador_ana)
    novo_jogo.tirar_carta_para_jogador(jogador_ana)