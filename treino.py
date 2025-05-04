# treino.py

import random
from exercicios import exercicios_por_grupo

def filtrar_exercicios_por_experiencia(lista, experiencia):
    if experiencia == "iniciante":
        return lista[:4]
    elif experiencia == "intermediário":
        return lista[:6]
    elif experiencia == "avançado":
        return lista
    else:
        return lista

def gerar_treino_personalizado(grupos_musculares, dias_treino, experiencia, objetivo):
    plano_treino = {}

    # Define número total de sessões com base em dias_treino
    num_dias = dias_treino
    grupos_selecionados = grupos_musculares if grupos_musculares else list(exercicios_por_grupo.keys())

    grupos_por_dia = max(1, len(grupos_selecionados) // num_dias)
    grupos_divididos = [grupos_selecionados[i:i + grupos_por_dia] for i in range(0, len(grupos_selecionados), grupos_por_dia)]

    for dia, grupos in enumerate(grupos_divididos, start=1):
        exercicios_dia = []
        for grupo in grupos:
            todos_exercicios = exercicios_por_grupo.get(grupo, [])
            selecionados = filtrar_exercicios_por_experiencia(todos_exercicios, experiencia)
            exercicios_dia.extend(random.sample(selecionados, min(len(selecionados), 2)))
        plano_treino[f"Dia {dia}"] = exercicios_dia

    return plano_treino
