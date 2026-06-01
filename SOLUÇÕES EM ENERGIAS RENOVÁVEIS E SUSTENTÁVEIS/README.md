# Energy Mission Monitor
### Monitoramento de Sistemas Energéticos — GS 2026.1 | FIAP

---

## Equipe

**Missão:** Marte  
**Equipe:** Equipe Pioneira

| Nome | RM |
|------|----|
| Davi Teodoro Novais | 571022 |
| Lourenco Borges da Silva | 569515 |

---

## Descrição

O **Energy Mission Monitor** é um sistema de monitoramento de sistemas energéticos
de uma missão espacial experimental desenvolvido em Python. O programa simula o
acompanhamento de três fontes de energia renováveis da nave — Painel Solar, Bateria
Principal e Reator de Fusão — além do controle térmico e da comunicação, analisando
cada ciclo de operação, calculando potência estimada, eficiência energética e emitindo
alertas e recomendações automáticas.

---

## Como executar

Pré-requisito: Python 3 instalado.

```bash
python energy_mission_monitor.py
```

Nenhuma biblioteca externa é necessária além do `os`, que já vem com o Python.

---

## Funcionalidades

| Opção | Descrição |
|-------|-----------|
| `1` | Inserir dados manualmente para todos os módulos |
| `2` | Visualizar o status da última leitura registrada |
| `3` | Análise energética completa (médias, eficiência, diagnóstico) |
| `4` | Histórico de todas as leituras |
| `5` | Monitoramento por ciclos simulados (demo automática) |
| `0` | Encerrar o sistema |

---

## Módulos Monitorados

| Módulo | O que representa |
|--------|-----------------|
| **Painel Solar** | Geração de energia renovável via radiação solar |
| **Bateria Principal** | Armazenamento e reserva de energia da nave |
| **Reator de Fusão** | Fonte de energia primária de alta potência |
| **Sistema Térmico** | Temperatura interna dos sistemas energéticos |
| **Comunicação** | Qualidade do sinal com a base terrestre |

---

## Regras de Alerta

### Energia — Painel Solar, Bateria e Reator (%)
| Condição | Classificação |
|----------|--------------|
| Abaixo de 20% | CRITICO — Risco de falha total |
| Entre 20% e 49% | ATENCAO — Acionar reserva |
| 50% ou mais | NORMAL — Nível adequado |

### Sistema Térmico (°C)
| Condição | Classificação |
|----------|--------------|
| Acima de 80 °C | CRITICO — Superaquecimento |
| Entre 61 °C e 80 °C | ATENCAO — Temperatura elevada |
| Até 60 °C | NORMAL — Temperatura estável |

### Comunicação (%)
| Condição | Classificação |
|----------|--------------|
| Igual a 0% | CRITICO — Falha total |
| Entre 1% e 49% | ATENCAO — Sinal instável |
| 50% ou mais | NORMAL — Comunicação estável |

### Status geral do ciclo
- Qualquer módulo **CRITICO** → `CICLO CRITICO` → acionar protocolo de emergência
- Qualquer módulo **ATENCAO** → `CICLO EM ATENCAO` → reduzir consumo não essencial
- Todos **NORMAL** → `CICLO ESTAVEL` → manter operação normal

---

## Conceitos de Energia Aplicados

**Potência estimada por módulo:**
```
Potencia (W) = nivel_energia (%) * fator_do_ciclo
```
O fator do ciclo diminui conforme a missão avança, simulando o desgaste
natural dos sistemas ao longo da operação.

**Eficiência energética geral:**
```
Eficiencia (%) = media_dos_tres_modulos_de_energia / 100 * 100
```
Indica o quanto a nave está aproveitando sua capacidade energética total.

**Diagnóstico automático:**
| Eficiência | Diagnóstico |
|------------|-------------|
| 70% ou mais | Missão operando com boa eficiência energética |
| Entre 40% e 69% | Eficiência moderada — revisar módulos em atenção |
| Abaixo de 40% | Eficiência crítica — acionar protocolos de emergência |

---

## Estrutura do Código

```
energy_mission_monitor.py
│
├── Dados simulados
│   └── modulos{}  — dicionario com 6 leituras por modulo
│
├── Funcoes auxiliares
│   ├── limpar()       — limpa o terminal
│   ├── linha()        — imprime separador
│   ├── cabecalho()    — exibe o cabecalho
│   ├── pausar()       — aguarda ENTER
│   └── ler_numero()   — valida entrada do usuario
│
├── Funcoes de analise energetica
│   ├── analisar_energia()        — classifica nivel de energia
│   ├── analisar_temperatura()    — classifica temperatura
│   ├── analisar_comunicacao()    — classifica comunicacao
│   ├── calcular_potencia()       — estima potencia gerada no ciclo
│   ├── calcular_eficiencia()     — calcula eficiencia percentual
│   ├── status_geral_ciclo()      — define status do ciclo
│   └── gerar_recomendacao()      — sugere acao automatica
│
├── Registro e exibicao
│   ├── registrar_leitura_manual()  — analisa e salva no historico
│   └── exibir_leitura()            — exibe leitura formatada
│
├── Opcoes do menu
│   ├── inserir_dados()       — entrada manual
│   ├── visualizar_status()   — ultimo status
│   ├── executar_analise()    — relatorio completo
│   ├── ver_historico()       — todas as leituras
│   └── monitorar_ciclos()    — demo com 6 ciclos simulados
│
└── Menu principal
    └── while com if/elif para navegacao
```

---

## Fluxograma

```
INICIO
  |
  v
Menu Principal
  |
  |-- [1] Inserir dados -----> le 5 valores do usuario
  |                                  |
  |-- [2] Status atual               v
  |                         registrar_leitura_manual()
  |-- [3] Analise                    |
  |                         analisar_energia()
  |-- [4] Historico         analisar_temperatura()
  |                         analisar_comunicacao()
  |-- [5] Ciclos demo       calcular_potencia()
  |        |                status_geral_ciclo()
  |        v                gerar_recomendacao()
  |   le modulos{}                   |
  |   6 ciclos automaticos    exibir_leitura()
  |                                  |
  |-- [0] Encerrar           volta ao menu
              |
              v
           FIM
```
