# Global Solution 2026.1 — FIAP

## Identificacao

**Missao:** Marte  
**Equipe:** Equipe Pioneira  

| Nome |
|------|
| Lourenco Borges da Silva | 

---

## Descricao Geral

Este repositorio reune os quatro projetos desenvolvidos pela Equipe Pioneira como parte da Global Solution 2026.1 da FIAP, tema central: **Solucoes em Energias Renovaveis e Sustentaveis aplicadas a Exploracao Espacial**.

Cada projeto foi desenvolvido para uma disciplina diferente, mas todos compartilham o mesmo contexto: o monitoramento computacional de uma missao espacial experimental chamada **Marte**. Os projetos se complementam, formando uma solucao integrada que vai desde a analise de dados operacionais da nave ate o tratamento estatistico de dados reais de energia solar mundial.

---

## Estrutura do Repositorio

```
global-solution-2026/
|
|-- mission_control.py              Projeto 1 - Pensamento Computacional
|-- space_mission_monitor.py        Projeto 2 - Programacao Aplicada
|-- energy_mission_monitor.py       Projeto 3 - Ciencia da Computacao
|-- analise_estatistica.py          Projeto 4 - Modelagem Linear
|-- energia_solar_mundial.csv       Base de dados real (Projeto 4)
|-- relatorio_estatistico.pdf       Relatorio estatistico (Projeto 4)
|-- README.md                       Este arquivo
```

---

## Projeto 1 — Mission Control AI

**Disciplina:** Pensamento Computacional e Automacao com Python  
**Arquivo:** `mission_control.py`

### Contexto

O Mission Control AI simula um sistema de monitoramento de missao espacial baseado em ciclos de operacao. Cada ciclo representa um momento distinto da missao, desde o inicio estavel ate situacoes de risco critico e tentativa de recuperacao.

### Estrutura de Dados

O sistema e construido em torno de uma matriz principal chamada `dados_missao`, uma lista de listas em que cada linha representa um ciclo e cada coluna representa uma variavel monitorada, nesta ordem: temperatura (graus Celsius), comunicacao (percentual), bateria (percentual), oxigenio (percentual) e estabilidade (percentual). A matriz possui seis ciclos de monitoramento.

### Regras de Alerta

Cada variavel e classificada de forma independente como NORMAL, ATENCAO ou CRITICO, com base em limiares definidos. A temperatura, por exemplo, e considerada critica acima de 35 graus Celsius. Cada classificacao gera uma pontuacao: NORMAL vale zero pontos, ATENCAO vale um ponto e CRITICO vale dois pontos. Como cada ciclo possui cinco variaveis, a pontuacao maxima por ciclo e dez pontos.

### Classificacao dos Ciclos

Com base na pontuacao total do ciclo, o sistema o classifica em tres categorias: MISSAO ESTAVEL (zero a dois pontos), MISSAO EM ATENCAO (tres a cinco pontos) e MISSAO CRITICA (seis a dez pontos).

### Funcionalidades

O programa percorre todos os ciclos da matriz com uma estrutura de repeticao, analisa cada variavel com funcoes dedicadas, calcula a pontuacao de risco, classifica o ciclo, gera uma recomendacao automatica e, ao final, exibe um relatorio completo com medias de cada variavel, ciclo mais critico, risco medio, tendencia da missao (comparando o primeiro e o ultimo ciclo) e a area mais afetada ao longo de todos os ciclos.

### Funcoes Implementadas

O projeto possui dez funcoes: `analisar_temperatura`, `analisar_comunicacao`, `analisar_bateria`, `analisar_oxigenio`, `analisar_estabilidade`, `classificar_ciclo`, `gerar_recomendacao`, `analisar_tendencia`, `identificar_area_mais_afetada` e `gerar_relatorio_final`.

### Como Executar

```bash
python mission_control.py
```

---

## Projeto 2 — Space Mission Monitor

**Disciplina:** Programacao Aplicada ao Monitoramento de Missao Espacial  
**Arquivo:** `space_mission_monitor.py`

### Contexto

O Space Mission Monitor e um sistema interativo com menu que permite ao usuario inserir dados manualmente, visualizar o status atual da missao, executar analises sobre o historico de leituras e simular dados automaticamente. O foco desta disciplina era o uso correto de estruturas de dados, estruturas condicionais, lacos de repeticao e funcoes.

### Estrutura de Dados

O historico de leituras e armazenado em uma lista chamada `historico`. Cada elemento dessa lista e, por sua vez, uma lista com onze posicoes, contendo o numero da leitura, os valores de temperatura, energia e comunicacao, as classificacoes e mensagens de cada variavel e o status geral da leitura.

