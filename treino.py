import random
from exercicios import exercicios_por_grupo

def gerar_treino_personalizado(objetivo, experiencia, dias_treino, grupos_musculares):
    treino = {}
    total_dias = dias_treino
    grupos_selecionados = grupos_musculares

    # Distribuir os grupos musculares selecionados pelos dias de treino
    distribuicao = distribuir_grupos(grupos_selecionados, total_dias)

    for i, grupos_do_dia in enumerate(distribuicao, 1):
        dia = f"Dia {i}"
        treino[dia] = []

        for grupo in grupos_do_dia:
            exercicios = exercicios_por_grupo.get(grupo, [])

            # Seleção de exercícios com base no nível de experiência
            if experiencia == "Iniciante":
                selecionados = exercicios[:4]
            elif experiencia == "Intermediário":
                selecionados = exercicios[:6]
            else:  # Avançado
                selecionados = exercicios

            # Embaralha e seleciona alguns exercícios
            random.shuffle(selecionados)
            quantidade = min(3, len(selecionados)) if experiencia == "Iniciante" else min(5, len(selecionados))
            treino[dia].extend(selecionados[:quantidade])

    return treino

def distribuir_grupos(grupos, dias):
    """Distribui os grupos musculares selecionados ao longo dos dias de treino."""
    distribuicao = [[] for _ in range(dias)]
    for i, grupo in enumerate(grupos):
        dia = i % dias
        distribuicao[dia].append(grupo)
    return distribuicao
