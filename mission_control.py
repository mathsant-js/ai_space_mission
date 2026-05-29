risco_temperatura = 0
risco_comunicacao = 0
risco_bateria = 0
risco_oxigenio = 0
risco_estabilidade = 0

lista_risco = [risco_temperatura, risco_comunicacao, risco_bateria, risco_oxigenio, risco_estabilidade]

def exibir_introducao_missao():
    print("============================================================")
    print("AI SPACE MISSION")
    print("============================================================")
    print("Missão: Moon Test Ômega")
    print("Equipe: Equipe Alpha")
    print(f"Quantidade de Ciclos Analisados: {len(dados_missao)}")
    print()

def percorrer_ciclo_missao():
    for i in range(len(dados_missao)):
        global lista_risco
        atualizar_lista_risco(i)
        soma_risco = 0
        soma_risco += somar_risco_ciclo(soma_risco)
        print(f"CICLO {i + 1}")
        print("------------------------------------------------------------")
        print(f"Temperatura: {dados_missao[i][0]} °C | {analisar_temperatura(dados_missao[i][0])}")
        print(f"Comunicação: {dados_missao[i][1]}% | {analisar_comunicacao(dados_missao[i][1])}")
        print(f"Bateria: {dados_missao[i][2]}% | {analisar_bateria(dados_missao[i][2])}")
        print(f"Oxigênio: {dados_missao[i][3]}% | {analisar_oxigenio(dados_missao[i][3])}")
        print(f"Estabilidade: {dados_missao[i][4]}% | {analisar_estabilidade(dados_missao[i][4])}")
        print()
        print(f"Pontuação de risco do ciclo: {soma_risco}")
        print(f"Classificação do ciclo: {classificar_ciclo(soma_risco)}")
        print()

def atualizar_lista_risco(i):
    lista_risco[0] = somar_risco_temperatura(dados_missao[i][0])
    lista_risco[1] = somar_risco_comunicacao(dados_missao[i][1])
    lista_risco[2] = somar_risco_bateria(dados_missao[i][2])
    lista_risco[3] = somar_risco_oxigenio(dados_missao[i][3])
    lista_risco[4] = somar_risco_estabilidade(dados_missao[i][4])

def somar_risco_ciclo(soma_risco):
    for risco in lista_risco:
        soma_risco += risco
    return soma_risco

def classificar_ciclo(soma_risco):   
    match soma_risco:
        case _ if soma_risco < 3:
            return "MISSÃO ESTÁVEL"
        case _ if soma_risco < 6:
            return "MISSÃO EM ATENÇÃO"
        case _:
            return "MISSÃO CRÍTICA"

def analisar_temperatura(temperatura):
    match temperatura:
        case _ if temperatura < 18 or temperatura > 30 and temperatura <= 35:
            return "ATENÇÃO"
        case _ if temperatura > 35:
            return "CRÍTICO"
        case _:
            return "NORMAL"

def analisar_comunicacao(comunicacao):
    match comunicacao:
        case _ if comunicacao < 30:
            return "CRÍTICO"
        case _ if comunicacao <= 59:
            return "ATENÇÃO"
        case _:
            return "NORMAL"
        
def analisar_bateria(bateria):
    match bateria:
        case _ if bateria < 20:
            return "CRÍTICO"
        case _ if bateria <= 49:
            return "ATENÇÃO"
        case _:
            return "NORMAL"
        
def analisar_oxigenio(oxigenio):
    match oxigenio:
        case _ if oxigenio < 80:
            return "CRÍTICO"
        case _ if oxigenio <= 89:
            return "ATENÇÃO"
        case _:
            return "NORMAL"
        
def analisar_estabilidade(estabilidade):
    match estabilidade:
        case _ if estabilidade < 40:
            return "CRÍTICO"
        case _ if estabilidade <= 69:
            return "ATENÇÃO"
        case _:
            return "NORMAL"

def somar_risco_temperatura(temperatura):
    risco = 0
    match temperatura:
        case _ if temperatura < 18 or temperatura > 30 and temperatura <= 35:
            risco += 1
        case _ if temperatura > 35:
            risco += 2
        case _:
            risco += 0
    return risco

def somar_risco_comunicacao(comunicacao):
    risco = 0
    match comunicacao:
        case _ if comunicacao < 30:
            risco += 2
        case _ if comunicacao <= 59:
            risco += 1
    return risco

def somar_risco_bateria(bateria):
    risco = 0
    match bateria:
        case _ if bateria < 20:
            risco += 2
        case _ if bateria <= 49:
            risco += 1
    return risco

def somar_risco_oxigenio(oxigenio):
    risco = 0
    match oxigenio:
        case _ if oxigenio < 80:
            risco += 2
        case _ if oxigenio <= 89:
            risco += 1
    return risco

def somar_risco_estabilidade(estabilidade):
    risco = 0
    match estabilidade:
        case _ if estabilidade < 40:
            risco += 2
        case _ if estabilidade <= 69:
            risco += 1
    return risco

dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

exibir_introducao_missao()
percorrer_ciclo_missao()