import streamlit as st
st.set_page_config(page_title="Personal Trainer App", page_icon=":muscle:", layout="centered")

from usuario import cadastrar, obter, atualizar, recuperar_senha
from treino import gerar_treino_personalizado
from exercicios import exercicios_por_grupo
from calculos import (
    calcular_imc,
    calcular_tmb,
    calcular_percentual_gordura,
    calcular_massa_muscular,
    calcular_idade_metabolica,
    recomendacao_hidratacao,
    recomendacao_proteina
)

def splash_screen():
    st.markdown("<h1 style='text-align: center;'>Personal Trainer App</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Seu treino, suas metas, sua evolução!</p>", unsafe_allow_html=True)
    st.markdown("---")

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

        submitted = st.form_submit_button("Cadastrar")
        if submitted:
            try:
                cadastrar(nome, email, senha, idade, peso, altura, genero, "", "", 0)
                st.success("Usuário cadastrado com sucesso!")
                st.balloons()
                st.session_state['mostrar_cadastro'] = False  # Voltar para a tela de login
                st.rerun()
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
                st.toast(f"Bem-vindo(a), {usuario['nome']}!", icon="🎉")
                st.rerun()
            else:
                st.error("Nome de usuário ou senha incorretos.")

    if st.button("Esqueceu a senha?"):
        recuperar_senha_form()

    if st.button("Cadastrar novo usuário"):
        st.session_state['mostrar_cadastro'] = True
        st.rerun()

def recuperar_senha_form():
    st.subheader("Recuperação de Senha")
    email = st.text_input("Digite seu e-mail cadastrado")
    
    if st.button("Recuperar Senha"):
        if email:
            try:
                mensagem = recuperar_senha(email)
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

    st.title(f"Treino de {usuario['nome']}")

    tabs = st.tabs(["📋 Perfil", "🏋️ Treino", "⚙️ Configurações", "📊 Análises Corporais"])

    with tabs[0]:
        st.subheader("Informações do Usuário")
        st.write(f"**Idade:** {usuario['idade']} anos")
        st.write(f"**Peso:** {usuario['peso']} kg")
        st.write(f"**Altura:** {usuario['altura']} m")
        st.write(f"**Gênero:** {usuario['genero']}")

    with tabs[1]:
        st.subheader("Gerar Plano de Treino Personalizado")

        objetivo = st.selectbox("Selecione seu objetivo", ["Perda de peso", "Ganhar massa muscular", "Melhorar resistência"])
        experiencia = st.selectbox("Selecione seu nível de experiência", ["Iniciante", "Intermediário", "Avançado"])
        dias_treino = st.slider("Quantos dias por semana você pode treinar?", 1, 7, 3)
        grupos_musculares = list(exercicios_por_grupo.keys())
        grupos_selecionados = st.multiselect("Selecione os grupos musculares que deseja treinar", grupos_musculares)

        if st.button("Gerar Treino"):
            if not grupos_selecionados:
                st.warning("Por favor, selecione ao menos um grupo muscular.")
            else:
                try:
                    treino = gerar_treino_personalizado(objetivo, experiencia, dias_treino, grupos_selecionados)
                    st.success("Treino gerado com sucesso!")

                    for dia, exercicios in treino.items():
                        with st.expander(dia):
                            for ex in exercicios:
                                st.markdown(f"**{ex['nome']}**")
                                st.write(f"- Séries: {ex['séries']}")
                                st.write(f"- Repetições: {ex['repetições']}")
                                st.write(f"- Equipamento: {ex['equipamento']}")
                except Exception as e:
                    st.error(f"Erro ao gerar treino: {e}")

    with tabs[2]:
        st.subheader("Atualizar Dados")
        with st.form("form_atualizar"):
            nome = st.text_input("Nome", value=usuario['nome'])
            idade = st.number_input("Idade", min_value=10, max_value=100, value=usuario['idade'], step=1)
            peso = st.number_input("Peso (kg)", min_value=30.0, max_value=300.0, value=usuario['peso'], step=0.1)
            altura = st.number_input("Altura (m)", min_value=1.0, max_value=2.5, value=usuario['altura'], step=0.01)
            genero = st.radio("Gênero", ("Masculino", "Feminino"), index=0 if usuario['genero'] == "Masculino" else 1)

            if st.form_submit_button("Salvar"):
                atualizar(usuario['id'], nome, idade, peso, altura, genero, "", "", 0)
                st.success("Dados atualizados!")
                st.rerun()

        if st.button("Sair da Conta"):
            del st.session_state['usuario']
            st.success("Sessão encerrada!")
            st.session_state['mostrar_cadastro'] = False  # Garantir que a tela de login seja exibida
            st.rerun()

    with tabs[3]:
        st.subheader("Relatório Corporal")

        peso = usuario['peso']
        altura = usuario['altura']
        idade = usuario['idade']
        genero = usuario['genero']
        objetivo = st.selectbox("Informe o objetivo para cálculo nutricional", ["Perda de peso", "Ganhar massa muscular", "Melhorar resistência"])

        with st.form("form_analise_corporal"):
            circunferencia = st.number_input("Informe sua circunferência da cintura (cm)", min_value=30.0, max_value=200.0, step=0.1)
            calcular = st.form_submit_button("Calcular Análises Corporais")

        if calcular:
            imc, faixa_imc = calcular_imc(peso, altura)
            tmb = calcular_tmb(idade, peso, altura, genero)
            gordura = calcular_percentual_gordura(peso, circunferencia, idade, genero)
            massa_magra = calcular_massa_muscular(peso, gordura)
            idade_metabolica = calcular_idade_metabolica(tmb, idade)
            agua = recomendacao_hidratacao(peso)
            proteina = recomendacao_proteina(peso, objetivo)
            gordura_recomendada = recomendacao_gordura(peso, objetivo)
            carboidrato = recomendacao_carboidrato(peso, objetivo)

            st.markdown(f"**IMC:** {imc:.2f} ({faixa_imc})")
            st.markdown(f"**TMB (Taxa Metabólica Basal):** {tmb:.2f} kcal/dia")
            st.markdown(f"**Percentual de Gordura Estimado:** {gordura:.2f}%")
            st.markdown(f"**Massa Muscular Estimada:** {massa_magra:.2f} kg")
            st.markdown(f"**Idade Metabólica Estimada:** {idade_metabolica:.0f} anos")
            st.markdown(f"**Hidratação Recomendada:** {agua:.0f} ml por dia")
            st.markdown(f"**Proteína Diária Recomendada:** {proteina:.2f} g")
            st.markdown(f"**Gordura Recomendada:** {gordura_recomendada:.2f} g/dia")
            st.markdown(f"**Carboidrato Recomendado:** {carboidrato:.2f} g/dia")

def rodape():
    st.markdown("""
        <hr style="margin-top: 50px; margin-bottom: 10px;">
        <div style="text-align: center; color: gray; font-size: 0.9em;">
            Desenvolvido por Samucj Technology © 2025
        </div>
    """, unsafe_allow_html=True)

# Execução principal
if __name__ == "__main__":
    splash_screen()  # Mostra o cabeçalho uma única vez

    if 'usuario' in st.session_state:
        exibir_treino()
    elif 'mostrar_cadastro' in st.session_state and st.session_state['mostrar_cadastro']:
        cadastro()
    else:
        login()

    rodape()
