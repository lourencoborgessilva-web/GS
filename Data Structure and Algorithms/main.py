# ==================================================
# SPACE MISSION MONITOR
# Missao: Nova Horizonte Alpha | Equipe: Equipe Cosmos
# ==================================================

import os

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
    print("       SPACE MISSION MONITOR")
    print("       Missao: Marte")
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
# FUNCOES DE ANALISE
# --------------------------------------------------

def analisar_temperatura(temp):
    if temp > 80:
        return "CRITICO", "Alerta de superaquecimento"
    elif temp > 60:
        return "ATENCAO", "Temperatura elevada"
    else:
        return "NORMAL ", "Temperatura estavel"

def analisar_energia(energia):
    if energia < 20:
        return "CRITICO", "Acionar economia de energia"
    elif energia < 40:
        return "ATENCAO", "Energia abaixo do recomendado"
    else:
        return "NORMAL ", "Energia estavel"

def analisar_comunicacao(comunicacao):
    if comunicacao == 0:
        return "CRITICO", "Falha total de comunicacao"
    elif comunicacao < 50:
        return "ATENCAO", "Sinal instavel com a base"
    else:
        return "NORMAL ", "Comunicacao estavel"

def status_geral(st_temp, st_energ, st_com):
    if "CRITICO" in st_temp or "CRITICO" in st_energ or "CRITICO" in st_com:
        return "MISSAO CRITICA"
    elif "ATENCAO" in st_temp or "ATENCAO" in st_energ or "ATENCAO" in st_com:
        return "MISSAO EM ATENCAO"
    else:
        return "MISSAO ESTAVEL"

# --------------------------------------------------
# REGISTRAR E EXIBIR LEITURA
# --------------------------------------------------

def registrar_leitura(temp, energia, comunicacao):
    st_t, msg_t = analisar_temperatura(temp)
    st_e, msg_e = analisar_energia(energia)
    st_c, msg_c = analisar_comunicacao(comunicacao)
    status      = status_geral(st_t, st_e, st_c)

    leitura = [len(historico) + 1, temp, energia, comunicacao,
               st_t, msg_t, st_e, msg_e, st_c, msg_c, status]
    historico.append(leitura)
    return leitura

def exibir_leitura(leitura):
    numero      = leitura[0]
    temp        = leitura[1]
    energia     = leitura[2]
    comunicacao = leitura[3]
    st_t        = leitura[4]
    msg_t       = leitura[5]
    st_e        = leitura[6]
    msg_e       = leitura[7]
    st_c        = leitura[8]
    msg_c       = leitura[9]
    status      = leitura[10]

    linha()
    print("  Leitura #" + str(numero))
    linha()
    print("  Temperatura  : " + str(temp) + " C  |  " + st_t + "  |  " + msg_t)
    print("  Energia      : " + str(energia) + " %  |  " + st_e + "  |  " + msg_e)
    print("  Comunicacao  : " + str(comunicacao) + " %  |  " + st_c + "  |  " + msg_c)
    linha()
    print("  Status geral : " + status)
    linha()

# --------------------------------------------------
# OPCOES DO MENU
# --------------------------------------------------

def inserir_dados():
    cabecalho()
    print("  INSERIR DADOS\n")

    temp        = ler_numero("  Temperatura  (0 a 120 C) : ", 0, 120)
    energia     = ler_numero("  Energia      (0 a 100 %) : ", 0, 100)
    comunicacao = ler_numero("  Comunicacao  (0 a 100 %) : ", 0, 100)

    leitura = registrar_leitura(temp, energia, comunicacao)

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
    print("  ANALISE COMPLETA\n")

    if len(historico) == 0:
        print("  Nenhuma leitura para analisar.")
        pausar()
        return

    n           = len(historico)
    soma_temp   = 0
    soma_energ  = 0
    soma_com    = 0
    criticos    = 0
    atencao     = 0
    estaveis    = 0

    for leitura in historico:
        soma_temp  += leitura[1]
        soma_energ += leitura[2]
        soma_com   += leitura[3]

        if leitura[10] == "MISSAO CRITICA":
            criticos += 1
        elif leitura[10] == "MISSAO EM ATENCAO":
            atencao += 1
        else:
            estaveis += 1

    media_temp  = round(soma_temp  / n, 1)
    media_energ = round(soma_energ / n, 1)
    media_com   = round(soma_com   / n, 1)

    print("  Total de leituras   : " + str(n))
    linha()
    print("  Media temperatura   : " + str(media_temp) + " C")
    print("  Media energia       : " + str(media_energ) + " %")
    print("  Media comunicacao   : " + str(media_com) + " %")
    linha()
    print("  Leituras CRITICAS   : " + str(criticos))
    print("  Leituras EM ATENCAO : " + str(atencao))
    print("  Leituras ESTAVEIS   : " + str(estaveis))
    linha()

    pausar()

def simular_demo():
    cabecalho()
    print("  SIMULACAO AUTOMATICA\n")
    print("  Carregando dados de demonstracao...\n")

    dados_demo = [
        [22, 95, 90],
        [45, 70, 80],
        [65, 38, 60],
        [85, 15,  0],
        [50, 55, 75],
    ]

    for dados in dados_demo:
        leitura = registrar_leitura(dados[0], dados[1], dados[2])
        exibir_leitura(leitura)

    pausar()

def ver_historico():
    cabecalho()
    print("  HISTORICO DE LEITURAS\n")

    if len(historico) == 0:
        print("  Nenhuma leitura no historico ainda.")
        pausar()
        return

    print("  N   Temp(C)  Energia(%)  Comunicacao(%)  Status")
    linha()

    for leitura in historico:
        print("  " + str(leitura[0]) + "   " +
              str(leitura[1]) + "      " +
              str(leitura[2]) + "          " +
              str(leitura[3]) + "             " +
              leitura[10])

    linha()
    print("  Total: " + str(len(historico)) + " leitura(s)")
    pausar()

# --------------------------------------------------
# MENU PRINCIPAL
# --------------------------------------------------

opcao = ""
while opcao != "0":
    cabecalho()
    print("  MENU PRINCIPAL\n")
    print("  1 - Inserir dados")
    print("  2 - Visualizar status atual")
    print("  3 - Executar analise")
    print("  4 - Historico das leituras")
    print("  5 - Simulacao automatica (demo)")
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
        simular_demo()
    elif opcao == "0":
        cabecalho()
        print("  Sistema encerrado. Ate logo!\n")
    else:
        print("\n  Opcao invalida. Tente novamente.")
        pausar()