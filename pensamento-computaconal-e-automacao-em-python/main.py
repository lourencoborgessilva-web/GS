# =============================================================
# MISSION CONTROL AI
# Sistema Inteligente de Monitoramento de Missão Espacial
# =============================================================

NOME_MISSAO = "Missão Marte"
NOME_EQUIPE  = "Equipe Pioneira"

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

# Matriz principal: [temperatura(°C), comunicacao(%), bateria(%), oxigenio(%), estabilidade(%)]
dados_missao = [
    [22, 95, 91, 97, 93],   # Ciclo 1 — início da missão (estável)
    [26, 82, 75, 95, 87],   # Ciclo 2 — estabilização dos sistemas
    [32, 61, 54, 90, 68],   # Ciclo 3 — queda parcial de comunicação
    [37, 40, 35, 85, 52],   # Ciclo 4 — alerta de energia
    [41, 25, 17, 76, 33],   # Ciclo 5 — risco operacional crítico
    [35, 52, 30, 81, 48],   # Ciclo 6 — tentativa de recuperação
]

# ------------------------------------------------------------------
# FUNÇÕES DE ANÁLISE POR VARIÁVEL
# Cada função retorna (classificação, pontuação, mensagem)
# ------------------------------------------------------------------

def analisar_temperatura(valor):
    """Classifica a temperatura interna do módulo (°C)."""
    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura baixa"
    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):
    """Classifica a qualidade do sinal de comunicação (%)."""
    if valor < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico"
    elif valor < 60:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(valor):
    """Classifica o nível de bateria da missão (%)."""
    if valor < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif valor < 50:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(valor):
    """Classifica o nível de oxigênio disponível (%)."""
    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif valor < 90:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(valor):
    """Classifica a estabilidade geral dos sistemas (%)."""
    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif valor < 70:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


# ------------------------------------------------------------------
# CLASSIFICAÇÃO DO CICLO
# ------------------------------------------------------------------

def classificar_ciclo(pontuacao):
    """Retorna o status do ciclo com base na pontuação total de risco."""
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


# ------------------------------------------------------------------
# RECOMENDAÇÃO AUTOMÁTICA
# ------------------------------------------------------------------

def gerar_recomendacao(resultados):
    """
    Gera uma recomendação baseada nos alertas do ciclo.
    resultados = lista de (classificação, pontuação, mensagem) para cada variável.
    """
    tem_critico = any(r[0] == "CRÍTICO" for r in resultados)
    tem_atencao = any(r[0] == "ATENÇÃO" for r in resultados)

    # Recomendações específicas para situações críticas
    msgs = []
    nomes = ["temperatura", "comunicação", "bateria", "oxigênio", "estabilidade"]
    acoes = [
        "verificar controle térmico da missão",
        "tentar restabelecer contato com a base",
        "ativar modo de economia de energia",
        "acionar protocolo de suporte à vida",
        "reduzir operações não essenciais"
    ]

    for i, (classe, _, _) in enumerate(resultados):
        if classe == "CRÍTICO":
            msgs.append(acoes[i].capitalize())

    if len(msgs) >= 3:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."
    elif msgs:
        return " | ".join(msgs) + "."
    elif tem_atencao:
        return "Monitorar sistemas em atenção e preparar plano de contingência."
    else:
        return "Manter operação normal e continuar monitoramento."


# ------------------------------------------------------------------
# ANÁLISE DE TENDÊNCIA
# ------------------------------------------------------------------

def analisar_tendencia(riscos):
    """Compara o risco do primeiro e do último ciclo."""
    primeiro = riscos[0]
    ultimo   = riscos[-1]
    if ultimo > primeiro:
        return "A missão apresentou tendência de PIORA."
    elif ultimo < primeiro:
        return "A missão apresentou tendência de MELHORA."
    else:
        return "A missão permaneceu ESTÁVEL em relação ao início."


# ------------------------------------------------------------------
# ÁREA MAIS AFETADA
# ------------------------------------------------------------------

def identificar_area_mais_afetada(pontuacoes_por_area):
    """Retorna o nome da área com maior pontuação acumulada de risco."""
    indice_max = pontuacoes_por_area.index(max(pontuacoes_por_area))
    return areas_monitoradas[indice_max]


# ------------------------------------------------------------------
# RELATÓRIO FINAL
# ------------------------------------------------------------------

