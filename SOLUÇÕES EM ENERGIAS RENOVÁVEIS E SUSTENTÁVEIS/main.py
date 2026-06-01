
import os

# --------------------------------------------------
# DADOS SIMULADOS DOS MODULOS DA MISSAO
# Cada modulo representa um sistema energetico
# da nave. Os valores sao listas com uma leitura
# por ciclo de monitoramento.
# --------------------------------------------------

modulos = {
    "Painel Solar":       [95, 88, 72, 40, 15, 60],
    "Bateria Principal":  [88, 75, 60, 35, 18, 45],
    "Reator de Fusao":    [100, 98, 85, 50, 22, 70],
    "Sistema Termico":    [30, 42, 61, 78, 88, 65],
    "Comunicacao":        [90, 80, 60, 40, 0,  55],
}

# Quantidade de ciclos simulados
TOTAL_CICLOS = 6

historico = []

# --------------------------------------------------
# FUNCOES AUXILIARES
# --------------------------------------------------

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def linha():
    print("--------------------------------------------------")

def cabecalho():
    limpar()
    linha()
    print("       ENERGY MISSION MONITOR")
    print("       Missao: Marte | GS 2026.1 - FIAP")
    print("       Equipe: Equipe Pioneira")
    linha()

def pausar():
    input("\nPressione ENTER para voltar ao menu...")

