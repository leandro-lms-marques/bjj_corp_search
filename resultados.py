import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

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
        if df.empty:
            st.warning("Nenhum dado disponível para gerar o relatório.")
            return

        for pergunta in df.columns[3:]:
            if pergunta not in df.columns:
                continue

            dados = df[pergunta].value_counts()
            if dados.empty:
                st.warning(f"BJJ CORP, transformando vidas através do Jiu-Jitsu!")
                continue

            plt.figure(figsize=(10, 5))
            dados.plot(kind='bar')
            plt.title(pergunta)
            plt.xlabel('Respostas')
            plt.ylabel('Frequência')

            logo = plt.imread(self.logo_path)
            imagebox = OffsetImage(logo, zoom=0.1)
            ab = AnnotationBbox(imagebox, (0.5, 0.5), frameon=False, xycoords='axes fraction', boxcoords="axes fraction", pad=0.1)
            plt.gca().add_artist(ab)

            st.pyplot(plt)

st.set_page_config(page_title="Resultados da Pesquisa de Jiu-Jitsu", layout="wide")

st.image("logo.png", width=200)

pesquisa = PesquisaJiuJitsu(logo_path="logo.png")

st.title("Resultados das Pesquisas")
tipo_pesquisa = st.selectbox("Selecione o tipo de pesquisa", ["Semanal", "Mensal"])

try:
    if tipo_pesquisa == "Semanal":
        df_semanal = pd.read_csv("respostas_semanal.csv", names=["Sexo", "Idade", "Função"] + [p["pergunta"] for p in pesquisa.semanal_perguntas])
        st.write("Dados Semanais Carregados:", df_semanal.head())  # Debug: Mostrar os dados carregados
        if df_semanal.empty:
            st.warning("Nenhum dado encontrado para a pesquisa semanal.")
        else:
            pesquisa.gerar_relatorio(df_semanal)
    elif tipo_pesquisa == "Mensal":
        df_mensal = pd.read_csv("respostas_mensal.csv", names=["Sexo", "Idade", "Função"] + [p["pergunta"] for p in pesquisa.final_perguntas])
        st.write("Dados Mensais Carregados:", df_mensal.head())  # Debug: Mostrar os dados carregados
        if df_mensal.empty:
            st.warning("Nenhum dado encontrado para a pesquisa mensal.")
        else:
            pesquisa.gerar_relatorio(df_mensal)
except FileNotFoundError:
    st.error("Arquivo de respostas não encontrado.")
except pd.errors.EmptyDataError:
    st.error("O arquivo de respostas está vazio.")
except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")