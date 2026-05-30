TEMPERATURA = 0
COMUNICACAO = 1
BATERIA = 2
OXIGENIO = 3
ESTABILIDADE = 4

risco_temperatura = 0
risco_comunicacao = 0
risco_bateria = 0
risco_oxigenio = 0
risco_estabilidade = 0

lista_soma_risco_ciclo = []
lista_soma_pontuacao = [0, 0, 0, 0, 0]
lista_risco = [risco_temperatura, risco_comunicacao, risco_bateria, risco_oxigenio, risco_estabilidade]

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
        calcular_acumulo_pontuacao(i)
        soma_risco = somar_risco_ciclo()
        lista_soma_risco_ciclo.append(soma_risco)
        print(f"CICLO {i + 1}")
        print("------------------------------------------------------------")
        print(f"Temperatura: {dados_missao[i][TEMPERATURA]} °C | {analisar_temperatura(dados_missao[i][TEMPERATURA])}")
        print(f"Comunicação: {dados_missao[i][COMUNICACAO]}% | {analisar_comunicacao(dados_missao[i][COMUNICACAO])}")
        print(f"Bateria: {dados_missao[i][BATERIA]}% | {analisar_bateria(dados_missao[i][BATERIA])}")
        print(f"Oxigênio: {dados_missao[i][OXIGENIO]}% | {analisar_oxigenio(dados_missao[i][OXIGENIO])}")
        print(f"Estabilidade: {dados_missao[i][ESTABILIDADE]}% | {analisar_estabilidade(dados_missao[i][ESTABILIDADE])}")
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
    exibir_tendencia()
    print()
    print("Pontuação acumuldada por área: ")
    exibir_pontuacao_acumulada()
    print()
    print("Área mais afetada:")
    exibir_area_mais_afetada()
    print()
    print("Classificação final da missão:")
    exibir_classificacao_final_missao()
    print()
    print("Conclusão:")
    print("A missão apresentou instabilidade relevante durante a operação. Apesar da tentativa de recuperação no último ciclo, ainda existem sistemas em atenção e a equipe deve manter o plano de contingência ativo.")
    
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

def exibir_tendencia():
    print(analisar_tendencia())

def exibir_classificacao_final_missao():
    print(calcular_classificacao_final_missao())

def exibir_area_mais_afetada():
    print(calcular_area_mais_afetada())
    
def exibir_pontuacao_acumulada():
    for ls, area in zip(lista_soma_pontuacao, areas_monitoradas):
        print(f"{area}: {ls} pontos")

def exibir_media_temperatura():
    return calcular_media_informacao(TEMPERATURA)

def exibir_media_comunicacao():
    return calcular_media_informacao(COMUNICACAO)

def exibir_media_bateria():
    return calcular_media_informacao(BATERIA)

def exibir_media_oxigenio():
    return calcular_media_informacao(OXIGENIO)

def exibir_media_estabilidade():
    return calcular_media_informacao(ESTABILIDADE)

def atualizar_lista_risco(i):
    lista_risco[TEMPERATURA] = somar_risco_temperatura(dados_missao[i][TEMPERATURA])
    lista_risco[COMUNICACAO] = somar_risco_comunicacao(dados_missao[i][COMUNICACAO])
    lista_risco[BATERIA] = somar_risco_bateria(dados_missao[i][BATERIA])
    lista_risco[OXIGENIO] = somar_risco_oxigenio(dados_missao[i][OXIGENIO])
    lista_risco[ESTABILIDADE] = somar_risco_estabilidade(dados_missao[i][ESTABILIDADE])

