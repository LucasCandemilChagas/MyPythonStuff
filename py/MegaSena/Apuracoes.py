from Sorteios import Sorteio
verifaca = False
vencedores = []
class Apuracao:
    def __init__(self, numeros_sorteados = None):
        if numeros_sorteados is None:
            numeros_sorteados = []
        self.numeros_sorteados = numeros_sorteados
        
    def verificaVencedor(self):
        sorteio = Sorteio()
        for i in sorteio.getApostaS():
            aposta = i.getApostas
            if aposta == self.numeros_sorteados:
                verifica = True
                vencedores.append(i)
    
    def numeroVencedores(self):
        return len(vencedores)
    
        