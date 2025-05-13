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
├── notebooks/              # Jupyter Notebooks com as etapas do projeto
│   ├── EDA_V1_.ipynb
│   ├── DeepQLearning_Desafio.ipynb
│   ├── InvesteAI_Reforco.ipynb
│   ├── RandomForest_Desafio.ipynb
│   ├── Regressão_linear_Desafio.ipynb
│   └── ARIMA_e_SARIMA.ipynb
│
├── streamlit_app/          # Aplicativo interativo em Streamlit
│   ├── app.py
│   └── assets/             # Imagens ou arquivos estáticos
│
├── data/                    # Conjunto de dados
│   ├── sp500_2015_2024.csv
│   ├── sp500_2025.csv      
│   └── SP500.csv
│
├── reports/                # Relatório do desafio
│   └── VIII_Desafio_InvesteAI_Relatorio.docx
│
├── models/                 # Modelos treinados salvos
│   └── trading_bot.pkl
│
└── README.md               # Este arquivo


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
