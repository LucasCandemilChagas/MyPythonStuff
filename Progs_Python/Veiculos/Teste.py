from Carros import Carro
from Motos import Moto


def mostrar_informacoes_veiculo(veiculo):
    veiculo.mostrar_detalhes()
    
carro = Carro("Ford", "Fusion", 4)
moto = Moto("Honda", "CBR", 650)

mostrar_informacoes_veiculo(carro)
mostrar_informacoes_veiculo(moto)