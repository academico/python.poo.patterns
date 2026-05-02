class Casa:
    def __init__(self, quartos, banheiros, garagem, jardim, piscina):
        self.quartos = quartos
        self.banheiros = banheiros
        self.garagem = garagem
        self.jardim = jardim
        self.piscina = piscina

class CasaBuilder:
    def __init__(self):
        self.casa = Casa(0, 0, False, False, False)

    def quartos(self, num):
        self.casa.quartos = num
        return self

    def banheiros(self, num):
        self.casa.banheiros = num
        return self

    def com_garagem(self):
        self.casa.garagem = True
        return self

    def com_jardim(self):
        self.casa.jardim = True
        return self

    def com_piscina(self):
        self.casa.piscina = True
        return self

    def construir(self):
        print(f"Casa construída: {self.casa.quartos} quartos, "
              f"{self.casa.banheiros} banheiros, "
              f"garagem: {self.casa.garagem}, "
              f"jardim: {self.casa.jardim}, "
              f"piscina: {self.casa.piscina}")
        #return self.casa


comodos = input().split(", ")
casa = CasaBuilder()

for i in comodos:
    i = i.strip().lower()
    if "quarto" in i:
        num = int(i.split()[0])
        casa.quartos(num)
    elif "banheiro" in i:
        num = int(i.split()[0])
        casa.banheiros(num)
    elif "garagem" in i:
        casa.com_garagem()
    elif "jardim" in i:
        casa.com_jardim()
    elif "piscina" in i:
        casa.com_piscina()

casa.construir()
