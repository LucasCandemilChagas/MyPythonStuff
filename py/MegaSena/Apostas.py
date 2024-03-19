class Aposta:
    def __init__(self, nome, cpf, numeros=None):
        self.nome = nome
        self.cpf = cpf
        
        if numeros is None:
            numeros = []
            
        self.numeros = numeros

    def setId(self, id):
        self.id = id
    
    