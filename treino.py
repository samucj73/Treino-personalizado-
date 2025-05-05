import random
from exercicios import exercicios_por_grupo

def gerar_treino_personalizado(objetivo, experiencia, dias, grupos_musculares):
    treino = {}

    # Define o número de exercícios por grupo com base na experiência
    if experiencia == "Iniciante":
        num_exercicios = 3
    elif experiencia == "Intermediário":
        num_exercicios = 5
    else:  # Avançado
        num_exercicios = 7

    # Distribui os grupos musculares pelos dias
    grupos_por_dia = [[] for _ in range(dias)]
    for i, grupo in enumerate(grupos_musculares):
        grupos_por_dia[i % dias].append(grupo)

    for dia_idx, grupos in enumerate(grupos_por_dia, 1):
        exercicios_do_dia = []
        for grupo in grupos:
            todos_exercicios = exercicios_por_grupo.get(grupo, [])
            selecionados = random.sample(todos_exercicios, min(num_exercicios, len(todos_exercicios)))
            for ex in selecionados:
                exercicios_do_dia.append({
                    "grupo_muscular": grupo,
                    "nome": ex["nome"],
                    "séries": ex["séries"],
                    "repetições": ex["repetições"],
                    "equipamento": ex["equipamento"]
                })
        treino[f"Dia {dia_idx}"] = exercicios_do_dia

    return treino
