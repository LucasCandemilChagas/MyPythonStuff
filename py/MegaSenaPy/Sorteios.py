from Apostas import Aposta
class Sorteio:
    def __init__(self, apostas=None, numerosSorteados =None):
        if apostas is None:
            apostas = [Aposta]
        if numerosSorteados is None:
            numerosSorteados = []
        
        self. apostas = apostas
        self.numerosSorteados = numerosSorteados
        
    
    