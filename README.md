# 🧠 VIII Desafio em Ciência de Dados - Investe.AI

Este repositório contém a solução desenvolvida para o **VIII Desafio em Ciência de Dados**. O desafio propõe a aplicação de técnicas de ciência de dados e aprendizado de máquina na análise e predição de dados do **Mercado Financeiro**, simulando um cenário real de tomada de decisão baseada em dados. Desenvolvemos um bot de trading capaz de realizar decisões automáticas de compra, venda ou manutenção de ativos no mercado financeiro, utilizando dados históricos e técnicas de ciência de dados.

---

## 📌 Objetivo

O objetivo deste projeto é construir um bot inteligente para operar no mercado financeiro. Ele deve ser capaz de:

- Analisar dados históricos de preços e indicadores financeiros
- Identificar padrões e tendências relevantes
- Tomar decisões automatizadas de trading: **comprar**, **vender** ou **manter**
- Realizar **backtesting** para validar sua performance
- Ser integrado em uma interface interativa usando **Streamlit**

---

## 📁 Estrutura do Repositório

InvesteAI-Trading-Bot/
├── notebooks/ # Jupyter Notebooks com as etapas do projeto
│ ├── EDA_V1_.ipynb # Análise exploratória dos dados
│ ├── DeepQLearning_Desafio.ipynb # Implementação de aprendizado por reforço profundo
│ ├── InvesteAI_Reforco.ipynb # Estratégia baseada em aprendizado por reforço
│ ├── RandomForest_Desafio.ipynb # Modelo Random Forest para decisão de trade
│ ├── Regressão_linear_Desafio.ipynb # Abordagem com regressão linear
│ └── ARIMA_e_SARIMA.ipynb # Modelos de séries temporais (ARIMA e SARIMA)
│
├── streamlit_app/ # Aplicativo interativo em Streamlit
│ ├── app.py # Interface com o bot de trading
│ └── assets/ # Imagens ou arquivos estáticos usados no app
│
├── data/ # Conjunto de dados históricos
│ ├── sp500_2015_2024.csv # Dados do S&P 500 entre 2015 e 2024
│ ├── sp500_2025.csv # Dados de 2025 (ano atual)
│ └── SP500.csv # Arquivo geral com histórico do índice
│
├── reports/ # Relatório do desafio
│ └── VIII_Desafio_InvesteAI_Relatorio.docx
│
├── models/ # Modelos treinados salvos
│ └── trading_bot.pkl # Modelo final exportado
│
└── README.md # Este arquivo


---


## 🛠️ Tecnologias Utilizadas
- Python (Pandas, NumPy, Scikit-learn)
- Jupyter Notebook
- Streamlit
- Matplotlib / Plotly
- APIs de dados financeiros (ex: Yahoo Finance, Alpha Vantage)
- Backtesting com estratégias baseadas em machine learning

---

## 📊 Exemplo de Decisão do Bot

= O bot analisa dados como médias móveis, RSI, volume e realiza previsões com base em modelos supervisionados para sugerir ações como:

Data	Preço Fechamento	Ação Sugerida
2023-06-01	104.32	🟢 Comprar
2023-06-02	108.50	🔴 Vender
2023-06-05	106.20	🟡 Manter

---


## 📄 Relatório

O relatório completo da solução, abordando metodologia, resultados e conclusões, está disponível na pasta:

/reports/VIII_Desafio_InvesteAI_Relatorio.docx
