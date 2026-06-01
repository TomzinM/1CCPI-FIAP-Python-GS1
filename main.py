dados_missao = [
    [22, 95, 91, 97, 92], # Ciclo 1 — início da missão
    [25, 83, 70, 93, 85], # Ciclo 2 — estabilização dos sistemas
    [29, 35, 63, 91, 71], # Ciclo 3 — queda parcial de comunicação
    [34, 42, 31, 83, 53], # Ciclo 4 — alerta de energia
    [40, 24, 18, 74, 32], # Ciclo 5 — risco operacional
    [32, 53, 31, 84, 51]  # Ciclo 6 — tentativa de recuperação

]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

tempRegistros = []
commRegistros = []
enerRegistros = []
oxigRegistros = []
stabRegistros = []
indiceRegistros = []

missionName = "Erebus Test Alpha"
missionCrew = "Equipe Nyx"


# Classificação da missão no ciclo atual
def classificar(cycle):
    score = tempRegistros[cycle] + commRegistros[cycle] + enerRegistros[cycle] + oxigRegistros[cycle] + stabRegistros[cycle]
    indiceRegistros.append(score)
    print()
    print(f"Pontuação de risco do Ciclo: {indiceRegistros[cycle]}")
    if 3 <= indiceRegistros[cycle] <= 5:
        print(f"Classificação do Ciclo: MISSÃO EM ATENÇÃO")
    elif 6 <= indiceRegistros[cycle] <= 10:
        print(f"Classificação do Ciclo: MISSÃO CRÍTICA")
    else:
        print(f"Classificação do Ciclo: MISSÃO ESTÁVEL")

def recomendacao(cycle):
    sistemas = [
        ("OXIGÊNIO", oxigRegistros, "Acionar protocolo de suporte à vida.",
         "Monitores de O2 em alerta. Verificar taxa de fluxo."),

        ("TEMPERATURA", tempRegistros, "Risco de superaquecimento! Ativar resfriamento de emergência.",
         "Verificar controle térmico da missão."),

        ("ESTABILIDADE", stabRegistros, "Instabilidade severa! Evacuar setores não pressurizados.",
         "Reduzir operações não essenciais.."),

        ("COMUNICAÇÃO", commRegistros, "Perda extrema de sinal, ativar antena reserva.",
         "Tentar restabelecer contato com a base."),

        ("ENERGIA", enerRegistros, "Apagão iminente, desligar sistemas não vitais.",
         "Ativar modo de economia de energia.")
    ]

    for nome, registros, msg_critica, _ in sistemas:
        if registros[cycle] == 2:
            print(f"[{nome} CRÍTICO]: {msg_critica}")
            return

    for nome, registros, _, msg_atencao in sistemas:
        if registros[cycle] == 1:
            print(f"[{nome} EM ATENÇÃO]: {msg_atencao}")
            return

    print("Manter operação normal e continuar monitoramento.")


# Analise completa de todos os dados em dados_missao
def analise():
    for i, dado in enumerate(dados_missao):
        temp = dado[0]
        comm = dado[1]
        ener = dado[2]
        oxig = dado[3]
        stab = dado[4]

        print(f"CICLO {i + 1}")
        print("-" * 60)
        if temp < 18 or (30 <= temp <= 35):
            print(f"Temperatura ({temp}°C) | ATENÇÃO | Temperatura elevada")
            tempRegistros.append(1)
        elif temp > 35:
            print(f"Temperatura ({temp}°C) | CRÍTICO | Risco de superaquecimento")
            tempRegistros.append(2)
        else:
            print(f"Temperatura ({temp}°C) | NORMAL | Temperatura estável")
            tempRegistros.append(0)

        if 30 <= comm <= 59:
            print(f"Comunicação ({comm}%) | ATENÇÃO | Comunicação instável")
            commRegistros.append(1)
        elif comm < 30:
            print(f"Comunicação ({comm}%) | CRÍTICO | Comunicação com base em nível crítico")
            commRegistros.append(2)
        else:
            print(f"Comunicação ({comm}%) | NORMAL | Comunicação estável")
            commRegistros.append(0)

        if 20 <= ener <= 39:
            print(f"Energia ({ener}%) | ATENÇÃO | Bateria abaixo do recomendado")
            enerRegistros.append(1)
        elif ener < 20:
            print(f"Energia ({ener}%) | CRÍTICO | Bateria em nível crítico")
            enerRegistros.append(2)
        else:
            print(f"Energia ({ener}%) | NORMAL | Energia estável")
            enerRegistros.append(0)

        if 80 <= oxig <= 89:
            print(f"Oxigenio ({oxig}%) | ATENÇÃO | Oxigênio abaixo do ideal")
            oxigRegistros.append(1)
        elif oxig < 80:
            print(f"Oxigenio ({oxig}%) | CRÍTICO | Oxigênio em nível crítico")
            oxigRegistros.append(2)
        else:
            print(f"Oxigenio ({oxig}%) | NORMAL | Oxigênio adequado")
            oxigRegistros.append(0)

        if 40 <= stab <= 69:
            print(f"Estabilidade ({stab}%) | ATENÇÃO | Estabilidade operacional reduzida")
            stabRegistros.append(1)
        elif stab < 40:
            print(f"Estabilidade ({stab}%) | CRÍTICO | Estabilidade operacional crítica")
            stabRegistros.append(2)
        else:
            print(f"Estabilidade ({stab}%) | NORMAL | Estabilidade operacional adequada")
            stabRegistros.append(0)

        classificar(i)
        recomendacao(i)
        print()