def calcular_acumulo_pontuacao(i):
    lista_soma_pontuacao[TEMPERATURA] += somar_risco_temperatura(dados_missao[i][TEMPERATURA])
    lista_soma_pontuacao[COMUNICACAO] += somar_risco_comunicacao(dados_missao[i][COMUNICACAO])
    lista_soma_pontuacao[BATERIA] += somar_risco_bateria(dados_missao[i][BATERIA])
    lista_soma_pontuacao[OXIGENIO] += somar_risco_oxigenio(dados_missao[i][OXIGENIO])
    lista_soma_pontuacao[ESTABILIDADE] += somar_risco_estabilidade(dados_missao[i][ESTABILIDADE])

def somar_risco_ciclo():
    soma_risco = 0
    for risco in lista_risco:
        soma_risco += risco
    return soma_risco

def analisar_tendencia():
    risco_primeiro_ciclo = lista_soma_risco_ciclo[0]
    risco_ultimo_ciclo = lista_soma_risco_ciclo[len(lista_soma_risco_ciclo) - 1]
    if risco_ultimo_ciclo > risco_primeiro_ciclo:
        return "A missão apresentou tendência de piora."
    elif risco_primeiro_ciclo > risco_ultimo_ciclo:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."

def calcular_classificacao_final_missao():
    soma_risco_ultimo_ciclo = somar_risco_ciclo()
    if soma_risco_ultimo_ciclo < 3:
        return "MISSÃO ESTÁVEL"
    elif soma_risco_ultimo_ciclo < 6:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"

def calcular_area_mais_afetada():
    mais_afetada = lista_soma_pontuacao[0]
    area_mais_afetada = areas_monitoradas[0]
    for ls, area in zip(lista_soma_pontuacao, areas_monitoradas):
        if ls > mais_afetada:
            mais_afetada = ls
            area_mais_afetada = area
    return area_mais_afetada

def calcular_media_informacao(coluna):
    soma = 0
    for i in range(len(dados_missao)):
        soma += dados_missao[i][coluna]
    return soma / len(dados_missao)

def exibir_ciclo_critico():
    ciclo_critico = 0
    maior_risco = lista_soma_risco_ciclo[0]
    for i in range(1, len(lista_soma_risco_ciclo)):
        if lista_soma_risco_ciclo[i] > maior_risco:
            maior_risco = lista_soma_risco_ciclo[i]
            ciclo_critico = i
    return ciclo_critico + 1

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

def classificar_ciclo(soma_risco):   
    match soma_risco:
        case _ if soma_risco < 3:
            return "MISSÃO ESTÁVEL"
        case _ if soma_risco < 6:
            return "MISSÃO EM ATENÇÃO"
        case _:
            return "MISSÃO CRÍTICA"
    
def possui_risco(i):
    return somar_risco_temperatura(dados_missao[i][TEMPERATURA]) or somar_risco_comunicacao(dados_missao[i][COMUNICACAO]) or somar_risco_bateria(dados_missao[i][BATERIA]) or somar_risco_oxigenio(dados_missao[i][OXIGENIO]) or somar_risco_estabilidade(dados_missao[i][ESTABILIDADE])
        
def gerar_recomendacao_ciclo(i):
    recomendacao = ""
    if possui_risco(i):
        if somar_risco_temperatura(dados_missao[i][TEMPERATURA]) > 0:
            recomendacao += "Verificar controle térmico da missão. "
        if somar_risco_comunicacao(dados_missao[i][COMUNICACAO]) > 0:
            recomendacao += "Tentar reestabelecer contato com a base. "
        if somar_risco_bateria(dados_missao[i][BATERIA]) > 0:
            recomendacao += "Ativar modo de economia de energia. "
        if somar_risco_oxigenio(dados_missao[i][OXIGENIO]) > 0:
            recomendacao += "Acionar protocolo de suporte à vida. "
        if somar_risco_estabilidade(dados_missao[i][ESTABILIDADE]) > 0:
            recomendacao += "Reduzir operações não essenciais. "
    else:
        recomendacao = "Manter operação normal e continuar monitoramento."
    return recomendacao

def eh_temperatura_elevada(temperatura):
    return temperatura < 18 or temperatura > 30 and temperatura <= 35

