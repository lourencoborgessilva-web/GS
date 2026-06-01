#  Mission Control AI

Sistema inteligente de monitoramento de missão espacial desenvolvido em Python.

##  Descrição

O **Mission Control AI** simula o acompanhamento de uma missão espacial experimental por meio de ciclos de monitoramento. A cada ciclo, o sistema analisa 5 variáveis operacionais, calcula o nível de risco, emite alertas automáticos e gera um relatório final completo.

##  Equipe

- **Missão:** Marte
- **Equipe:** Equipe Pioneira 

##  Funcionalidades

- Análise de 6 ciclos de monitoramento
- Classificação automática de cada variável em **NORMAL**, **ATENÇÃO** ou **CRÍTICO**
- Cálculo de pontuação de risco por ciclo
- Classificação do ciclo: **MISSÃO ESTÁVEL**, **MISSÃO EM ATENÇÃO** ou **MISSÃO CRÍTICA**
- Geração de recomendações automáticas
- Análise da tendência geral da missão (melhora / piora / estável)
- Identificação da área mais afetada ao longo da missão
- Relatório final consolidado no terminal

##  Estrutura do repositório

```
mission-control-ai/
│
├── README.md
└── mission_control.py
```

## ▶ Como executar

Pré-requisito: Python 3.x instalado.

```bash
python mission_control.py
```

Não são necessárias bibliotecas externas.

##  Estrutura dos dados

A matriz `dados_missao` contém 6 ciclos, cada um com 5 valores:

| Posição | Variável     | Unidade |
|---------|-------------|---------|
| 0       | Temperatura | °C      |
| 1       | Comunicação | %       |
| 2       | Bateria     | %       |
| 3       | Oxigênio    | %       |
| 4       | Estabilidade| %       |

##  Regras de alerta

### Temperatura (°C)
| Condição          | Classificação |
|-------------------|--------------|
| < 18              | ATENÇÃO      |
| 18 a 30           | NORMAL       |
| > 30 até 35       | ATENÇÃO      |
| > 35              | CRÍTICO      |

### Comunicação (%)
| Condição   | Classificação |
|------------|--------------|
| < 30%      | CRÍTICO      |
| 30% a 59%  | ATENÇÃO      |
| ≥ 60%      | NORMAL       |

### Bateria (%)
| Condição   | Classificação |
|------------|--------------|
| < 20%      | CRÍTICO      |
| 20% a 49%  | ATENÇÃO      |
| ≥ 50%      | NORMAL       |

### Oxigênio (%)
| Condição   | Classificação |
|------------|--------------|
| < 80%      | CRÍTICO      |
| 80% a 89%  | ATENÇÃO      |
| ≥ 90%      | NORMAL       |

### Estabilidade (%)
| Condição   | Classificação |
|------------|--------------|
| < 40%      | CRÍTICO      |
| 40% a 69%  | ATENÇÃO      |
| ≥ 70%      | NORMAL       |

##  Pontuação de risco

| Classificação | Pontos |
|--------------|--------|
| NORMAL       | 0      |
| ATENÇÃO      | 1      |
| CRÍTICO      | 2      |

Pontuação máxima por ciclo: **10 pontos** (5 variáveis × 2 pontos cada).

##  Classificação do ciclo

| Pontuação  | Status               |
|------------|----------------------|
| 0 a 2      | MISSÃO ESTÁVEL       |
| 3 a 5      | MISSÃO EM ATENÇÃO    |
| 6 a 10     | MISSÃO CRÍTICA       |

##  Funções implementadas

| Função                          | Descrição                                      |
|---------------------------------|------------------------------------------------|
| `analisar_temperatura()`        | Classifica a temperatura do módulo             |
| `analisar_comunicacao()`        | Classifica a qualidade do sinal                |
| `analisar_bateria()`            | Classifica o nível de bateria                  |
| `analisar_oxigenio()`           | Classifica o nível de oxigênio                 |
| `analisar_estabilidade()`       | Classifica a estabilidade dos sistemas         |
| `classificar_ciclo()`           | Determina o status geral do ciclo              |
| `gerar_recomendacao()`          | Produz recomendação automática para o ciclo    |
| `analisar_tendencia()`          | Compara risco do 1º e último ciclo             |
| `identificar_area_mais_afetada()` | Aponta a área com maior risco acumulado      |
| `gerar_relatorio_final()`       | Exibe o relatório consolidado da missão        |
| `main()`                        | Função principal que orquestra todo o sistema  |