import random
from exercicios import exercicios_por_grupo

def gerar_treino_personalizado(objetivo, experiencia, dias_treino):
    grupos = list(exercicios_por_grupo.keys())
    treino = {}

    grupos_por_dia = dividir_grupos(grupos, dias_treino)

    for i in range(dias_treino):
        dia = f"Dia {i+1}"
        treino[dia] = []

        for grupo in grupos_por_dia[i]:
            exercicios = exercicios_por_grupo[grupo]
            qtd = definir_qtd_exercicios(experiencia)
            selecionados = random.sample(exercicios, min(qtd, len(exercicios)))

            for ex in selecionados:
                treino[dia].append({
                    "nome": ex["nome"],
                    "series": definir_series(objetivo),
                    "repeticoes": definir_repeticoes(objetivo),
                    "equipamento": ex["equipamento"]
                })

    return treino

def dividir_grupos(grupos, dias):
    random.shuffle(grupos)
    grupos_por_dia = [[] for _ in range(dias)]
    for i, grupo in enumerate(grupos):
        grupos_por_dia[i % dias].append(grupo)
    return grupos_por_dia

def definir_qtd_exercicios(experiencia):
    if experiencia == "Iniciante":
        return 4
    elif experiencia == "Intermediário":
        return 6
    else:  # Avançado
        return 8

def definir_series(objetivo):
    if objetivo == "Perda de peso":
        return 3
    elif objetivo == "Ganhar massa muscular":
        return 4
    else:  # Melhorar resistência
        return 2

def definir_repeticoes(objetivo):
    if objetivo == "Perda de peso":
        return 15
    elif objetivo == "Ganhar massa muscular":
        return 10
    else:  # Melhorar resistência
        return 20