### Variaveis Monitoradas

O sistema monitora tres variaveis: temperatura da nave (em graus Celsius), nivel de energia (em percentual) e qualidade da comunicacao (em percentual). Cada variavel possui tres faixas de classificacao — NORMAL, ATENCAO e CRITICO — com limiares definidos de acordo com o enunciado da disciplina.

### Menu Interativo

O menu principal e controlado por um laco `while` que permanece ativo ate que o usuario escolha a opcao de encerramento. As cinco opcoes disponiveis sao:

- Opcao 1: inserir dados manualmente, com validacao de intervalo e tratamento de erro para entradas nao numericas;
- Opcao 2: visualizar o status da leitura mais recente registrada no historico;
- Opcao 3: executar uma analise completa do historico, calculando media de cada variavel e contando leituras por categoria de status;
- Opcao 4: exibir todas as leituras registradas em formato resumido;
- Opcao 5: carregar automaticamente cinco leituras pre-definidas que cobrem todos os cenarios possiveis, do mais estavel ao mais critico.

### Limpeza de Tela

O programa utiliza `import os` e a funcao `os.system` para limpar o terminal a cada transicao de tela, mantendo a interface organizada sem o uso de bibliotecas externas alem das nativas do Python.

### Como Executar

```bash
python space_mission_monitor.py
```

---

## Projeto 3 — Energy Mission Monitor

**Disciplina:** Ciencia da Computacao — Solucoes em Energias Renovaveis e Sustentaveis  
**Arquivo:** `energy_mission_monitor.py`

### Contexto

O Energy Mission Monitor expande o conceito do projeto anterior para focar especificamente nos sistemas energeticos da nave. O projeto aplica conceitos de energia, potencia e eficiencia energetica ao contexto de uma missao espacial, simulando o monitoramento de fontes renovaveis de energia.

### Modulos Monitorados

O sistema monitora cinco modulos:

- **Painel Solar:** representa a geracao de energia renovavel por meio de radiacao solar, principal fonte energetica de satelites e naves espaciais;
- **Bateria Principal:** representa o sistema de armazenamento e reserva de energia;
- **Reator de Fusao:** representa a fonte de energia primaria de alta potencia da nave;
- **Sistema Termico:** monitora a temperatura interna dos sistemas energeticos;
- **Comunicacao:** monitora a qualidade do sinal com a base terrestre.

### Calculo de Potencia e Eficiencia

O sistema calcula a potencia estimada de cada modulo energetico em cada ciclo, usando um fator de degradacao que diminui ao longo dos ciclos para simular o desgaste natural dos sistemas. A eficiencia energetica geral e calculada como a media dos tres modulos de energia dividida pela capacidade maxima, expressa em percentual. Com base nessa eficiencia, o sistema emite um diagnostico automatico: boa eficiencia (acima de 70%), eficiencia moderada (entre 40% e 70%) ou eficiencia critica (abaixo de 40%).

### Dados Simulados

O dicionario `modulos` contem seis leituras pre-definidas para cada um dos cinco modulos, representando a trajetoria da missao do inicio ao fim. Os valores foram escolhidos para simular um cenario realista de degradacao gradual seguida de tentativa de recuperacao.

### Menu Interativo

O sistema possui as mesmas cinco opcoes do projeto anterior, com o acrescimo da exibicao de potencia estimada por modulo na opcao de monitoramento por ciclos.

### Como Executar

```bash
python energy_mission_monitor.py
```

---

## Projeto 4 — Analise Estatistica de Energia Solar Mundial

**Disciplina:** Modelagem Linear  
**Arquivos:** `analise_estatistica.py`, `energia_solar_mundial.csv`, `relatorio_estatistico.pdf`

### Contexto

Este projeto aplica tecnicas de estatistica descritiva a dados reais de geracao de energia solar em 20 paises entre 2000 e 2025. A analise foi feita em Python e os resultados foram organizados em um relatorio estatistico em formato PDF.

### Base de Dados

A base de dados utilizada e o **Our World in Data — Energy Data**, disponivel publicamente no repositorio GitHub `owid/energy-data` sob licenca Creative Commons BY 4.0. Trata-se de uma base amplamente utilizada em pesquisas academicas e jornalismo de dados, contendo 23.378 registros e 130 variaveis de energia por pais e ano.

A base foi filtrada para 20 paises relevantes (Brasil, Estados Unidos, China, Alemanha, India, Japao, Reino Unido, Franca, Australia, Espanha, Italia, Coreia do Sul, Holanda, Dinamarca, Suecia, Noruega, Canada, Mexico, Argentina e Chile), abrangendo o periodo de 2000 a 2025, resultando em 520 registros com dados nao nulos para as variaveis de interesse.