def gerar_relatorio_final(dados, riscos_ciclos, resultados_ciclos):
    """Exibe o relatório consolidado da missão."""
    num_ciclos = len(dados)

    # Médias por variável
    media_temp  = sum(c[0] for c in dados) / num_ciclos
    media_com   = sum(c[1] for c in dados) / num_ciclos
    media_bat   = sum(c[2] for c in dados) / num_ciclos
    media_oxy   = sum(c[3] for c in dados) / num_ciclos
    media_est   = sum(c[4] for c in dados) / num_ciclos

    # Ciclo mais crítico
    maior_risco  = max(riscos_ciclos)
    ciclo_critico = riscos_ciclos.index(maior_risco) + 1

    risco_medio   = sum(riscos_ciclos) / num_ciclos
    ciclos_criticos = sum(1 for r in riscos_ciclos if r >= 6)

    # Tendência
    tendencia = analisar_tendencia(riscos_ciclos)

    # Pontuação acumulada por área
    pontuacoes_area = [0] * 5
    for resultado in resultados_ciclos:
        for i, (_, pts, _) in enumerate(resultado):
            pontuacoes_area[i] += pts

    area_afetada = identificar_area_mais_afetada(pontuacoes_area)

    # Classificação final (com base no risco médio arredondado)
    classificacao_final = classificar_ciclo(round(risco_medio))

    # Conclusão automática
    if classificacao_final == "MISSÃO CRÍTICA":
        conclusao = ("A missão entrou em estado crítico durante a operação. "
                     "É necessária intervenção imediata e ativação de todos os protocolos de segurança.")
    elif classificacao_final == "MISSÃO EM ATENÇÃO":
        conclusao = ("A missão apresentou instabilidade relevante durante a operação. "
                     "Apesar da tentativa de recuperação no último ciclo, ainda existem sistemas "
                     "em atenção e a equipe deve manter o plano de contingência ativo.")
    else:
        conclusao = ("A missão transcorreu dentro dos parâmetros esperados. "
                     "Todos os sistemas operaram de forma satisfatória.")

    print("=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão : {NOME_MISSAO}")
    print(f"Equipe : {NOME_EQUIPE}")
    print()
    print(f"Quantidade de ciclos analisados : {num_ciclos}")
    print()
    print(f"Média de temperatura  : {media_temp:.2f} °C")
    print(f"Média de comunicação  : {media_com:.2f}%")
    print(f"Média de bateria      : {media_bat:.2f}%")
    print(f"Média de oxigênio     : {media_oxy:.2f}%")
    print(f"Média de estabilidade : {media_est:.2f}%")
    print()
    print(f"Ciclo mais crítico      : Ciclo {ciclo_critico}")
    print(f"Maior pontuação de risco: {maior_risco}")
    print(f"Risco médio da missão   : {risco_medio:.2f}")
    print(f"Quantidade de ciclos críticos: {ciclos_criticos}")
    print()
    print("Tendência da missão:")
    print(f"  {tendencia}")
    print()
    print("Pontuação acumulada por área:")
    for i, area in enumerate(areas_monitoradas):
        print(f"  {area}: {pontuacoes_area[i]} pontos")
    print()
    print("Área mais afetada:")
    print(f"  {area_afetada}")
    print()
    print("Classificação final da missão:")
    print(f"  {classificacao_final}")
    print()
    print("Conclusão:")
    print(f"  {conclusao}")
    print("=" * 60)


# ------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------------

def main():
    print("=" * 60)
    print("        MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missão  : {NOME_MISSAO}")
    print(f"Equipe  : {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 60)

    riscos_ciclos     = []
    resultados_ciclos = []

    for numero_ciclo, ciclo in enumerate(dados_missao, start=1):
        temp, com, bat, oxy, est = ciclo

        # Analisar cada variável
        r_temp = analisar_temperatura(temp)
        r_com  = analisar_comunicacao(com)
        r_bat  = analisar_bateria(bat)
        r_oxy  = analisar_oxigenio(oxy)
        r_est  = analisar_estabilidade(est)

        resultados = [r_temp, r_com, r_bat, r_oxy, r_est]
        resultados_ciclos.append(resultados)

        # Pontuação total do ciclo
        pontuacao = sum(r[1] for r in resultados)
        riscos_ciclos.append(pontuacao)

        status       = classificar_ciclo(pontuacao)
        recomendacao = gerar_recomendacao(resultados)

        # Exibir ciclo
        print(f"\nCICLO {numero_ciclo} " + "-" * 44)
        print(f"  Temperatura : {temp} °C  | {r_temp[0]:8s} | {r_temp[2]}")
        print(f"  Comunicação : {com}%    | {r_com[0]:8s} | {r_com[2]}")
        print(f"  Bateria     : {bat}%    | {r_bat[0]:8s} | {r_bat[2]}")
        print(f"  Oxigênio    : {oxy}%    | {r_oxy[0]:8s} | {r_oxy[2]}")
        print(f"  Estabilidade: {est}%    | {r_est[0]:8s} | {r_est[2]}")
        print(f"\n  Pontuação de risco do ciclo : {pontuacao}")
        print(f"  Classificação do ciclo      : {status}")
        print(f"  Recomendação: {recomendacao}")

    print()
    gerar_relatorio_final(dados_missao, riscos_ciclos, resultados_ciclos)


if __name__ == "__main__":
    main()