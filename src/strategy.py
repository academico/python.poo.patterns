from typing import Protocol

class EstrategiaRelatorio(Protocol):
    def gerar(): ...

#usa estratégias
class GeradorRelatorio:
    def __init__(self, estrategia):
        self.estrategia = estrategia
    def gerar(self, dados):
        self.estrategia.gerar(dados)

#estratégias  
class RelatorioPDF(EstrategiaRelatorio):
    def gerar(self, dados):
        print(f"Relatório PDF gerado com: "+', '.join(dados))

class RelatorioExcel(EstrategiaRelatorio):
    def gerar(self, dados):
        print(f"Relatório Excel gerado com: "+', '.join(dados))

class RelatorioCSV(EstrategiaRelatorio):
    def gerar(self, dados):
        print(f"Relatório CSV gerado com: "+', '.join(dados))

    
#entrada
formato, relatorios = input().split(":")
dados = relatorios.split(', ')
if formato == "PDF":
    gerador = GeradorRelatorio(RelatorioPDF())
elif formato =="Excel":
    gerador = GeradorRelatorio(RelatorioExcel())
elif formato == "CSV":
    gerador = GeradorRelatorio(RelatorioCSV())
else:
    print("Formato não suportado")
    exit(0)
gerador.gerar(dados)