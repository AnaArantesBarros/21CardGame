import random


class Baralho:
    def __init__(self):
        self.resetar()  # cria o baralho inicial
        self.embaralhar()
        
    def embaralhar(self):
        random.shuffle(self.cartas)
    
    def tirar(self):
        return self.cartas.pop() # retorna qual carta foi tirada
    
    def tiraragem_inicial(self):
        return self.cartas.pop(), self.cartas.pop() # retorna qual carta foi tirada
    
    def resetar(self):
        self.cartas = 4 * ['A', 'K', 'Q', 'J', '10', '09', '08', '07', '06', '05', '04', '03', '02']

if __name__ == '__main__':
    baralho = Baralho()
    baralho.embaralhar()
    print(baralho.tiraragem_inicial())