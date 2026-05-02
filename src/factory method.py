from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass
    
class Carro(Veiculo):
    def acelerar(self):
        return "Carro acelerando suavemente"

class Moto(Veiculo):
    def acelerar(self):
        return "Moto acelerando rapidamente"

class Caminhao(Veiculo):
    def acelerar(self):
        return "Caminhão acelerando devagar"

class FabricaVeiculos:
    @staticmethod
    def criar_veiculo(tipo): #sem self, ele não instancia obj da classe veiculo
        tipos_validos = {"carro": Carro(), "moto": Moto(), "caminhão": Caminhao()}
        return tipos_validos.get(tipo)


def main():
    tipo = input()
    veiculo = FabricaVeiculos.criar_veiculo(tipo)
    if veiculo:
        print(f"Classe {type (veiculo).__name__} criado")
        print(veiculo.acelerar())
    else:
        print("Tipo de veículo inválido")

if __name__ == "__main__":
    main()