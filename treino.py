# Função para gerar treino personalizado
def gerar_treino(usuario):
    idade = usuario[3]
    peso = usuario[4]
    objetivo = usuario[7]
    experiencia = usuario[8]

    treino = ""

    if experiencia == "iniciante":
        treino += "### Treino Iniciante\n"
        treino += "- Agachamento (3x10)\n"
        treino += "- Flexão de braço (3x10)\n"
        treino += "- Remada unilateral (3x12 por lado)\n"
    elif experiencia == "intermediário":
        treino += "### Treino Intermediário\n"
        treino += "- Agachamento com barra (4x8)\n"
        treino += "- Supino reto (4x8)\n"
        treino += "- Levantamento terra (4x8)\n"
    elif experiencia == "avançado":
        treino += "### Treino Avançado\n"
        treino += "- Agachamento pesado (5x6)\n"
        treino += "- Supino pesado (5x6)\n"
        treino += "- Deadlift (5x6)\n"

    treino += "\n---\n"
    treino += f"**Idade:** {idade} anos\n\n"
    treino += f"**Peso:** {peso:.1f} kg\n\n"
    treino += f"**Objetivo:** {objetivo}\n\n"

    return treino