# Relatorio final da missão
def relatorio():
    tempMedia = 0
    commMedia = 0
    enerMedia = 0
    oxigMedia = 0
    stabMedia = 0

    for i, dado in enumerate(dados_missao):
        tempMedia += dado[0]
        commMedia += dado[1]
        enerMedia += dado[2]
        oxigMedia += dado[3]
        stabMedia += dado[4]

    tempMedia /= len(dados_missao)
    commMedia /= len(dados_missao)
    enerMedia /= len(dados_missao)
    oxigMedia /= len(dados_missao)
    stabMedia /= len(dados_missao)

    mediaCritica = sum(indiceRegistros) / len(indiceRegistros)
    cicloCritico = max(indiceRegistros)
    criticoCount = []
    ciclosCriticos = 0

    pontosAcumulados = [sum(tempRegistros), sum(commRegistros), sum(enerRegistros), sum(oxigRegistros), sum(stabRegistros)]

    for i, ciclo in enumerate(indiceRegistros):
        if ciclo == cicloCritico:
            criticoNumero = i + 1
            criticoCount.append(criticoNumero)
            if ciclo > 6:
                ciclosCriticos += 1

    print(f"Média de temperatura: {round(tempMedia, 2)} °C")
    print(f"Média de comunicação: {round(commMedia, 2)}%")
    print(f"Media de bateria: {round(enerMedia, 2)}%")
    print(f"Média de oxigênio: {round(oxigMedia, 2)}%")
    print(f"Média de estabilidade: {round(stabMedia, 2)}%")
    print()

    if cicloCritico == 0:
        print(f"Nenhum dos ciclos foram criticos.")
    elif len(criticoCount) > 1:
        ciclos_str = ", ".join(map(str, criticoCount))
        print(f"Ciclos mais críticos: Ciclos {ciclos_str}")
    elif len(criticoCount) == 1:
        print(f"Ciclo mais crítico: Ciclo {criticoCount[0]}")
    print(f"Maior pontuação de risco: {cicloCritico}")
    print(f"Risco médio da missão: {round(mediaCritica, 2)}")
    print(f"Quantidade de ciclos criticos: {ciclosCriticos}")
    print()

    print("Tendencia da missão:")
    if indiceRegistros[0] > indiceRegistros[-1]:
        print("A missão apresentou tendência de melhora.")
    elif indiceRegistros[0] < indiceRegistros[-1]:
        print("A missão apresentou tendência de piora.")
    else: print("A missão permaneceu estável em relação ao início.")
    print()

    print("Pontuação acumulada por área:")
    for i, area in enumerate(areas_monitoradas):
        print(f"{area}: {pontosAcumulados[i]} pontos")
    print()

    print("Area mais afetada:")
    print(f"{areas_monitoradas[pontosAcumulados.index(max(pontosAcumulados))]}")
    print()

    print("Classificação final da missão:")
    if mediaCritica > 6:
        print("MISSÃO CRÍTICA")
    elif mediaCritica > 2:
        print("MISSÃO EM ATENÇÃO")
    else: print("MISSÃO ESTÁVEL")

# A função que chama todas as outras
def checkupCompleto():
    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missão: {missionName}")
    print(f"Equipe: {missionCrew}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 60)
    print()
    analise()
    print("=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão: {missionName}")
    print(f"Equipe: {missionCrew}")
    print()
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print()
    relatorio()

checkupCompleto()