class Jogador:
    def __init__(self, nome: str):
        self.nome = nome
        self.pontuacao = 0
        self.status = 'Jogando'

    def checar_estado(self, silencio=False):
        if self.pontuacao == 21:
            if not silencio:
                print(f'{self.nome} venceu!')
            self.status = 'Venceu'
            return 'Venceu'
        elif self.pontuacao > 21:
            if not silencio:
                print(f'{self.nome} perdeu!')
            self.status = 'Perdeu'
            return 'Perdeu'
        else:
            return self.pontuacao

    def adc_pontos(self, cartas: tuple):
        for carta in cartas:
            pontos = self.pontuacao  # usa a pontuação atual
            if carta in ['K', 'Q', 'J']:
                valor = 10
            elif carta == 'A':
                valor = 11 if pontos + 11 <= 21 else 1
            else:
                valor = int(carta)

            self.pontuacao += valor

        return self.pontuacao  # retorna sempre int


if __name__ == '__main__':
    jogador1 = Jogador('Ana')

    jogador1.adc_pontos(('04', '10'))
    print(f'Pontuação: {jogador1.pontuacao}, Estado: {jogador1.checar_estado()}')

    jogador1.adc_pontos(('A',))
    print(f'Pontuação: {jogador1.pontuacao}, Estado: {jogador1.checar_estado()}')
