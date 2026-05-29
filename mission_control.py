def percorrer_ciclo_missao():
    for i in range(len(dados_missao)):
        print(f"Temperatura: {dados_missao[i][0]} °C")
        print(f"Comunicação: {dados_missao[i][1]}%")
        print(f"Bateria: {dados_missao[i][2]}%")
        print(f"Oxigênio: {dados_missao[i][3]}%")
        print(f"Estabilidade: {dados_missao[i][4]}%")
        print()

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

percorrer_ciclo_missao()