_treino(usuario):
    idade = usuario[3]
    peso = usuario[4]
    altura = usuario[5]
    genero = usuario[6].lower()
    objetivo = usuario[7].lower()
    experiencia = usuario[8].lower()

    # Definir séries e repetições
    if genero == "masculino":
        if experiencia == "iniciante":
            series = 3
            reps = "12-15"
        elif experiencia == "intermediário":
            series = 4
            reps = "8-12"
        else:  # avançado
            series = 5
            reps = "6-10"
    else:  # feminino
        if experiencia == "iniciante":
            series = 3
            reps = "15-20"
        elif experiencia == "intermediário":
            series = 4
            reps = "12-15"
        else:  # avançado
            series = 5
            reps = "8-12"

    # Início do treino
    treino = f"## Dados Físicos\n"
    treino += f"- **Idade:** {idade} anos\n"
    treino += f"- **Peso:** {peso:.1f} kg\n"
    treino += f"- **Altura:** {altura:.2f} m\n"
    treino += f"- **Gênero:** {genero.capitalize()}\n"
    treino += f"- **Objetivo:** {objetivo.capitalize()}\n"
    treino += f"- **Experiência:** {experiencia.capitalize()}\n"
    treino += "---\n\n"

    # Exibindo a estrutura do treino com base nos dias da semana
    treino += "## Treino Semanal\n"

    # Segunda-feira
    with st.expander("Segunda-feira (Peito e Tríceps)"):
        treino_segunda = [
            ("Supino reto barra", series, reps),
            ("Supino inclinado halteres", series, reps),
            ("Crucifixo reto", series, reps),
            ("Crossover no cabo", series, reps),
            ("Tríceps testa", series, reps),
            ("Tríceps corda", series, reps)
        ]
        st.write("### Exercícios:")
        st.table(treino_segunda)

    # Terça-feira
    with st.expander("Terça-feira (Costas e Bíceps)"):
        treino_terca = [
            ("Puxada frente aberta", series, reps),
            ("Remada baixa", series, reps),
            ("Puxada frente neutra", series, reps),
            ("Remada unilateral", series, reps),
            ("Rosca direta barra", series, reps),
            ("Rosca alternada halteres", series, reps)
        ]
        st.write("### Exercícios:")
        st.table(treino_terca)

    # Quarta-feira
    with st.expander("Quarta-feira (Pernas e Abdômen)"):
        treino_quarta = [
            ("Agachamento livre", series, reps),
            ("Leg press 45º", series, reps),
            ("Cadeira extensora", series, reps),
            ("Mesa flexora", series, reps),
            ("Stiff com halteres", series, reps),
            ("Glúteo cabo", series, reps),
            ("Abdominal supra solo", "3", "20"),
            ("Prancha isométrica", "3", "30s"),
            ("Abdominal oblíquo solo", "3", "20 cada lado")
        ]
        st.write("### Exercícios:")
        st.table(treino_quarta)

    # Quinta-feira
    with st.expander("Quinta-feira (Ombros e Trapézio)"):
        treino_quinta = [
            ("Desenvolvimento militar", series, reps),
            ("Elevação lateral", series, reps),
            ("Elevação frontal", series, reps),
            ("Encolhimento de ombros", series, reps),
            ("Desenvolvimento Arnold", series, reps),
            ("Crucifixo inverso máquina", series, reps)
        ]
        st.write("### Exercícios:")
        st.table(treino_quinta)

    # Sexta-feira
    with st.expander("Sexta-feira (Glúteos e Abdômen)"):
        if genero == "feminino":
            treino_sexta = [
                ("Agachamento sumô com halteres", series, reps),
                ("Elevação de quadril no banco", series, reps),
                ("Afundo com halteres", series, reps),
                ("Abdução de quadril máquina", series, reps),
                ("Ponte de glúteo solo", series, reps),
                ("Extensão de quadril no cabo", series, reps),
                ("Abdominal infra solo", "3", "20"),
                ("Prancha lateral", "3", "30s"),
                ("Abdominal bicicleta", "3", "20")
            ]
        else:
            treino_sexta = [
                ("Agachamento frontal barra", series, reps),
                ("Agachamento búlgaro halteres", series, reps),
                ("Leg press 45º", series, reps),
                ("Extensão de quadril cabo", series, reps),
                ("Cadeira abdutora", series, reps),
                ("Elevação de quadril solo", series, reps),
                ("Abdominal supra banco", "3", "20"),
                ("Prancha lateral", "3", "30s"),
                ("Abdominal infra no banco", "3", "20")
            ]
        st.write("### Exercícios:")
        st.table(treino_sexta)

    # Fim do treino
    treino += "---\n"
    treino += "Lembre-se sempre de realizar os exercícios com a forma correta e progredir de maneira segura! Em caso de dúvidas, consulte um profissional de saúde ou treinador!"

    return treino

# Exemplo de uso da função com os dados do usuário
usuario = [1, "Nome", "email@example.com", 30, 70, 1.75, "masculino", "hipertrofia", "intermediário"]
treino_gerado = gerar_treino(usuario)
st.write(treino_gerado)
