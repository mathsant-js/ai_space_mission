def exibir_introducao_missao():
    print("============================================================")
    print("AI SPACE MISSION")
    print("============================================================")
    print("Missão: Moon Test Ômega")
    print("Equipe: Equipe Alpha")
    print(f"Quantidade de Ciclos Analisados: 6")
    print()

def percorrer_ciclo_missao():
    risco_temperatura = 0
    risco_comunicacao = 0
    for i in range(len(dados_missao)):
        risco_temperatura += analisar_temperatura(dados_missao[i][0])
        risco_comunicacao += analisar_comunicacao(dados_missao[i][1])
        print(f"Temperatura: {dados_missao[i][0]} °C | {calcular_pontuacao_risco(risco_temperatura)}")
        print(f"Comunicação: {dados_missao[i][1]}% | {calcular_pontuacao_risco(risco_comunicacao)}")
        print(f"Bateria: {dados_missao[i][2]}%")
        print(f"Oxigênio: {dados_missao[i][3]}%")
        print(f"Estabilidade: {dados_missao[i][4]}%")
        print()

def calcular_pontuacao_risco(pontuacao):
    match pontuacao:
        case _ if pontuacao < 3:
            return "NORMAL"
        case _ if pontuacao < 6:
            return "ATENÇÃO"
        case _:
            return "CRÍTICO"

def analisar_temperatura(temperatura):
    risco = 0
    match temperatura:
        case _ if temperatura < 18 or temperatura > 30 and temperatura <= 35:
            risco += 1
        case _:
            risco += 2
    return risco

def analisar_comunicacao(comunicacao):
    risco = 0
    match comunicacao:
        case _ if comunicacao < 30:
            risco += 2
        case _ if comunicacao <= 59:
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