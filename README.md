# Pesquisa de Feedback do Programa de Treinamento de Jiu-Jitsu

Este projeto coleta e analisa o feedback de um programa de treinamento de Jiu-Jitsu. Ele inclui uma pesquisa semanal, uma pesquisa mensal e uma página de resultados, utilizando Streamlit para criar uma interface web interativa.

## Estrutura do Projeto

/PesquisaJiuJitsu
│
├── .streamlit
│ └── secrets.toml
├── logo.png
├── pesquisa_semanal.py
├── pesquisa_mensal.py
├── resultados.py
├── requirements.txt
└── README.md
## Instruções de Uso

### Pré-requisitos

- Python 3.x
- Bibliotecas listadas em `requirements.txt`

### Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/PesquisaJiuJitsu.git
    cd PesquisaJiuJitsu
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure a senha e a chave da API OpenAI:
    - Crie um arquivo `secrets.toml` no diretório `.streamlit`:
        ```bash
        mkdir -p .streamlit
        touch .streamlit/secrets.toml
        ```
    - Adicione a senha e a chave da API OpenAI ao arquivo `secrets.toml`:
        ```toml
        # .streamlit/secrets.toml
        password = "sua_senha_secreta"
        openai_api_key = "sua_chave_api_openai"
        ```

### Execução

1. Coloque a logo da sua empresa no arquivo `logo.png`.

2. Para executar a pesquisa semanal:
    ```bash
    streamlit run pesquisa_semanal.py
    ```

3. Para executar a pesquisa mensal:
    ```bash
    streamlit run pesquisa_mensal.py
    ```

4. Para visualizar os resultados:
    ```bash
    streamlit run resultados.py
    ```

### Coleta de Respostas

As perguntas serão exibidas na interface web, e você deve selecionar a opção desejada e clicar no botão "Enviar".

### Armazenamento de Respostas

As respostas são armazenadas em arquivos CSV (`respostas_semanal.csv` e `respostas_mensal.csv`) para análise posterior.

### Acesso aos Resultados

Para acessar os resultados, selecione o tipo de pesquisa na página "Resultados" e insira a senha correta. Você poderá visualizar os gráficos gerados com base nas respostas coletadas e receberá insights e sugestões de melhorias do ChatGPT.

### Acesso via Mobile

O aplicativo Streamlit pode ser acessado via mobile através do navegador, utilizando o endereço IP da máquina onde o aplicativo está sendo executado.

## Contribuição

Sinta-se à vontade para contribuir com melhorias para este projeto. Faça um fork do repositório, crie um branch para suas alterações e envie um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT.