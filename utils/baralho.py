import random

class Baralho:
    def __init__(self):
        self.resetar()  # cria o baralho inicial
        self.embaralhar()
        
    def embaralhar(self):
        random.shuffle(self.cartas)
    
    def tirar(self):
        carta = self.cartas.pop()
        print('Carta:', carta)
        return carta # retorna qual carta foi tirada
    
    def tiraragem_inicial(self):
        cartas = (self.cartas.pop(), self.cartas.pop())
        print('Cartas inicias:', cartas)
        return cartas# retorna qual carta foi tirada
    
    def resetar(self):
        self.cartas = 4 * ['A', 'K', 'Q', 'J', '10', '09', '08', '07', '06', '05', '04', '03', '02']

if __name__ == '__main__':
    from jogadores import Jogador
    baralho = Baralho()
    baralho.embaralhar()

    jogador1 = Jogador('ANA')
    jogador1.adc_pontos(baralho.tiraragem_inicial())
    #sprint(baralho.tiraragem_inicial())