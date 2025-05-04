import random
from exercicios import exercicios

def gerar_treino_personalizado(objetivo, experiencia, dias_treino):
    treino_final = {}

    grupos = list(exercicios.keys())
    num_grupos = len(grupos)
    grupos_selecionados = grupos[:]

    for i in range(dias_treino):
        grupo = grupos_selecionados[i % num_grupos]
        nivel = experiencia

        if nivel not in exercicios[grupo]:
            continue

        lista_exercicios = exercicios[grupo][nivel]
        num_exercicios = min(3, len(lista_exercicios))
        selecionados = random.sample(lista_exercicios, num_exercicios)

        treino_final[f"Dia {i+1} - {grupo.title()}"] = []
        for nome, series, repeticoes, equipamento in selecionados:
            treino_final[f"Dia {i+1} - {grupo.title()}"].append({
                "nome": nome,
                "series": series,
                "repeticoes": repeticoes,
                "equipamento": equipamento
            })

    return treino_final

def exibir_treino(treino):
    for dia, exercicios_dia in treino.items():
        print(f"\n{dia}")
        for ex in exercicios_dia:
            print(f"- {ex['nome']} | Séries: {ex['series']} | Repetições: {ex['repeticoes']} | Equipamento: {ex['equipamento']}")
