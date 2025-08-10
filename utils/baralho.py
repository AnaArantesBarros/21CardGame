import random


class Baralho:
    def __init__(self):
        self.resetar()  # cria o baralho inicial

    def embaralhar(self):
        random.shuffle(self.cartas)
    
    def tirar(self):
        return self.cartas.pop()
    
    def resetar(self):
        self.cartas = 4 * ['A', 'K', 'Q', 'J', '10', '09', '08', '07', '06', '05', '04', '03', '02']