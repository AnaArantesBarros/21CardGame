class Jogador:
    def __init__(self, nome:str):
        self.nome = nome
        self.pontuacao = 0

    def checar_estado(self):
        if self.pontuacao == 21:
            print(f'{self.nome} venceu!')
            self.pontuacao = 0
            return 'Venceu'
        elif self.pontuacao > 21:
            print(f'{self.nome} perdeu!')
            self.pontuacao = 0
            return 'Perdeu'
        else:
            return self.pontuacao

    def adc_pontos(self, cartas:tuple):
        for carta in cartas:
            pontos = self.checar_estado()
            if carta in ['K', 'Q', 'J']:
                valor = 10
            elif carta == 'A' and pontos + 11 <= 21:
                valor = 11
            elif carta == 'A' and pontos + 11 > 21:
                valor = 1
            else:
                valor = int(carta)

            self.pontuacao += valor
            self.checar_estado()



if __name__ == '__main__':
    jogador1 = Jogador('Ana')

    jogador1.adc_pontos(('04','10'))

