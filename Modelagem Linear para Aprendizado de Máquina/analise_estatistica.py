# ===========================================================
# MODELAGEM LINEAR — GLOBAL SOLUTION 2026.1 — FIAP
# Análise Estatística: Energia Solar Mundial (2000–2024)
# Fonte: Our World in Data (OWID) — https://github.com/owid/energy-data
# ===========================================================

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from scipy import stats
import os

BASE_DIR = os.path.dirname(__file__)
OUTPUT_DIR = os.path.join(BASE_DIR, "CSV")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------------------------------------
# 1. CARREGAMENTO E DESCRIÇÃO DOS DADOS
# -----------------------------------------------------------
csv_path = os.path.join(BASE_DIR, "CSV", "energia_solar_mundial.csv")
if not os.path.exists(csv_path):
    csv_path = os.path.join(BASE_DIR, "energia_solar_mundial.csv")
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"Arquivo CSV não encontrado: {csv_path}")
df = pd.read_csv(csv_path)

print("=" * 60)
print("BASE DE DADOS: Energia Solar Mundial (2000–2024)")
print("Fonte: Our World in Data — owid/energy-data (GitHub)")
print("=" * 60)
print(f"\nDimensões: {df.shape[0]} linhas × {df.shape[1]} colunas")
print("\nColunas disponíveis:")
for c in df.columns:
    print(f"  - {c}")

# Variáveis de análise
# Quantitativa DISCRETA : year  (ano de referência, valores inteiros)
# Quantitativa CONTÍNUA : solar_electricity (TWh gerados, valores reais)

# -----------------------------------------------------------
# 2. TABELAS DE DISTRIBUIÇÃO DE FREQUÊNCIAS
# -----------------------------------------------------------

def tabela_frequencia_discreta(serie, nome):
    """Tabela de distribuição de frequências para variável discreta."""
    fi = serie.value_counts().sort_index()
    fri = fi / fi.sum()
    Fri = fri.cumsum()
    fi_ac = fi.cumsum()

    tabela = pd.DataFrame({
        "Ano (xi)": fi.index,
        "fi (freq. abs.)": fi.values,
        "fi acum.": fi_ac.values,
        "fri (freq. rel.)": fri.values.round(4),
        "Fri (freq. rel. acum.)": Fri.values.round(4),
    })
    print(f"\n{'=' * 60}")
    print(f"TABELA DE DISTRIBUIÇÃO DE FREQUÊNCIAS — {nome}")
    print(f"(Variável Quantitativa Discreta)")
    print(f"{'=' * 60}")
    print(tabela.to_string(index=False))
    return tabela


def tabela_frequencia_continua(serie, nome, n_classes=8):
    """Tabela de distribuição de frequências para variável contínua (Sturges)."""
    serie = serie.dropna()
    n = len(serie)
    k = n_classes
    h = (serie.max() - serie.min()) / k

    limites = [serie.min() + i * h for i in range(k + 1)]
    classes, fi_list, mp_list = [], [], []

    for i in range(k):
        li, ls = limites[i], limites[i + 1]
        if i < k - 1:
            cnt = ((serie >= li) & (serie < ls)).sum()
        else:
            cnt = ((serie >= li) & (serie <= ls)).sum()
        classes.append(f"[{li:.2f} ; {ls:.2f})")
        fi_list.append(cnt)
        mp_list.append(round((li + ls) / 2, 2))

    fi_arr = np.array(fi_list)
    fri_arr = fi_arr / n
    tabela = pd.DataFrame({
        "Classe": classes,
        "Ponto Médio": mp_list,
        "fi": fi_arr,
        "fi acum.": fi_arr.cumsum(),
        "fri": fri_arr.round(4),
        "Fri": fri_arr.cumsum().round(4),
    })

    print(f"\n{'=' * 60}")
    print(f"TABELA DE DISTRIBUIÇÃO DE FREQUÊNCIAS — {nome}")
    print(f"(Variável Quantitativa Contínua — {k} classes, h={h:.2f})")
    print(f"{'=' * 60}")
    print(tabela.to_string(index=False))
    return tabela


tab_discreta  = tabela_frequencia_discreta(df["year"], "Ano")
tab_continua  = tabela_frequencia_continua(df["solar_electricity"], "Geração Solar (TWh)")

# -----------------------------------------------------------
# 3. GRÁFICOS
# -----------------------------------------------------------

cores = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
         "#8c564b", "#e377c2", "#7f7f7f"]

# --- Gráfico 1: Evolução da geração solar — Brasil vs China vs Alemanha
fig1, ax1 = plt.subplots(figsize=(10, 5))

paises_g1 = ["Brazil", "China", "Germany", "United States", "India"]
for i, pais in enumerate(paises_g1):
    d = df[df["country"] == pais].sort_values("year")
    ax1.plot(d["year"], d["solar_electricity"],
             marker="o", markersize=4, linewidth=2,
             color=cores[i], label=pais)

ax1.set_title("Evolução da Geração Solar por País (2000–2024)\nFonte: Our World in Data", fontsize=13, pad=12)
ax1.set_xlabel("Ano", fontsize=11)
ax1.set_ylabel("Geração Solar (TWh)", fontsize=11)
ax1.legend(title="País", fontsize=9)
ax1.grid(axis="y", linestyle="--", alpha=0.5)
ax1.xaxis.set_major_locator(mticker.MultipleLocator(3))
fig1.tight_layout()
fig1.savefig(f"{OUTPUT_DIR}/grafico1_evolucao_solar.png", dpi=150)
plt.close(fig1)
print("\n[OK] Gráfico 1 salvo: grafico1_evolucao_solar.png")

