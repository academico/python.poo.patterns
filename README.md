# Padrões de projeto (POO)

Este repositório contém exemplos mínimos em Python de padrões clássicos de projeto. Cada arquivo é um programa autônomo que lê da entrada padrão e ilustra um padrão específico.

---

## `strategy.py` — Strategy (Estratégia)

**Ideia:** encapsular famílias de algoritmos intercambiáveis e delegar a escolha do algoritmo em tempo de execução, sem alterar o código do cliente que usa o comportamento.

**Neste projeto:** `GeradorRelatorio` depende de uma abstração (`EstrategiaRelatorio`, via `Protocol`) e delega `gerar(dados)` à estratégia concreta. As classes `RelatorioPDF`, `RelatorioExcel` e `RelatorioCSV` implementam formatos diferentes; o formato é escolhido a partir da entrada (`PDF:...`, `Excel:...`, `CSV:...`).

**Benefício:** adicionar um novo formato exige uma nova classe de estratégia e um ramo na seleção, sem espalhar `if/elif` de formatação dentro de um único método gigante.

---

## `adapter.py` — Adapter (Adaptador)

**Ideia:** permitir que duas interfaces incompatíveis trabalhem juntas, convertendo chamadas de uma interface na outra.

**Neste projeto:** o código novo espera `ProcessadorPagamento.processar_pagamento(dados_json)` (dicionário JSON). `SistemaLegado` só entende um valor numérico “estilo XML” no método `processar_pagamento`. `AdapterPagamento` implementa a interface esperada, extrai o valor do JSON (`converter_json_para_xml`) e repassa ao legado.

**Benefício:** o restante do sistema fala apenas com `ProcessadorPagamento`; o legado permanece isolado atrás do adaptador.

---

## `decorator.py` — Decorator (Decorador)

**Ideia:** compor comportamentos dinamicamente, empilhando “camadas” ao redor de um objeto base, mantendo a mesma interface pública.

**Neste projeto:** `CafeSimples` é o componente concreto. `ComLeite`, `ComAcucar` e `ComCanela` recebem uma `Bebida` no construtor, delegam `get_descricao` e `get_preco` ao objeto interno e acrescentam texto e custo. A entrada (`cafe simples + leite + ...`) monta a cadeia de decoradores.

**Benefício:** combinações de opcionais (leite, açúcar, canela) sem uma explosão de subclasses para cada combinação.

---

## `builder.py` — Builder (Construtor)

**Ideia:** separar a construção de um objeto complexo da sua representação, permitindo montar passo a passo com uma API fluente.

**Neste projeto:** `CasaBuilder` inicializa uma `Casa` padrão e expõe métodos encadeáveis (`quartos`, `banheiros`, `com_garagem`, `com_jardim`, `com_piscina`) que retornam `self`. O laço interpreta a entrada (por exemplo `2 quartos`, `garagem`) e chama os métodos correspondentes; `construir()` exibe o resultado.

**Benefício:** leitores diferentes da mesma `Casa` podem ser montados sem construtores com dezenas de parâmetros opcionais.

---

## `factory method.py` — Fábrica (criação centralizada)

**Ideia:** centralizar a criação de objetos quando o tipo exato depende de dados em tempo de execução, escondendo dos clientes qual classe concreta instanciar.

**Neste projeto:** `FabricaVeiculos.criar_veiculo(tipo)` mapeia strings (`carro`, `moto`, `caminhão`) para instâncias de `Carro`, `Moto` ou `Caminhao`, todas subclasses abstratas de `Veiculo`. O `main` só pede o tipo e usa o objeto retornado.

**Nota:** na literatura da *Gang of Four*, “Factory Method” costuma ser o método polimórfico em *subclasses* de fábrica; este exemplo é mais próximo de uma **fábrica simples** (um único lugar com `if`/mapa que escolhe a classe). O nome do arquivo reflete o tema “fábrica”; o comportamento é o de criação encapsulada por tipo.

**Como executar:** o nome contém espaço; use aspas no terminal, por exemplo:

`python "factory method.py"`

---

## `singleton.py` — Singleton

**Ideia:** garantir no máximo uma instância de uma classe e um ponto global de acesso a ela.

**Neste projeto:** `ConfiguracaoBanco` usa `__new__` e a variável de classe `_instancia`. Na primeira chamada, cria o objeto e guarda `taxa_de_juros`; chamadas seguintes retornam a mesma instância (mensagens “Instância criada” / “Instância já existente”). `set_taxa_de_juros` e `get_taxa_de_juros` alteram e leem o estado compartilhado.

**Benefício:** configuração única para todo o programa (com os trade-offs conhecidos do Singleton: testes, acoplamento global e concorrência em aplicações mais complexas).

---

## Resumo

| Arquivo | Padrão | Papel principal no exemplo |
|---------|--------|---------------------------|
| `strategy.py` | Strategy | Trocar formato de relatório (PDF/Excel/CSV) |
| `adapter.py` | Adapter | JSON → interface compatível com sistema legado |
| `decorator.py` | Decorator | Compor café com opcionais e preço |
| `builder.py` | Builder | Montar `Casa` passo a passo |
| `factory method.py` | Fábrica simples | Instanciar veículo por tipo de string |
| `singleton.py` | Singleton | Uma única configuração de banco (taxa) |

Todos os scripts foram pensados para execução interativa com `input()`; ao rodar, forneça as entradas esperadas em cada um conforme a lógica do arquivo.
