from typing import Protocol

class ProcessadorPagamento(Protocol):
    def processar_pagamento(self, dados_json): ...

class SistemaLegado:
    def processar_pagamento(self, dados_xml):
        print(f"Pagamento processado via sistema legado: R$ {dados_xml:.2f}")
    
class AdapterPagamento(ProcessadorPagamento):
    def __init__(self):
        self.sistema_legado = SistemaLegado()
    def processar_pagamento(self, dados_json):
        dados_xml = self.converter_json_para_xml(dados_json)
        self.sistema_legado.processar_pagamento(dados_xml)
    
    def converter_json_para_xml(self, dados_json):
        return dados_json["valor"]

import json
dado_json = json.loads(input())
adapter = AdapterPagamento()
adapter.processar_pagamento(dado_json)