def eh_temperatura_critica(temperatura):
    return temperatura > 35

def eh_comunicacao_critica(comunicacao):
    return comunicacao < 30

def eh_comunicacao_instavel(comunicacao):
    return comunicacao <= 59

def eh_bateria_critica(bateria):
    return bateria < 20

def eh_bateria_abaixo_recomendavel(bateria):
    return bateria <= 49

def eh_oxigenio_critico(oxigenio):
    return oxigenio < 80

def eh_oxigenio_abaixo_recomendavel(oxigenio):
    return oxigenio <= 89

def eh_estabilidade_critica(estabilidade):
    return estabilidade < 40

def eh_estabilidade_reduzida(estabilidade):
    return estabilidade <= 69

def analisar_temperatura(temperatura):
    match temperatura:
        case _ if eh_temperatura_elevada(temperatura):
            return "ATENÇÃO | Temperatura elevada"
        case _ if eh_temperatura_critica(temperatura):
            return "CRÍTICO | Risco de superaquecimento"
        case _:
            return "NORMAL | Temperatura estável"

def analisar_comunicacao(comunicacao):
    match comunicacao:
        case _ if eh_comunicacao_critica(comunicacao):
            return "CRÍTICO | Comunicação com a base em nível crítico"
        case _ if eh_comunicacao_instavel(comunicacao):
            return "ATENÇÃO | Comunicação instável"
        case _:
            return "NORMAL | Comunicação estável"
        
def analisar_bateria(bateria):
    match bateria:
        case _ if eh_bateria_critica(bateria):
            return "CRÍTICO | Bateria em nível crítico"
        case _ if eh_bateria_abaixo_recomendavel(bateria):
            return "ATENÇÃO | Bateria abaixo do recomendável"
        case _:
            return "NORMAL | Energia estável"
        
def analisar_oxigenio(oxigenio):
    match oxigenio:
        case _ if eh_oxigenio_critico(oxigenio):
            return "CRÍTICO | Oxigênio em nível crítico"
        case _ if eh_oxigenio_abaixo_recomendavel(oxigenio):
            return "ATENÇÃO | Oxigênio abaixo do ideal"
        case _:
            return "NORMAL | Oxigênio adequado"
        
def analisar_estabilidade(estabilidade):
    match estabilidade:
        case _ if eh_estabilidade_critica(estabilidade):
            return "CRÍTICO | Estabilidade operacional crítica"
        case _ if eh_estabilidade_reduzida(estabilidade):
            return "ATENÇÃO | Estabilidade operacional reduzida"
        case _:
            return "NORMAL | Estabilidade operacional adequada"

def somar_risco_temperatura(temperatura):
    risco = 0
    match temperatura:
        case _ if eh_temperatura_elevada(temperatura):
            risco += 1
        case _ if eh_temperatura_critica(temperatura):
            risco += 2
        case _:
            risco += 0
    return risco

def somar_risco_comunicacao(comunicacao):
    risco = 0
    match comunicacao:
        case _ if eh_comunicacao_critica(comunicacao):
            risco += 2
        case _ if eh_comunicacao_instavel(comunicacao):
            risco += 1
    return risco

def somar_risco_bateria(bateria):
    risco = 0
    match bateria:
        case _ if eh_bateria_critica(bateria):
            risco += 2
        case _ if eh_bateria_abaixo_recomendavel(bateria):
            risco += 1
    return risco

def somar_risco_oxigenio(oxigenio):
    risco = 0
    match oxigenio:
        case _ if eh_oxigenio_critico(oxigenio):
            risco += 2
        case _ if eh_oxigenio_abaixo_recomendavel(oxigenio):
            risco += 1
    return risco

def somar_risco_estabilidade(estabilidade):
    risco = 0
    match estabilidade:
        case _ if eh_estabilidade_critica(estabilidade):
            risco += 2
        case _ if eh_estabilidade_reduzida(estabilidade):
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