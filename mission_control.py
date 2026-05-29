risco_temperatura = 0
risco_comunicacao = 0
risco_bateria = 0
risco_oxigenio = 0
risco_estabilidade = 0

lista_risco = [risco_temperatura, risco_comunicacao, risco_bateria, risco_oxigenio, risco_estabilidade]
lista_soma_risco_ciclo = []

def exibir_introducao_missao():
    print("============================================================")
    print("AI SPACE MISSION")
    print("============================================================")
    print("Missão: Moon Test Ômega")
    print("Equipe: Equipe Alpha")
    print(f"Quantidade de Ciclos Analisados: {len(dados_missao)}")
    print("============================================================")
    print()

def percorrer_ciclo_missao():
    for i in range(len(dados_missao)):
        atualizar_lista_risco(i)
        soma_risco = somar_risco_ciclo()
        lista_soma_risco_ciclo.append(soma_risco)
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
        print(f"Recomendação: {gerar_recomendacao_ciclo(i)}")
        print()

def exibir_relatorio_final():
    print("============================================================")
    print("RELATÓRIO FINAL DA MISSÃO")
    print("============================================================")
    print("Missão: Moon Test Ômega")
    print("Equipe: Equipe Alpha")
    print()
    print(f"Quantidade de Ciclos Analisados: {len(dados_missao)}")
    print()
    exibir_media_informacoes()
    print()
    exibir_estatisticas_ciclos()
    print()
    print("Tendência da missão:")
    print("<tendencia_missao>")
    print()
    print("Pontuação acumuldada por área: ")
    print("")
    print()
    print("Área mais afetada:")
    print("")
    print()
    print("Classificação final da missão:")
    print("<classificao_final_missao>")
    print()
    print("Conclusão:")
    print("<análise_final>")
    
def exibir_estatisticas_ciclos():
    print(f"Ciclo mais crítico: Ciclo {exibir_ciclo_critico()}")
    print(f"Maior pontuação de risco: {exibir_maior_pontuacao_risco()}")
    print(f"Risco médio da missão: {exibir_media_risco_missao():.2f}")
    print(f"Quantidade de ciclos críticos: {exibir_quantidade_ciclo_critico()}")
    
def exibir_media_informacoes():
    print(f"Média de temperatura: {exibir_media_temperatura():.2f} °C")
    print(f"Média de comunicação: {exibir_media_comunicacao():.2f} %")
    print(f"Média de bateria: {exibir_media_bateria():.2f} %")
    print(f"Média de oxigênio: {exibir_media_oxigenio():.2f} %")
    print(f"Média de estabilidade: {exibir_media_estabilidade():.2f} %")

def calcular_media_informacao(coluna):
    soma = 0
    for i in range(len(dados_missao)):
        soma += dados_missao[i][coluna]
    return soma / len(dados_missao)

def exibir_media_temperatura():
    return calcular_media_informacao(0)

def exibir_media_comunicacao():
    return calcular_media_informacao(1)

def exibir_media_bateria():
    return calcular_media_informacao(2)

def exibir_media_oxigenio():
    return calcular_media_informacao(3)

def exibir_media_estabilidade():
    return calcular_media_informacao(4)

def atualizar_lista_risco(i):
    lista_risco[0] = somar_risco_temperatura(dados_missao[i][0])
    lista_risco[1] = somar_risco_comunicacao(dados_missao[i][1])
    lista_risco[2] = somar_risco_bateria(dados_missao[i][2])
    lista_risco[3] = somar_risco_oxigenio(dados_missao[i][3])
    lista_risco[4] = somar_risco_estabilidade(dados_missao[i][4])

def exibir_ciclo_critico():
    ciclo_critico = 0
    maior_risco = lista_soma_risco_ciclo[0]
    for i in range(1, len(lista_soma_risco_ciclo)):
        if lista_soma_risco_ciclo[i] > maior_risco:
            ciclo_critico = i
    return ciclo_critico

def exibir_quantidade_ciclo_critico():
    ciclos_criticos = 0
    for risco in lista_soma_risco_ciclo:
        if risco > 5:
            ciclos_criticos += 1
    return ciclos_criticos

def exibir_maior_pontuacao_risco():
    maior_risco = lista_soma_risco_ciclo[0]
    for risco in lista_soma_risco_ciclo:
        if risco > maior_risco:
            maior_risco = risco
    return maior_risco

def exibir_media_risco_missao():
    soma_risco = 0
    for risco in lista_soma_risco_ciclo:
        soma_risco += risco
    return soma_risco / len(lista_soma_risco_ciclo)        

def somar_risco_ciclo():
    soma_risco = 0
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
    
def gerar_recomendacao_ciclo(i):
    recomendacao = ""
    if somar_risco_temperatura(dados_missao[i][0]) > 0:
        recomendacao += "Verificar controle térmico da missão. "
    if somar_risco_comunicacao(dados_missao[i][1]) > 0:
        recomendacao += "Tentar reestabelecer contato com a base. "
    if somar_risco_bateria(dados_missao[i][2]) > 0:
        recomendacao += "Ativar modo de economia de energia. "
    if somar_risco_oxigenio(dados_missao[i][3]) > 0:
        recomendacao += "Acionar protocolo de suporte à vida. "
    if somar_risco_estabilidade(dados_missao[i][4]) > 0:
        recomendacao += "Reduzir operações não essenciais. "
    else:
        recomendacao = "Manter operação normal e continuar monitoramento."
    return recomendacao

def analisar_temperatura(temperatura):
    match temperatura:
        case _ if temperatura < 18 or temperatura > 30 and temperatura <= 35:
            return "ATENÇÃO | Temperatura elevada"
        case _ if temperatura > 35:
            return "CRÍTICO | Risco de superaquecimento"
        case _:
            return "NORMAL | Temperatura estável"

def analisar_comunicacao(comunicacao):
    match comunicacao:
        case _ if comunicacao < 30:
            return "CRÍTICO | Comunicação com a base em nível crítico"
        case _ if comunicacao <= 59:
            return "ATENÇÃO | Comunicação instável"
        case _:
            return "NORMAL | Comunicação estável"
        
def analisar_bateria(bateria):
    match bateria:
        case _ if bateria < 20:
            return "CRÍTICO | Bateria em nível crítico"
        case _ if bateria <= 49:
            return "ATENÇÃO | Bateria abaixo do recomendável"
        case _:
            return "NORMAL | Energia estável"
        
def analisar_oxigenio(oxigenio):
    match oxigenio:
        case _ if oxigenio < 80:
            return "CRÍTICO | Oxigênio em nível crítico"
        case _ if oxigenio <= 89:
            return "ATENÇÃO | Oxigênio abaixo do ideal"
        case _:
            return "NORMAL | Oxigênio adequado"
        
def analisar_estabilidade(estabilidade):
    match estabilidade:
        case _ if estabilidade < 40:
            return "CRÍTICO | Estabilidade operacional crítica"
        case _ if estabilidade <= 69:
            return "ATENÇÃO | Estabilidade operacional reduzida"
        case _:
            return "NORMAL | Estabilidade operacional adequada"

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
exibir_relatorio_final()