#  Space Mission Monitor
### Programação Aplicada ao Monitoramento de Missão Espacial — GS 2026.1 | FIAP

---

##  Equipe

**Missão:** Marte  
**Equipe:** Equipe Pioneira

| Nome | RM |
|------|----|
| Davi Teodoro Novais | 571022 |
| Lourenco Borges da Silva | 569515 |

---

##  Descrição

O **Space Mission Monitor** é um sistema de monitoramento de missão espacial desenvolvido em Python. O programa simula o acompanhamento em tempo real de sensores de uma nave, analisando temperatura, energia e comunicação, emitindo alertas automáticos e organizando um histórico de leituras.

---

##  Como executar

Pré-requisito: Python 3 instalado.

```bash
python space_mission_monitor.py
```

Nenhuma biblioteca externa é necessária além do `os`, que já vem com o Python.

---

##  Funcionalidades

| Opção | Descrição |
|-------|-----------|
| `1` | Inserir dados manualmente (temperatura, energia, comunicação) |
| `2` | Visualizar o status da última leitura registrada |
| `3` | Executar análise completa do histórico (médias e contagem de alertas) |
| `4` | Ver histórico de todas as leituras |
| `5` | Simulação automática com dados de demonstração |
| `0` | Encerrar o sistema |

---

##  Regras de alerta

### Temperatura (°C)
| Condição | Classificação |
|----------|--------------|
| Acima de 80 °C | CRITICO — Alerta de superaquecimento |
| Entre 61 °C e 80 °C | ATENCAO — Temperatura elevada |
| Até 60 °C | NORMAL — Temperatura estavel |

### Energia (%)
| Condição | Classificação |
|----------|--------------|
| Abaixo de 20% | CRITICO — Acionar economia de energia |
| Entre 20% e 39% | ATENCAO — Energia abaixo do recomendado |
| 40% ou mais | NORMAL — Energia estavel |

### Comunicação (%)
| Condição | Classificação |
|----------|--------------|
| Igual a 0% | CRITICO — Falha total de comunicacao |
| Entre 1% e 49% | ATENCAO — Sinal instavel com a base |
| 50% ou mais | NORMAL — Comunicacao estavel |

### Status geral da missão
- Se qualquer sensor estiver **CRITICO** → `MISSAO CRITICA`
- Se qualquer sensor estiver **ATENCAO** → `MISSAO EM ATENCAO`
- Todos os sensores **NORMAL** → `MISSAO ESTAVEL`

---

##  Estrutura do código

```
space_mission_monitor.py
│
├── Funcoes auxiliares
│   ├── limpar()         — limpa o terminal
│   ├── linha()          — imprime separador
│   ├── cabecalho()      — exibe o cabecalho do sistema
│   ├── pausar()         — aguarda o usuario pressionar ENTER
│   └── ler_numero()     — le e valida entrada numerica do usuario
│
├── Funcoes de analise
│   ├── analisar_temperatura()   — classifica a temperatura
│   ├── analisar_energia()       — classifica o nivel de energia
│   ├── analisar_comunicacao()   — classifica a comunicacao
│   └── status_geral()           — define o status geral da missao
│
├── Registro e exibicao
│   ├── registrar_leitura()  — analisa e salva uma leitura no historico
│   └── exibir_leitura()     — exibe os dados de uma leitura no terminal
│
├── Opcoes do menu
│   ├── inserir_dados()      — entrada manual de dados
│   ├── visualizar_status()  — exibe a leitura mais recente
│   ├── executar_analise()   — relatorio completo do historico
│   ├── ver_historico()      — lista todas as leituras
│   └── simular_demo()       — carrega dados de demonstracao automaticamente
│
└── Menu principal
    └── while loop com if/elif para navegacao entre opcoes
```

---

##  Estruturas de dados utilizadas

- **Lista** (`historico`) — armazena todas as leituras registradas
- **Lista dentro de lista** — cada leitura é uma lista com 11 campos
- **`while`** — loop do menu principal e validacao de entrada
- **`for`** — percorre o historico na analise e no relatorio
- **`if / elif / else`** — todas as classificacoes de alerta

---

##  Fluxograma

```
INICIO
  |
  v
Menu Principal
  |
  |-- [1] Inserir dados ---------> le temperatura, energia, comunicacao
  |                                       |
  |-- [2] Visualizar status               v
  |                               registrar_leitura()
  |-- [3] Executar analise               |
  |                               analisar_temperatura()
  |-- [4] Historico               analisar_energia()
  |                               analisar_comunicacao()
  |-- [5] Simulacao demo          status_geral()
  |                                       |
  |-- [0] Encerrar                exibir_leitura()
              |                          |
              v                          v
           FIM                    volta ao menu
```