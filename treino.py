import streamlit as st
import time

# Função para gerar treino
def gerar_treino(usuario):
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

    treino = f"## Dados Físicos\n"
    treino += f"- **Idade:** {idade} anos\n"
    treino += f"- **Peso:** {peso:.1f} kg\n"
    treino += f"- **Altura:** {altura:.2f} m\n"
    treino += f"- **Gênero:** {genero.capitalize()}\n"
    treino += f"- **Objetivo:** {objetivo.capitalize()}\n"
    treino += f"- **Experiência:** {experiencia.capitalize()}\n"
    treino += "---\n\n"

    treino += "## Treino Semanal\n"

    treino += """
### Segunda-feira (Peito e Tríceps)
"""
    progresso = 0  # Inicializa o progresso
    total_exercicios = 6  # Total de exercícios para o dia

    for i, exercicio in enumerate([
        ("Supino reto barra", "Banco + Barra"),
        ("Supino inclinado halteres", "Banco + Halteres"),
        ("Crucifixo reto", "Banco + Halteres"),
        ("Crossover no cabo", "Cross Over"),
        ("Tríceps testa", "Barra W"),
        ("Tríceps corda", "Polia")
    ]):
        if st.checkbox(f"Realizado: {exercicio[0]} ({exercicio[1]})", key=f"exercicio_{i}_segunda"):
            # Código para marcar como realizado (se necessário)
            progresso += 1
            st.progress(progresso / total_exercicios)  # Atualiza a barra de progresso
            time.sleep(1)  # Simula o tempo de descanso entre os exercícios
            # Tempo de descanso
            if st.button(f"Iniciar descanso entre {exercicio[0]}"):
                for t in range(10, 0, -1):
                    st.write(f"Descanso: {t} segundos")
                    time.sleep(1)

    treino += """
### Terça-feira (Costas e Bíceps)
"""
    progresso = 0  # Reinicia o progresso
    total_exercicios = 6  # Total de exercícios para o dia

    for i, exercicio in enumerate([
        ("Puxada frente aberta", "Cross Over"),
        ("Remada baixa", "Máquina Remada"),
        ("Puxada frente neutra", "Cross Over"),
        ("Remada unilateral", "Halteres"),
        ("Rosca direta barra", "Barra Reta"),
        ("Rosca alternada halteres", "Halteres")
    ]):
        if st.checkbox(f"Realizado: {exercicio[0]} ({exercicio[1]})", key=f"exercicio_{i}_terca"):
            # Código para marcar como realizado (se necessário)
            progresso += 1
            st.progress(progresso / total_exercicios)  # Atualiza a barra de progresso
            time.sleep(1)  # Simula o tempo de descanso entre os exercícios
            # Tempo de descanso
            if st.button(f"Iniciar descanso entre {exercicio[0]}"):
                for t in range(10, 0, -1):
                    st.write(f"Descanso: {t} segundos")
                    time.sleep(1)

    treino += """
### Quarta-feira (Pernas e Abdômen)
"""
    progresso = 0  # Reinicia o progresso
    total_exercicios = 6  # Total de exercícios para o dia

    for i, exercicio in enumerate([
        ("Agachamento livre", "Barra"),
        ("Leg press 45º", "Leg Press"),
        ("Cadeira extensora", "Máquina"),
        ("Mesa flexora", "Máquina"),
        ("Stiff com halteres", "Halteres"),
        ("Glúteo cabo", "Polia (principalmente para feminino)")
    ]):
        if st.checkbox(f"Realizado: {exercicio[0]} ({exercicio[1]})", key=f"exercicio_{i}_quarta"):
            # Código para marcar como realizado (se necessário)
            progresso += 1
            st.progress(progresso / total_exercicios)  # Atualiza a barra de progresso
            time.sleep(1)  # Simula o tempo de descanso entre os exercícios
            # Tempo de descanso
            if st.button(f"Iniciar descanso entre {exercicio[0]}"):
                for t in range(10, 0, -1):
                    st.write(f"Descanso: {t} segundos")
                    time.sleep(1)

    treino += """
### Quinta-feira (Ombros e Trapézio)
"""
    progresso = 0  # Reinicia o progresso
    total_exercicios = 6  # Total de exercícios para o dia

    for i, exercicio in enumerate([
        ("Desenvolvimento militar", "Barra ou Halteres"),
        ("Elevação lateral", "Halteres"),
        ("Elevação frontal", "Halteres"),
        ("Encolhimento de ombros", "Barra"),
        ("Desenvolvimento Arnold", "Halteres"),
        ("Crucifixo inverso máquina", "Máquina de deltoide posterior")
    ]):
        if st.checkbox(f"Realizado: {exercicio[0]} ({exercicio[1]})", key=f"exercicio_{i}_quinta"):
            # Código para marcar como realizado (se necessário)
            progresso += 1
            st.progress(progresso / total_exercicios)  # Atualiza a barra de progresso
            time.sleep(1)  # Simula o tempo de descanso entre os exercícios
            # Tempo de descanso
            if st.button(f"Iniciar descanso entre {exercicio[0]}"):
                for t in range(10, 0, -1):
                    st.write(f"Descanso: {t} segundos")
                    time.sleep(1)

    treino += """
### Sexta-feira (Glúteos e Abdômen)
"""
    if genero == "feminino":
        for i, exercicio in enumerate([
            ("Agachamento sumô com halteres", "Halteres"),
            ("Elevação de quadril no banco", "Banco + Peso"),
            ("Afundo com halteres", "Halteres"),
            ("Abdução de quadril máquina", "Máquina"),
            ("Ponte de glúteo solo", "Peso corporal"),
            ("Extensão de quadril no cabo", "Polia")
        ]):
            if st.checkbox(f"Realizado: {exercicio[0]} ({exercicio[1]})", key=f"exercicio_{i}_sexta_feminino"):
                # Código para marcar como realizado (se necessário)
                progresso += 1
                st.progress(progresso / total_exercicios)  # Atualiza a barra de progresso
                time.sleep(1)  # Simula o tempo de descanso entre os exercícios
                # Tempo de descanso
                if st.button(f"Iniciar descanso entre {exercicio[0]}"):
                    for t in range(10, 0, -1):
                        st.write(f"Descanso: {t} segundos")
                        time.sleep(1)

    else:
        for i, exercicio in enumerate([
            ("Agachamento frontal barra", "Barra"),
            ("Agachamento búlgaro halteres", "Halteres"),
            ("Leg press 45º", "Leg Press"),
            ("Extensão de quadril cabo", "Polia"),
            ("Cadeira abdutora", "Máquina"),
            ("Elevação de quadril solo", "Peso corporal")
        ]):
            if st.checkbox(f"Realizado: {exercicio[0]} ({exercicio[1]})", key=f"exercicio_{i}_sexta_masculino"):
                # Código para marcar como realizado (se necessário)
                progresso += 1
                st.progress(progresso / total_exercicios)  # Atualiza a barra de progresso
                time.sleep(1)  # Simula o tempo de descanso entre os exercícios
                # Tempo de descanso
                if st.button(f"Iniciar descanso entre {exercicio[0]}"):
                    for t in range(10, 0, -1):
                        st.write(f"Descanso: {t} segundos")
                        time.sleep(1)

    treino += "---\n"
    treino += "Lembre-se sempre de realizar os exercícios com a forma correta e progredir de maneira segura! Em caso de dúvidas, consulte um profissional de saúde ou treinador!"

    return treino
