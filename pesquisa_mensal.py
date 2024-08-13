import streamlit as st
import pandas as pd

class PesquisaJiuJitsu:
    def __init__(self):
        self.mensal_perguntas = [
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

    def coletar_respostas(self):
        if "respostas_mensal" not in st.session_state:
            st.session_state["respostas_mensal"] = {}

        respostas = st.session_state["respostas_mensal"]
        sexo_opcoes = ["Masculino", "Feminino", "Outro"]
        sexo_valor = respostas.get("Sexo", sexo_opcoes[0])
        sexo_index = sexo_opcoes.index(sexo_valor) if sexo_valor in sexo_opcoes else 0
        respostas["Sexo"] = st.selectbox("Sexo", sexo_opcoes, index=sexo_index)

        respostas["Idade"] = st.number_input("Idade", min_value=0, max_value=120, step=1, value=respostas.get("Idade", 0))
        respostas["Função"] = st.text_input("Função", value=respostas.get("Função", ""))

        for pergunta in self.mensal_perguntas:
            resposta_opcoes = pergunta["opcoes"]
            if resposta_opcoes:  # Verificar se a lista de opções não está vazia
                resposta_valor = respostas.get(pergunta["pergunta"], resposta_opcoes[0])
                resposta_index = resposta_opcoes.index(resposta_valor) if resposta_valor in resposta_opcoes else 0
                resposta = st.radio(pergunta["pergunta"], resposta_opcoes, index=resposta_index)
                respostas[pergunta["pergunta"]] = resposta

        st.session_state["respostas_mensal"] = respostas
        return respostas

    def analisar_respostas(self, respostas):
        df = pd.DataFrame([respostas])
        return df

# Configuração do Streamlit
st.set_page_config(page_title="Pesquisa Final do treinamento", layout="wide")

# Exibir a logo no topo da página
st.image("logo.png", width=200)

# Instância da pesquisa
pesquisa = PesquisaJiuJitsu()

st.title("Pesquisa Final do treinamento")
respostas_mensal = pesquisa.coletar_respostas()
if st.button("Enviar"):
    if not respostas_mensal["Idade"] or not respostas_mensal["Função"]:
        st.error("Por favor, preencha todos os campos obrigatórios.")
    else:
        try:
            df_mensal = pesquisa.analisar_respostas(respostas_mensal)
            df_mensal.to_csv("respostas_mensal.csv", mode='a', header=False, index=False)
            st.write("Respostas enviadas com sucesso!")
            st.session_state["respostas_mensal"] = {}  # Limpar respostas após envio
        except Exception as e:
            st.error(f"Erro ao salvar as respostas: {e}")