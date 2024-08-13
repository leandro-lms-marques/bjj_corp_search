import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import openai

class PesquisaJiuJitsu:
    def __init__(self, logo_path):
        self.logo_path = logo_path
        self.semanal_perguntas = [
            {
                "pergunta": "Como você avalia a satisfação com a aula de Jiu-jitsu desta semana?",
                "opcoes": ["Muito satisfeito", "Satisfeito", "Neutro", "Insatisfeito", "Muito insatisfeito"]
            },
            {
                "pergunta": "A aula desta semana contribuiu para o seu sentimento de pertencimento à equipe?",
                "opcoes": ["Concordo totalmente", "Concordo", "Neutro", "Discordo", "Discordo totalmente"]
            },
            {
                "pergunta": "Você sente que a aula desta semana ajudou a melhorar sua resiliência?",
                "opcoes": ["Concordo totalmente", "Concordo", "Neutro", "Discordo", "Discordo totalmente"]
            },
            {
                "pergunta": "Como você avalia a união do time após a aula desta semana?",
                "opcoes": ["Muito melhor", "Melhor", "Igual", "Pior", "Muito pior"]
            },
            {
                "pergunta": "Você percebeu alguma mudança na sua produtividade nesta semana?",
                "opcoes": ["Aumentou significativamente", "Aumentou", "Permaneceu igual", "Diminuiu", "Diminuiu significativamente"]
            },
            {
                "pergunta": "Como você avalia seu nível de estresse após a aula desta semana?",
                "opcoes": ["Muito menor", "Menor", "Igual", "Maior", "Muito maior"]
            }
        ]

        self.final_perguntas = [
            {
                "pergunta": "Como você avalia sua satisfação geral com o programa de treinamento de Jiu-jitsu?",
                "opcoes": ["Muito satisfeito", "Satisfeito", "Neutro", "Insatisfeito", "Muito insatisfeito"]
            },
            {
                "pergunta": "O programa de treinamento de Jiu-jitsu contribuiu para o seu sentimento de pertencimento à equipe?",
                "opcoes": ["Concordo totalmente", "Concordo", "Neutro", "Discordo", "Discordo totalmente"]
            },
            {
                "pergunta": "Você sente que o treinamento de Jiu-jitsu ajudou a melhorar sua resiliência?",
                "opcoes": ["Concordo totalmente", "Concordo", "Neutro", "Discordo", "Discordo totalmente"]
            },
            {
                "pergunta": "Como você avalia a união do time após participar do treinamento de Jiu-jitsu?",
                "opcoes": ["Muito melhor", "Melhor", "Igual", "Pior", "Muito pior"]
            },
            {
                "pergunta": "Você sente que o treinamento de Jiu-jitsu promoveu a camaradagem entre os colegas?",
                "opcoes": ["Concordo totalmente", "Concordo", "Neutro", "Discordo", "Discordo totalmente"]
            },
            {
                "pergunta": "Você percebeu alguma mudança na sua produtividade após o início do treinamento de Jiu-jitsu?",
                "opcoes": ["Aumentou significativamente", "Aumentou", "Permaneceu igual", "Diminuiu", "Diminuiu significativamente"]
            },
            {
                "pergunta": "O treinamento de Jiu-jitsu ajudou a melhorar sua capacidade de concentração no trabalho?",
                "opcoes": ["Concordo totalmente", "Concordo", "Neutro", "Discordo", "Discordo totalmente"]
            },
            {
                "pergunta": "Você sente que o treinamento de Jiu-jitsu ajudou a melhorar sua gestão de tempo?",
                "opcoes": ["Concordo totalmente", "Concordo", "Neutro", "Discordo", "Discordo totalmente"]
            },
            {
                "pergunta": "Como você avalia seu nível de estresse após participar do treinamento de Jiu-jitsu?",
                "opcoes": ["Muito menor", "Menor", "Igual", "Maior", "Muito maior"]
            },
            {
                "pergunta": "O treinamento de Jiu-jitsu teve um impacto positivo na sua saúde mental?",
                "opcoes": ["Concordo totalmente", "Concordo", "Neutro", "Discordo", "Discordo totalmente"]
            },
            {
                "pergunta": "Você percebeu alguma melhoria na sua saúde física após o treinamento de Jiu-jitsu?",
                "opcoes": ["Concordo totalmente", "Concordo", "Neutro", "Discordo", "Discordo totalmente"]
            },
            {
                "pergunta": "Quais aspectos do programa de treinamento você acha que poderiam ser melhorados?",
                "opcoes": []
            }
        ]

    def gerar_relatorio(self, df):
        for pergunta in df.columns[3:]:  # Ignorar as colunas de Sexo, Idade e Função
            dados = df[pergunta].value_counts()
            plt.figure(figsize=(10, 5))
            dados.plot(kind='bar')
            plt.title(pergunta)
            plt.xlabel('Respostas')
            plt.ylabel('Frequência')

            # Adicionar logo da empresa
            logo = plt.imread(self.logo_path)
            imagebox = OffsetImage(logo, zoom=0.1)
            ab = AnnotationBbox(imagebox, (0.5, 0.5), frameon=False, xycoords='axes fraction', boxcoords="axes fraction", pad=0.1)
            plt.gca().add_artist(ab)

            st.pyplot(plt)

    def gerar_insights(self, df):
        st.subheader("Insights e Sugestões de Melhorias")
        resultados_texto = df.to_string()
        openai.api_key = st.secrets["openai_api_key"]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente que ajuda a analisar dados de pesquisa."},
                {"role": "user", "content": f"Analise os seguintes dados da pesquisa e forneça sugestões de melhorias e insights: {resultados_texto}"}
            ],
            max_tokens=500
        )

        st.write(response.choices[0].message["content"])

# Função para autenticação
def check_password():
    def password_entered():
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # remove the password from the state
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if "password" not in st.session_state:
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("Password incorrect")
        return False
    else:
        return True

# Configuração do Streamlit
st.set_page_config(page_title="Resultados da Pesquisa de Jiu-Jitsu", layout="wide")

# Exibir a logo no topo da página
st.image("logo.png", width=200)

# Instância da pesquisa
pesquisa = PesquisaJiuJitsu(logo_path="logo.png")

if check_password():
    st.title("Resultados das Pesquisas")
    tipo_pesquisa = st.selectbox("Selecione o tipo de pesquisa", ["Semanal", "Mensal"])
    try:
        if tipo_pesquisa == "Semanal":
            df_semanal = pd.read_csv("respostas_semanal.csv", names=["Sexo", "Idade", "Função"] + [p["pergunta"] for p in PesquisaJiuJitsu(logo_path="logo.png").semanal_perguntas])
            if df_semanal.empty:
                st.warning("Nenhum dado encontrado para a pesquisa semanal.")
            else:
                pesquisa.gerar_relatorio(df_semanal)
                pesquisa.gerar_insights(df_semanal)
        elif tipo_pesquisa == "Mensal":
            df_mensal = pd.read_csv("respostas_mensal.csv", names=["Sexo", "Idade", "Função"] + [p["pergunta"] for p in PesquisaJiuJitsu(logo_path="logo.png").final_perguntas])
            if df_mensal.empty:
                st.warning("Nenhum dado encontrado para a pesquisa mensal.")
            else:
                pesquisa.gerar_relatorio(df_mensal)
                pesquisa.gerar_insights(df_mensal)
    except FileNotFoundError:
        st.error("Arquivo de respostas não encontrado.")
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")