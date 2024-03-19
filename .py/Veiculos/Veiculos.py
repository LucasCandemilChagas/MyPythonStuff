class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_detalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")
