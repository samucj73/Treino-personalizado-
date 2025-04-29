import streamlit as st
st.set_page_config(page_title="Personal Trainer App", page_icon=":muscle:", layout="centered")
from usuario import cadastrar, obter, atualizar, recuperar_por_email
from treino import gerar_treino
from calculos import (
    calcular_imc,
    calcular_tmb,
    calcular_percentual_gordura,
    calcular_massa_muscular,
    calcular_idade_metabolica,
    recomendacao_hidratacao,
    recomendacao_proteina
)

def cadastro():
    st.subheader("Cadastro de Novo Usuário")
    with st.form("cadastro_form"):
        nome = st.text_input("Nome de usuário")
        email = st.text_input("E-mail")
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
                cadastrar(nome, email, senha, idade, peso, altura, genero, objetivo, experiencia, dias_treino)
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
                st.rerun()
            else:
                st.error("Nome de usuário ou senha incorretos.")

    if st.button("Esqueceu a senha?"):
        recuperar_senha_form()

def recuperar_senha_form():
    st.subheader("Recuperação de Senha")
    email = st.text_input("Digite seu e-mail cadastrado", type="email")
    
    if st.button("Recuperar Senha"):
        if email:
            try:
                mensagem = recuperar_credencial(email)
                st.success(mensagem)
            except Exception as e:
                st.error(f"Erro ao tentar recuperar a senha: {e}")
        else:
            st.error("Por favor, insira um e-mail válido.")

def exibir_treino():
    if 'usuario' not in st.session_state:
        st.error("Usuário não encontrado na sessão. Faça login novamente.")
        st.stop()

    usuario = st.session_state['usuario']
    
    if usuario is None or len(usuario) < 10:
        st.error("Dados do usuário estão incompletos. Faça login novamente.")
        st.stop()

    st.title(f"Treino de {usuario[1]}")

    tabs = st.tabs(["📋 Perfil", "🏋️ Treino", "⚙️ Configurações", "📊 Análises Corporais"])

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
                st.rerun()

        if st.button("Sair da Conta"):
            del st.session_state['usuario']
            st.success("Sessão encerrada!")
            st.rerun()

    with tabs[3]:  # Análises Corporais
        st.subheader("Relatório Corporal")

        peso = usuario[4]
        altura = usuario[5]
        idade = usuario[3]
        genero = usuario[6]
        objetivo = usuario[7]

        imc, faixa_imc = calcular_imc(peso, altura)
        tmb = calcular_tmb(idade, peso, altura, genero)

        circunferencia = st.number_input("Informe sua circunferência da cintura (cm)", min_value=30.0, max_value=200.0, step=0.1)

        if circunferencia:
            gordura = calcular_percentual_gordura(peso, circunferencia, idade, genero)
            massa_magra = calcular_massa_muscular(peso, gordura)
            idade_metabolica = calcular_idade_metabolica(tmb, idade)
            agua = recomendacao_hidratacao(peso)
            proteina = recomendacao_proteina(peso, objetivo)

            st.markdown(f"**IMC:** {imc:.2f} ({faixa_imc})")
            st.markdown(f"**TMB (Taxa Metabólica Basal):** {tmb:.2f} kcal/dia")
            st.markdown(f"**Percentual de Gordura Estimado:** {gordura:.2f}%")
            st.markdown(f"**Massa Muscular Estimada:** {massa_magra:.2f} kg")
            st.markdown(f"**Idade Metabólica Estimada:** {idade_metabolica:.0f} anos")
            st.markdown(f"**Hidratação Recomendada:** {agua:.0f} ml por dia")
            st.markdown(f"**Proteína Diária Recomendada:** {proteina:.2f} g")
        else:
            st.info("Informe a circunferência da cintura para visualizar as análises completas.")

def preencher_dados_usuario():
    st.title("Complete seu Perfil")

    if 'usuario' not in st.session_state:
        st.error("Sessão expirada. Faça login novamente.")
        st.stop()

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
            st.rerun()

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

        if len(usuario) > 3 and (usuario[3] is None or usuario[3] == 0):
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
