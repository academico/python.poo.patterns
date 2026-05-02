class ConfiguracaoBanco:
    _instancia = None
    def __new__(cls, taxa_de_juros):
        if cls._instancia is None: #none quer dizer que a instancia ainda não foi criada, criando:
            cls._instancia = super().__new__(cls)
            cls._instancia.taxa_de_juros = taxa_de_juros
            print("Instância criada")
        else:
            print("Instância já existente")
        return cls._instancia
    
    def get_taxa_de_juros(self):
        return self.taxa_de_juros
        
    def set_taxa_de_juros(self, taxa):
        self.taxa_de_juros = taxa #atualizada
        
def main():
    taxa_de_juros = float(input())
    acao = input()
    instancia = ConfiguracaoBanco(taxa_de_juros)
    if acao == "set_new_taxa":
        taxa = float(input())
        instancia.set_taxa_de_juros(taxa)
        print(f"Taxa definida: {instancia.get_taxa_de_juros():.1f}")
    elif acao == "get_taxa":
        print(f"Taxa atual: {instancia.get_taxa_de_juros():.1f}")
    elif acao == "nova_instancia":
        instancia2 = ConfiguracaoBanco(taxa_de_juros)

if __name__ == "__main__":
    main()