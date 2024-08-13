import streamlit as st
import pandas as pd

class PesquisaJiuJitsu:
    def __init__(self):
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

    def coletar_respostas(self):
        if "respostas_semanal" not in st.session_state:
            st.session_state["respostas_semanal"] = {}

        respostas = st.session_state["respostas_semanal"]
        sexo_opcoes = ["Masculino", "Feminino", "Outro"]
        sexo_index = sexo_opcoes.index(respostas.get("Sexo", sexo_opcoes[0])) if "Sexo" in respostas else 0
        respostas["Sexo"] = st.selectbox("Sexo", sexo_opcoes, index=sexo_index)

        respostas["Idade"] = st.number_input("Idade", min_value=0, max_value=120, step=1, value=respostas.get("Idade", 0))
        respostas["Função"] = st.text_input("Função", value=respostas.get("Função", ""))

        for pergunta in self.semanal_perguntas:
            resposta_opcoes = pergunta["opcoes"]
            resposta_index = resposta_opcoes.index(respostas.get(pergunta["pergunta"], resposta_opcoes[0])) if pergunta["pergunta"] in respostas else 0
            resposta = st.radio(pergunta["pergunta"], resposta_opcoes, index=resposta_index)
            respostas[pergunta["pergunta"]] = resposta

        st.session_state["respostas_semanal"] = respostas
        return respostas

    def analisar_respostas(self, respostas):
        df = pd.DataFrame([respostas])
        return df

# Configuração do Streamlit
st.set_page_config(page_title="Pesquisa Semanal do treinamento", layout="wide")

# Exibir a logo no topo da página
st.image("logo.png", width=200)

# Instância da pesquisa
pesquisa = PesquisaJiuJitsu()

st.title("Pesquisa Semanal do treinamento")
respostas_semanal = pesquisa.coletar_respostas()
if st.button("Enviar"):
    if not respostas_semanal["Idade"] or not respostas_semanal["Função"]:
        st.error("Por favor, preencha todos os campos obrigatórios.")
    else:
        try:
            df_semanal = pesquisa.analisar_respostas(respostas_semanal)
            df_semanal.to_csv("respostas_semanal.csv", mode='a', header=False, index=False)
            st.write("Respostas enviadas com sucesso!")
            st.session_state["respostas_semanal"] = {}  # Limpar respostas após envio
        except Exception as e:
            st.error(f"Erro ao salvar as respostas: {e}")