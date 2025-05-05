from exercicios import EXERCICIOS_POR_GRUPO
import random

def gerar_treino_personalizado(objetivo, experiencia, dias_treino):
    grupos_musculares = list(EXERCICIOS_POR_GRUPO.keys())
    treino = {}

    grupos_selecionados = random.sample(grupos_musculares, k=min(dias_treino, len(grupos_musculares)))

    for i, grupo in enumerate(grupos_selecionados):
        dia = f"Dia {i+1} - {grupo}"
        treino[dia] = []

        exercicios_grupo = EXERCICIOS_POR_GRUPO.get(grupo, [])
        exercicios_filtrados = [ex for ex in exercicios_grupo if ex["nivel"] in niveis_aceitos(experiencia)]

        if experiencia == "Iniciante":
            exercicios_dia = random.sample(exercicios_filtrados, min(4, len(exercicios_filtrados)))
        elif experiencia == "Intermediário":
            exercicios_dia = random.sample(exercicios_filtrados, min(6, len(exercicios_filtrados)))
        else:
            exercicios_dia = random.sample(exercicios_filtrados, min(8, len(exercicios_filtrados)))

        treino[dia] = [
            {
                "nome": ex["nome"],
                "series": ex["series"],
                "repeticoes": ex["repeticoes"],
                "equipamento": ex["equipamento"]
            }
            for ex in exercicios_dia
        ]

    return treino

def niveis_aceitos(nivel):
    if nivel == "Iniciante":
        return ["Iniciante"]
    elif nivel == "Intermediário":
        return ["Iniciante", "Intermediário"]
    else:
        return ["Iniciante", "Intermediário", "Avançado"]
