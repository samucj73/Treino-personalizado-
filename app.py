import streamlit as st
from usuario import cadastrar, obter, atualizar
from treino import gerar_treino

st.set_page_config(page_title="Personal Trainer App", page_icon=":muscle:", layout="centered")

def cadastro():
    st.subheader("Cadastro de Novo Usuário")
    with st.form("cadastro_form"):
        nome = st.text_input("Nome de usuário")
        senha = st.text_input("Senha", type="password")
        idade = st.number_input("Idade", min_value=10, max_value=100, step=1)
        peso = st.number_input("Peso (kg)", min_value=30.0, max_value=300.0, step=0.1)
        altura = st.number_input("Altura (m)", min_value=1.0, max_value=2.5, step=0.01)
        genero = st.radio("Gênero", ("Masculino", "Feminino"))
        objetivo = st.selectbox("Objetivo", ["Perda de peso", "Ganhar massa muscular", "Melhorar resistência"])
        experiencia = st.selectbox("Nível de experiência", ["Iniciante", "Intermediário", "Avançado"])
        dias_treino = st.slider("Dias de treino na semana", 1, 7, 3)

        submitted = st.form_submit_button("Cadastrar")
        if submitted:
            try:
                cadastrar(nome, senha, idade, peso, altura, genero, objetivo, experiencia, dias_treino)
                st.success("Usuário cadastrado com sucesso!")
                st.balloons()
            except Exception as e:
                st.error(str(e))

def login():
    st.subheader("Login")
    with st.form("login_form"):
        nome = st.text_input("Nome de usuário")
        senha = st.text_input("Senha", type="password")
        submitted = st.form_submit_button("Entrar")

        if submitted:
            usuario = obter(nome, senha)
            if usuario:
                st.session_state['usuario'] = usuario
                st.toast(f"Bem-vindo(a), {usuario[1]}!", icon="🎉")
                st.experimental_rerun()
            else:
                st.error("Nome de usuário ou senha incorretos.")

def exibir_treino():
    usuario = st.session_state['usuario']

    st.title(f"Treino de {usuario[1]}")

    tabs = st.tabs(["📋 Perfil", "🏋️ Treino", "⚙️ Configurações"])

    with tabs[0]:  # Perfil
        st.subheader("Informações do Usuário")
        st.write(f"**Idade:** {usuario[3]} anos")
        st.write(f"**Peso:** {usuario[4]} kg")
        st.write(f"**Altura:** {usuario[5]} m")
        st.write(f"**Gênero:** {usuario[6]}")
        st.write(f"**Objetivo:** {usuario[7]}")
        st.write(f"**Experiência:** {usuario[8]}")
        st.write(f"**Dias de treino por semana:** {usuario[9]}")

    with tabs[1]:  # Treino
        st.subheader("Plano de Treino")
        treino = gerar_treino(usuario[7], usuario[8], usuario[9])

        progress = st.progress(0)
        for i in range(100):
            progress.progress(i + 1)
        st.success("Treino carregado!")

        for dia, exercicios in treino.items():
            with st.expander(dia):
                for exercicio in exercicios:
                    st.write(f"- {exercicio}")

    with tabs[2]:  # Configurações
        st.subheader("Atualizar Dados")
        with st.form("form_atualizar"):
            nome = st.text_input("Nome", value=usuario[1])
            idade = st.number_input("Idade", min_value=10, max_value=100, value=usuario[3], step=1)
            peso = st.number_input("Peso (kg)", min_value=30.0, max_value=300.0, value=usuario[4], step=0.1)
            altura = st.number_input("Altura (m)", min_value=1.0, max_value=2.5, value=usuario[5], step=0.01)
            genero = st.radio("Gênero", ("Masculino", "Feminino"), index=0 if usuario[6] == "Masculino" else 1)
            objetivo = st.selectbox("Objetivo", ["Perda de peso", "Ganhar massa muscular", "Melhorar resistência"], index=["Perda de peso", "Ganhar massa muscular", "Melhorar resistência"].index(usuario[7]))
            experiencia = st.selectbox("Experiência", ["Iniciante", "Intermediário", "Avançado"], index=["Iniciante", "Intermediário", "Avançado"].index(usuario[8]))
            dias_treino = st.slider("Dias de treino por semana", 1, 7, value=usuario[9])

            if st.form_submit_button("Salvar"):
                atualizar(usuario[0], nome, idade, peso, altura, genero, objetivo, experiencia, dias_treino)
                st.success("Dados atualizados! Atualize a página para ver as mudanças.")
                st.experimental_rerun()

        if st.button("Sair da Conta"):
            del st.session_state['usuario']
            st.success("Sessão encerrada!")
            st.experimental_rerun()

def preencher_dados_usuario():
    st.title("Complete seu Perfil")
    usuario = st.session_state['usuario']

    with st.form("form_completar_perfil"):
        idade = st.number_input("Idade", min_value=10, max_value=100, step=1)
        peso = st.number_input("Peso (kg)", min_value=30.0, max_value=300.0, step=0.1)
        altura = st.number_input("Altura (m)", min_value=1.0, max_value=2.5, step=0.01)
        genero = st.radio("Gênero", ("Masculino", "Feminino"))
        objetivo = st.selectbox("Objetivo", ["Perda de peso", "Ganhar massa muscular", "Melhorar resistência"])
        experiencia = st.selectbox("Nível de experiência", ["Iniciante", "Intermediário", "Avançado"])
        dias_treino = st.slider("Dias disponíveis para treino na semana", 1, 7, 3)

        if st.form_submit_button("Salvar"):
            atualizar(usuario[0], usuario[1], idade, peso, altura, genero, objetivo, experiencia, dias_treino)
            st.success("Perfil atualizado!")
            st.experimental_rerun()

def main():
    criar_tabela_no_inicio()

    if 'usuario' not in st.session_state:
        menu = st.sidebar.radio("Menu", ["Login", "Cadastro"])

        if menu == "Login":
            login()
        else:
            cadastro()
    else:
        usuario = st.session_state['usuario']

        if usuario[3] is None or usuario[3] == 0:
            preencher_dados_usuario()
        else:
            exibir_treino()

def criar_tabela_no_inicio():
    from db import criar_tabela
    try:
        criar_tabela()
    except Exception as e:
        st.error(f"Erro ao criar a tabela: {e}")

if __name__ == "__main__":
    main()
