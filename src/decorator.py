from typing import Protocol

class Bebida(Protocol): #interface
    def get_descricao(): ...
    def get_preco(): ...
        
class CafeSimples(Bebida):
    def get_descricao(self):
        return "Café Simples "
    def get_preco(self):
        return 3.00
        
class ComLeite(Bebida):
    def __init__(self, bebida):
        self.bebida = bebida
        self.preco = 0.50
    def get_descricao(self):
        return self.bebida.get_descricao()+ " com Leite"
    def get_preco(self):
        return self.bebida.get_preco()+self.preco

class ComAcucar(Bebida):
    def __init__(self, bebida):
        self.bebida = bebida
        self.preco = 0.20
    def get_descricao(self):
        return self.bebida.get_descricao()+ " com Açúcar"
    def get_preco(self):
        return self.bebida.get_preco()+self.preco

class ComCanela(Bebida):
    def __init__(self, bebida):
        self.bebida = bebida
        self.preco = 0.30
    def get_descricao(self):
        return self.bebida.get_descricao()+ " com Canela"
    def get_preco(self):
        return self.bebida.get_preco()+self.preco

linha = input().split(" + ")
for i in linha:
    if i == "cafe simples":
        bebida = CafeSimples()
    elif i == "leite":
        bebida = ComLeite(bebida)
    elif i == "açúcar":
        bebida = ComAcucar(bebida)
    elif i == "canela":
        bebida = ComCanela(bebida)
print(f"{bebida.get_descricao()} - R$ {bebida.get_preco():.2f}")