A escolha desta base justifica-se pela aderencia direta ao tema da Global Solution: a energia solar e a principal fonte energetica de satelites e missoes espaciais, tornando sua analise estatistica diretamente relevante para o desenvolvimento de sistemas como o Energy Mission Monitor.

### Variaveis Analisadas

- **year** (ano): variavel quantitativa discreta, utilizada na tabela de distribuicao de frequencias do Exercicio 2a;
- **solar_electricity** (geracao solar em TWh): variavel quantitativa continua, utilizada na tabela de frequencias do Exercicio 2b e na primeira analise univariada;
- **solar_share_elec** (participacao solar na geracao eletrica, em percentual): variavel quantitativa continua, utilizada na segunda analise univariada.

### Tabelas de Distribuicao de Frequencias

A tabela da variavel discreta (`year`) apresenta frequencia absoluta, frequencia absoluta acumulada, frequencia relativa e frequencia relativa acumulada para cada ano. Como os 20 paises possuem exatamente uma observacao por ano, a distribuicao e perfeitamente uniforme, com 20 registros por ano e frequencia relativa de 0,0385.

A tabela da variavel continua (`solar_electricity`) foi construida com oito classes de igual amplitude, calculada por divisao do intervalo total pelo numero de classes. A concentracao de 97,3% dos registros na primeira classe confirma a forte assimetria positiva da distribuicao.

### Graficos

Foram gerados dois graficos com a biblioteca matplotlib:

- **Grafico 1 (linhas):** evolucao da geracao solar em TWh para cinco paises selecionados entre 2000 e 2024, com titulo, rotulos dos eixos x e y, legenda por pais e grade horizontal;
- **Grafico 2 (barras horizontais):** participacao percentual da energia solar na geracao eletrica total de cada pais em 2023, com titulo, rotulos dos eixos, valores exibidos ao lado de cada barra e o Brasil destacado em laranja.

### Analise Univariada

Para cada uma das duas variaveis continuas foram calculadas:

- **Medidas de tendencia central:** media, mediana e moda;
- **Medidas de dispersao:** maximo, minimo, amplitude, variancia (com ddof=1), desvio padrao e coeficiente de variacao;
- **Medidas separatrizes:** primeiro quartil (Q1), segundo quartil ou mediana (Q2), terceiro quartil (Q3) e intervalo interquartil (IIQ).

### Principais Resultados

Para a geracao solar (TWh), a media de 21,12 TWh e muito superior a mediana de 0,82 TWh, indicando forte assimetria positiva. O coeficiente de variacao de 379,8% confirma a heterogeneidade extrema entre os paises, reflexo da concentracao da producao em poucos grandes players como China e Estados Unidos.

Para a participacao solar, a media de 2,45% com CV de 173,7% demonstra que a transicao energetica solar ainda e desigual. O terceiro quartil de 3,35% indica que 75% dos registros historicos apresentam participacao abaixo desse valor.

O Brasil saiu de geracao praticamente nula em 2013 para 50,63 TWh em 2023, crescimento de mais de 10.000 vezes em uma decada, posicionando o pais como um dos maiores mercados solares emergentes do mundo.

### Bibliotecas Utilizadas

- `pandas`: carregamento, filtragem e manipulacao da base de dados;
- `matplotlib`: geracao dos graficos estatisticos;
- `scipy.stats`: calculo da moda;
- `numpy`: operacoes numericas auxiliares;
- `reportlab`: geracao do relatorio em formato PDF.

### Como Executar

```bash
pip install pandas matplotlib scipy reportlab
python analise_estatistica.py
```

O relatorio PDF ja esta disponivel no arquivo `relatorio_estatistico.pdf`.

---

## Requisitos Gerais

- Python 3.x instalado
- Os projetos 1, 2 e 3 nao requerem nenhuma biblioteca externa alem de `os`, que ja faz parte da biblioteca padrao do Python
- O projeto 4 requer instalacao das bibliotecas listadas acima

---

## Observacoes Finais

Os quatro projetos foram desenvolvidos de forma integrada, compartilhando o mesmo contexto narrativo da Missao Marte. A progressao entre eles reflete o aprofundamento tecnico ao longo do semestre: do monitoramento basico por ciclos (Projeto 1), passando pelo sistema interativo com historico (Projeto 2), pelo foco em sistemas energeticos com calculo de eficiencia (Projeto 3), ate a analise estatistica rigorosa de dados reais (Projeto 4).

Todos os projetos foram desenvolvidos priorizando clareza, organizacao do codigo, uso correto das estruturas de dados ensinadas em aula e aderencia ao tema da Global Solution 2026.1.