# --- Gráfico 2: Participação solar na geração elétrica total em 2023 (barras)
df_2023 = df[df["year"] == 2023].dropna(subset=["solar_share_elec"]).sort_values("solar_share_elec", ascending=True)

fig2, ax2 = plt.subplots(figsize=(10, 5))
bars = ax2.barh(df_2023["country"], df_2023["solar_share_elec"],
                color=["#f4a416" if c == "Brazil" else "#1f77b4" for c in df_2023["country"]])
ax2.set_title("Participação da Energia Solar na Geração Elétrica Total — 2023\nFonte: Our World in Data", fontsize=13, pad=12)
ax2.set_xlabel("Participação Solar (%)", fontsize=11)
ax2.set_ylabel("País", fontsize=11)
for bar, val in zip(bars, df_2023["solar_share_elec"]):
    ax2.text(val + 0.1, bar.get_y() + bar.get_height() / 2,
             f"{val:.1f}%", va="center", fontsize=8)
ax2.grid(axis="x", linestyle="--", alpha=0.4)
fig2.tight_layout()
fig2.savefig(f"{OUTPUT_DIR}/grafico2_participacao_solar_2023.png", dpi=150)
plt.close(fig2)
print("[OK] Gráfico 2 salvo: grafico2_participacao_solar_2023.png")

# -----------------------------------------------------------
# 4. ANÁLISE UNIVARIADA — ESTATÍSTICA DESCRITIVA
# -----------------------------------------------------------

def estatistica_descritiva(serie, nome_var):
    """Calcula e imprime medidas de tendência central, dispersão e separatrizes."""
    s = serie.dropna()
    n = len(s)

    media    = s.mean()
    mediana  = s.median()
    moda_res = stats.mode(s, keepdims=True)
    moda     = moda_res.mode[0]

    maximo    = s.max()
    minimo    = s.min()
    amplitude = maximo - minimo
    variancia = s.var(ddof=1)
    dp        = s.std(ddof=1)
    cv        = (dp / media) * 100 if media != 0 else float("nan")

    q1, q2, q3 = s.quantile([0.25, 0.50, 0.75])

    print(f"\n{'=' * 60}")
    print(f"ANÁLISE UNIVARIADA — {nome_var}")
    print(f"{'=' * 60}")
    print(f"  n (observações)  : {n}")
    print(f"\n  MEDIDAS DE TENDÊNCIA CENTRAL")
    print(f"  Média            : {media:.4f}")
    print(f"  Mediana          : {mediana:.4f}")
    print(f"  Moda             : {moda:.4f}")
    print(f"\n  MEDIDAS DE DISPERSÃO")
    print(f"  Máximo           : {maximo:.4f}")
    print(f"  Mínimo           : {minimo:.4f}")
    print(f"  Amplitude        : {amplitude:.4f}")
    print(f"  Variância        : {variancia:.4f}")
    print(f"  Desvio Padrão    : {dp:.4f}")
    print(f"  Coef. Variação   : {cv:.2f}%")
    print(f"\n  MEDIDAS SEPARATRIZES")
    print(f"  Q1 (25%)         : {q1:.4f}")
    print(f"  Q2 (50%)         : {q2:.4f}")
    print(f"  Q3 (75%)         : {q3:.4f}")
    print(f"  IIQ (Q3 - Q1)    : {q3 - q1:.4f}")

    return {
        "variavel": nome_var, "n": n,
        "media": media, "mediana": mediana, "moda": moda,
        "max": maximo, "min": minimo, "amplitude": amplitude,
        "variancia": variancia, "dp": dp, "cv": cv,
        "q1": q1, "q2": q2, "q3": q3,
    }


est1 = estatistica_descritiva(df["solar_electricity"],    "Geração Solar (TWh)")
est2 = estatistica_descritiva(df["solar_share_elec"],     "Participação Solar na Eletricidade (%)")

# -----------------------------------------------------------
# 5. INTERPRETAÇÕES / INSIGHTS
# -----------------------------------------------------------

print(f"""
{'=' * 60}
INSIGHTS E INTERPRETAÇÕES
{'=' * 60}

1. GERAÇÃO SOLAR (TWh) — variável contínua
   A média de {est1['media']:.2f} TWh com desvio padrão de {est1['dp']:.2f} TWh
   indica altíssima dispersão (CV = {est1['cv']:.1f}%). Isso reflete a enorme
   diferença entre países como China (>1000 TWh) e nações menores.
   A mediana de {est1['mediana']:.2f} TWh, muito abaixo da média, revela
   distribuição assimétrica à direita — a maioria dos países ainda
   gera pouco, mas alguns gigantes elevam a média.

2. PARTICIPAÇÃO SOLAR (%) — variável contínua
   A participação média de {est2['media']:.2f}% com CV de {est2['cv']:.1f}%
   indica dispersão elevada. O Q3 de {est2['q3']:.2f}% mostra que 75%
   dos registros têm participação abaixo desse valor — a transição
   energética solar ainda está em curso na maioria dos países.

3. BRASIL (destaque)
   Em 2023, o Brasil gerou 50,63 TWh de energia solar, representando
   3,3% da geração elétrica total — crescimento de ~10.000x desde 2014.
   Esse crescimento exponencial posiciona o Brasil como um dos maiores
   mercados solares emergentes do mundo.

4. RELAÇÃO COM A MISSÃO ESPACIAL
   Assim como sistemas de painéis solares terrestres são monitorados
   para garantir eficiência máxima, o Energy Mission Monitor
   aplica a mesma lógica de análise contínua ao contexto espacial:
   identificar anomalias, calcular eficiência e acionar alertas
   automatizados diante de quedas no fornecimento energético.
""")

print("[OK] Análise completa.")
