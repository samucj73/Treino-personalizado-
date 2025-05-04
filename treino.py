# treino.py
import random
from exercicios import exercicios

def gerar_treino_personalizado(grupo_muscular, nivel_experiencia, dias_treino):
    treino = []
    # Verificar se o grupo muscular e nível de experiência existem
    if grupo_muscular not in exercicios:
        raise ValueError(f"Grupo muscular '{grupo_muscular}' não encontrado.")
    if nivel_experiencia not in exercicios[grupo_muscular]:
        raise ValueError(f"Nível de experiência '{nivel_experiencia}' não encontrado para o grupo muscular '{grupo_muscular}'.")

    # Obter os exercícios disponíveis para o grupo muscular e nível de experiência
    exercicios_disponiveis = exercicios[grupo_muscular][nivel_experiencia]
    
    # Selecionar um número de exercícios baseado nos dias de treino
    num_exercicios = len(exercicios_disponiveis)
    
    # Se houver menos exercícios do que dias de treino, repetir exercícios
    treino_por_dia = random.sample(exercicios_disponiveis, min(dias_treino, num_exercicios))

    for exercicio, series, repeticoes, equipamento in treino_por_dia:
        treino.append({
            'exercicio': exercicio,
            'series': series,
            'repeticoes': repeticoes,
            'equipamento': equipamento
        })

    return treino

def exibir_treino(treino):
    for i, exercicio in enumerate(treino):
        print(f"{i + 1}. {exercicio['exercicio']}")
        print(f"   Séries: {exercicio['series']} | Repetições: {exercicio['repeticoes']} | Equipamento: {exercicio['equipamento']}")
        print("-" * 30)

# Exemplo de uso
grupo_muscular = "peito"
nivel_experiencia = "Iniciante"
dias_treino = 3

treino = gerar_treino_personalizado(grupo_muscular, nivel_experiencia, dias_treino)
exibir_treino(treino)
