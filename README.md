# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Gerenciador de Colheira de Cana de Açucar

## Kalil

## 👨‍🎓 Integrantes

- <a href="https://github.com/kalilReis">Kalil Reis de Sisto</a>

## 👩‍🏫 Professores

### Tutor(a)

- <a href="https://www.linkedin.com/company/inova-fusca">Leonardo Ruiz Orabona</a>

### Coordenador(a)

- <a href="https://www.linkedin.com/company/inova-fusca"> André Godoy acho</a>

## 📜 Descrição

Este projeto utiliza ciência de dados e aprendizado de máquina para monitorar e otimizar a irrigação agrícola, analisando dados de umidade do solo e condições ambientais. A solução inclui dashboards interativos para visualização dos dados e suporte à tomada de decisão, promovendo o uso eficiente de recursos hídricos no campo.

O arquivo CSV irrigation_data.csv contém registros horários coletados por sensores instalados no campo. Cada linha apresenta o momento da medição (timestamp), o identificador do sensor (sensor_id), a hora do dia (hour), a temperatura do ar (temp), a umidade relativa do ar (humidity_air), a umidade do solo (moisture_soil) e um indicador se houve irrigação naquele período (irrigated). Esses dados são fundamentais para análise do comportamento do solo e para o desenvolvimento de modelos preditivos de irrigação.

![Gráfico de Umidade do Solo ao Longo do Tempo](assets/soil_moisture_over_time_chart.png)
_Gráfico que mostra a variação da umidade do solo ao longo do tempo, permitindo identificar padrões e necessidades de irrigação._

![Gráfico de Umidade do Ar ao Longo do Tempo](assets/humidity_over_time_chart.png)
_Gráfico que apresenta a evolução da umidade relativa do ar, auxiliando na análise das condições ambientais que impactam a irrigação._

![Gráfico de Temperatura ao Longo do Tempo](assets/temperature_over_time_chart.png)
_Gráfico que exibe a variação da temperatura do ar ao longo do tempo, permitindo avaliar o impacto térmico nas condições do solo e na necessidade de irrigação._

![Gráfico de Predição de Irrigação](assets/irrigation_prediction_chart.png)
_Gráfico que demonstra as previsões do modelo de irrigação, indicando os períodos em que a irrigação é recomendada com base na análise dos dados coletados._

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>data</b>: Contém os dados utilizados no projeto, como o modelo de machine learning treinado (`irrigation_model.joblib`) e o arquivo `irrigation_data.csv`, que contém os dados de irrigação.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

Para executar o código, siga os seguintes passos:

1.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

    Este comando irá instalar as bibliotecas necessárias listadas no arquivo `requirements.txt`, que incluem `oracledb`, `python-dotenv`, `scikit-learn` e `streamlit`.

2.  **Configure as variáveis de ambiente:**
    Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis de ambiente:

    ```
    DB_DSN=<seu_dsn>
    DB_USER=<seu_usuario>
    DB_PASSWORD=<sua_senha>
    ```

    Substitua `<seu_dsn>`, `<seu_usuario>` e `<sua_senha>` pelas suas credenciais do banco de dados Oracle.

3.  **Execute os scripts na seguinte ordem:**

    ```bash
    python src/db_setup.py
    python src/db_import.py
    python src/model_training.py
    python src/dashboard.py
    ```

    - `db_setup.py`: Este script cria a tabela `irrigation_data` no banco de dados Oracle.
    - `db_import.py`: Este script importa os dados do arquivo `irrigation_data.csv` para a tabela `irrigation_data` no banco de dados Oracle.
    - `model_training.py`: Este script treina o modelo de machine learning e salva o modelo treinado no arquivo `data/irrigation_model.joblib`.
    - `dashboard.py`: Este script inicia o dashboard Streamlit.

4.  **Acesse o dashboard:**
    Após executar o script `dashboard.py`, o Streamlit irá exibir um link no terminal. Abra este link no seu navegador para acessar o dashboard.

## 🗃 Histórico de lançamentos

- ## 0.5.0 - XX/XX/2024
- ## 0.4.0 - XX/XX/2024
- ## 0.3.0 - XX/XX/2024
- ## 0.2.0 - XX/XX/2024
- ## 0.1.0 - XX/XX/2024

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