def ler_numero(mensagem, minimo, maximo):
    while True:
        try:
            valor = float(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            else:
                print("Valor invalido. Digite entre " + str(minimo) + " e " + str(maximo) + ".")
        except ValueError:
            print("Digite apenas numeros.")

# --------------------------------------------------
# FUNCOES DE ANALISE ENERGETICA
# --------------------------------------------------

def analisar_energia(valor):
    if valor < 20:
        return "CRITICO", "Nivel critico — risco de falha total"
    elif valor < 50:
        return "ATENCAO", "Nivel baixo — acionar reserva"
    else:
        return "NORMAL ", "Nivel adequado"

def analisar_temperatura(valor):
    if valor > 80:
        return "CRITICO", "Superaquecimento — risco ao sistema"
    elif valor > 60:
        return "ATENCAO", "Temperatura elevada — monitorar"
    else:
        return "NORMAL ", "Temperatura estavel"

def analisar_comunicacao(valor):
    if valor == 0:
        return "CRITICO", "Falha total de comunicacao"
    elif valor < 50:
        return "ATENCAO", "Sinal instavel com a base"
    else:
        return "NORMAL ", "Comunicacao estavel"

def calcular_potencia(energia, ciclo):
    # Potencia estimada = energia disponivel * fator do ciclo
    # Representa quantos watts o modulo esta gerando
    fator = [1.0, 0.95, 0.85, 0.60, 0.30, 0.70]
    return round(energia * fator[ciclo], 1)

def calcular_eficiencia(potencia_atual, potencia_maxima):
    if potencia_maxima == 0:
        return 0
    return round((potencia_atual / potencia_maxima) * 100, 1)

def status_geral_ciclo(alertas):
    if "CRITICO" in alertas:
        return "CICLO CRITICO"
    elif "ATENCAO" in alertas:
        return "CICLO EM ATENCAO"
    else:
        return "CICLO ESTAVEL"

def gerar_recomendacao(status):
    if status == "CICLO CRITICO":
        return "Acionar protocolo de emergencia e redistribuir energia."
    elif status == "CICLO EM ATENCAO":
        return "Reduzir consumo nos modulos nao essenciais."
    else:
        return "Manter operacao normal e continuar monitoramento."

# --------------------------------------------------
# REGISTRAR E EXIBIR LEITURA MANUAL
# --------------------------------------------------

def registrar_leitura_manual(painel, bateria, reator, temp, comunicacao):
    st_p,  msg_p  = analisar_energia(painel)
    st_b,  msg_b  = analisar_energia(bateria)
    st_r,  msg_r  = analisar_energia(reator)
    st_t,  msg_t  = analisar_temperatura(temp)
    st_c,  msg_c  = analisar_comunicacao(comunicacao)

    alertas = [st_p, st_b, st_r, st_t, st_c]
    status  = status_geral_ciclo(alertas)
    rec     = gerar_recomendacao(status)

    leitura = {
        "numero"      : len(historico) + 1,
        "painel"      : painel,
        "bateria"     : bateria,
        "reator"      : reator,
        "temperatura" : temp,
        "comunicacao" : comunicacao,
        "st_p"        : st_p,  "msg_p": msg_p,
        "st_b"        : st_b,  "msg_b": msg_b,
        "st_r"        : st_r,  "msg_r": msg_r,
        "st_t"        : st_t,  "msg_t": msg_t,
        "st_c"        : st_c,  "msg_c": msg_c,
        "status"      : status,
        "recomendacao": rec,
    }
    historico.append(leitura)
    return leitura

def exibir_leitura(leitura):
    linha()
    print("  Leitura #" + str(leitura["numero"]))
    linha()
    print("  Painel Solar      : " + str(leitura["painel"])      + " %  |  " + leitura["st_p"] + "  |  " + leitura["msg_p"])
    print("  Bateria Principal : " + str(leitura["bateria"])     + " %  |  " + leitura["st_b"] + "  |  " + leitura["msg_b"])
    print("  Reator de Fusao   : " + str(leitura["reator"])      + " %  |  " + leitura["st_r"] + "  |  " + leitura["msg_r"])
    print("  Sistema Termico   : " + str(leitura["temperatura"]) + " C  |  " + leitura["st_t"] + "  |  " + leitura["msg_t"])
    print("  Comunicacao       : " + str(leitura["comunicacao"]) + " %  |  " + leitura["st_c"] + "  |  " + leitura["msg_c"])
    linha()
    print("  Status     : " + leitura["status"])
    print("  Acao       : " + leitura["recomendacao"])
    linha()

# --------------------------------------------------
# OPCOES DO MENU
# --------------------------------------------------

def inserir_dados():
    cabecalho()
    print("  INSERIR DADOS MANUALMENTE\n")

    painel      = ler_numero("  Painel Solar      (0 a 100 %): ", 0, 100)
    bateria     = ler_numero("  Bateria Principal (0 a 100 %): ", 0, 100)
    reator      = ler_numero("  Reator de Fusao   (0 a 100 %): ", 0, 100)
    temperatura = ler_numero("  Sistema Termico   (0 a 120 C): ", 0, 120)
    comunicacao = ler_numero("  Comunicacao       (0 a 100 %): ", 0, 100)

    leitura = registrar_leitura_manual(painel, bateria, reator, temperatura, comunicacao)
    print("\n  Leitura registrada com sucesso!")
    exibir_leitura(leitura)
    pausar()

def visualizar_status():
    cabecalho()
    print("  STATUS ATUAL\n")

    if len(historico) == 0:
        print("  Nenhuma leitura registrada ainda.")
    else:
        print("  Ultima leitura registrada:\n")
        exibir_leitura(historico[-1])

    pausar()

def executar_analise():
    cabecalho()
    print("  ANALISE ENERGETICA COMPLETA\n")

    if len(historico) == 0:
        print("  Nenhuma leitura para analisar.")
        pausar()
        return

    n = len(historico)

    soma_painel   = 0
    soma_bateria  = 0
    soma_reator   = 0
    soma_temp     = 0
    soma_com      = 0
    criticos      = 0
    atencao       = 0
    estaveis      = 0

    for leitura in historico:
        soma_painel  += leitura["painel"]
        soma_bateria += leitura["bateria"]
        soma_reator  += leitura["reator"]
        soma_temp    += leitura["temperatura"]
        soma_com     += leitura["comunicacao"]

        if leitura["status"] == "CICLO CRITICO":
            criticos += 1
        elif leitura["status"] == "CICLO EM ATENCAO":
            atencao += 1
        else:
            estaveis += 1

    media_painel  = round(soma_painel  / n, 1)
    media_bateria = round(soma_bateria / n, 1)
    media_reator  = round(soma_reator  / n, 1)
    media_temp    = round(soma_temp    / n, 1)
    media_com     = round(soma_com     / n, 1)

    # Eficiencia energetica geral da missao
    energia_media    = round((media_painel + media_bateria + media_reator) / 3, 1)
    eficiencia_total = calcular_eficiencia(energia_media, 100)

    print("  Total de leituras       : " + str(n))
    linha()
    print("  Media Painel Solar      : " + str(media_painel)  + " %")
    print("  Media Bateria Principal : " + str(media_bateria) + " %")
    print("  Media Reator de Fusao   : " + str(media_reator)  + " %")
    print("  Media Sistema Termico   : " + str(media_temp)    + " C")
    print("  Media Comunicacao       : " + str(media_com)     + " %")
    linha()
    print("  Eficiencia energetica   : " + str(eficiencia_total) + " %")
    linha()
    print("  Ciclos CRITICOS         : " + str(criticos))
    print("  Ciclos EM ATENCAO       : " + str(atencao))
    print("  Ciclos ESTAVEIS         : " + str(estaveis))
    linha()

    # Diagnostico final
    if eficiencia_total >= 70:
        print("  Diagnostico: Missao operando com boa eficiencia energetica.")
    elif eficiencia_total >= 40:
        print("  Diagnostico: Eficiencia moderada. Revisar modulos em atencao.")
    else:
        print("  Diagnostico: Eficiencia critica. Acionar protocolos de emergencia.")

    linha()
    pausar()

def ver_historico():
    cabecalho()
    print("  HISTORICO DE LEITURAS\n")

    if len(historico) == 0:
        print("  Nenhuma leitura no historico ainda.")
        pausar()
        return

    print("  N    Painel  Bateria  Reator  Temp   Com    Status")
    linha()

    for leitura in historico:
        print("  " + str(leitura["numero"]) + "    " +
              str(leitura["painel"])      + "%     " +
              str(leitura["bateria"])     + "%     " +
              str(leitura["reator"])      + "%     " +
              str(leitura["temperatura"]) + "C    " +
              str(leitura["comunicacao"]) + "%    " +
              leitura["status"])

    linha()
    print("  Total: " + str(len(historico)) + " leitura(s)")
    pausar()

def monitorar_ciclos():
    cabecalho()
    print("  MONITORAMENTO POR CICLOS SIMULADOS\n")
    print("  Executando " + str(TOTAL_CICLOS) + " ciclos de monitoramento da missao Marte...\n")

    for ciclo in range(TOTAL_CICLOS):
        painel      = modulos["Painel Solar"][ciclo]
        bateria     = modulos["Bateria Principal"][ciclo]
        reator      = modulos["Reator de Fusao"][ciclo]
        temperatura = modulos["Sistema Termico"][ciclo]
        comunicacao = modulos["Comunicacao"][ciclo]

        leitura = registrar_leitura_manual(painel, bateria, reator, temperatura, comunicacao)

        print("  --- Ciclo " + str(ciclo + 1) + " ---")

        pot_painel  = calcular_potencia(painel,  ciclo)
        pot_bateria = calcular_potencia(bateria, ciclo)
        pot_reator  = calcular_potencia(reator,  ciclo)

        print("  Painel Solar      : " + str(painel)      + " %  |  Potencia estimada: " + str(pot_painel)  + " W  |  " + leitura["st_p"])
        print("  Bateria Principal : " + str(bateria)     + " %  |  Potencia estimada: " + str(pot_bateria) + " W  |  " + leitura["st_b"])
        print("  Reator de Fusao   : " + str(reator)      + " %  |  Potencia estimada: " + str(pot_reator)  + " W  |  " + leitura["st_r"])
        print("  Sistema Termico   : " + str(temperatura) + " C  |  " + leitura["st_t"] + "  |  " + leitura["msg_t"])
        print("  Comunicacao       : " + str(comunicacao) + " %  |  " + leitura["st_c"] + "  |  " + leitura["msg_c"])
        print("  Status do ciclo   : " + leitura["status"])
        print("  Acao recomendada  : " + leitura["recomendacao"])
        linha()

    pausar()

# --------------------------------------------------
# MENU PRINCIPAL
# --------------------------------------------------

opcao = ""
while opcao != "0":
    cabecalho()
    print("  MENU PRINCIPAL\n")
    print("  1 - Inserir dados manualmente")
    print("  2 - Visualizar status atual")
    print("  3 - Analise energetica completa")
    print("  4 - Historico de leituras")
    print("  5 - Monitorar ciclos simulados (demo)")
    print("  0 - Encerrar sistema")
    linha()

    opcao = input("  Escolha uma opcao: ")

    if opcao == "1":
        inserir_dados()
    elif opcao == "2":
        visualizar_status()
    elif opcao == "3":
        executar_analise()
    elif opcao == "4":
        ver_historico()
    elif opcao == "5":
        monitorar_ciclos()
    elif opcao == "0":
        cabecalho()
        print("  Sistema encerrado. Missao Marte — ate logo!\n")
    else:
        print("\n  Opcao invalida. Tente novamente.")
        pausar()