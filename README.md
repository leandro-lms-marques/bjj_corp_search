# Sistema de Pesquisa de Satisfação do Treinamento de Jiu-Jitsu

Este projeto é um sistema de pesquisa desenvolvido para coletar e analisar feedback de participantes de um programa de treinamento de Jiu-Jitsu. Ele utiliza o Streamlit para criar interfaces de usuário interativas para a coleta de dados e geração de relatórios.

## Estrutura do Projeto

O projeto está organizado nos seguintes arquivos:

- `pesquisa_semanal.py`: Script para a coleta de respostas semanais dos participantes.
- `pesquisa_mensal.py`: Script para a coleta de respostas mensais dos participantes.
- `resultados.py`: Script para a geração de relatórios baseados nas respostas coletadas.

## Funcionalidades

### Coleta de Respostas

- **Pesquisa Semanal**: Coleta feedback sobre as aulas de Jiu-Jitsu a cada semana, abordando aspectos como satisfação, pertencimento à equipe, resiliência, produtividade e estresse.
- **Pesquisa Mensal**: Coleta feedback sobre o impacto geral do programa de treinamento de Jiu-Jitsu, incluindo aspectos de saúde mental e física.

### Geração de Relatórios

- Gera relatórios visuais das respostas coletadas, permitindo uma análise fácil dos dados.
- Inclui gráficos de barras para cada pergunta, com a opção de adicionar um logotipo personalizado.

## Pré-requisitos

- **Python 3.x**: Certifique-se de ter o Python instalado na sua máquina.
- **Bibliotecas Python**: As seguintes bibliotecas são necessárias:
  - `streamlit`
  - `pandas`
  - `matplotlib`

Você pode instalar as dependências necessárias executando:

```bash
pip install streamlit pandas matplotlib