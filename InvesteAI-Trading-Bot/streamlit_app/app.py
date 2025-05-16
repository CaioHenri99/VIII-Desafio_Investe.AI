import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import os
import sys

# Adicionar o diretório atual ao PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# Configuração da página
st.set_page_config(
    page_title="InvesteAI - Resultados do Backtest",
    page_icon="📈",
    layout="wide"
)

# Título e subtítulo
st.title("VIII Desafio em ciência de dados: investe.ia")
st.subheader("Grupo: Os excluídos da ciência.")

# Função que usa a função do deepqlearning_investeai.py para executar o backtest
def executar_backtest():
    """
    Executa o backtest usando a função do módulo deepqlearning_investeai.py
    """
    try:
        # Importar a função do módulo deepqlearning_investeai
        st.write("Tentando importar o módulo deepqlearning_investeai...")
        from deepqlearning_investeai import rodar_modelo_backtest
        st.write("Módulo importado com sucesso!")
        
        # Caminho para o modelo
        current_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(current_dir, "model_ep30.keras")
        st.write(f"Verificando modelo em: {model_path}")
        
        if not os.path.exists(model_path):
            st.error(f"Modelo não encontrado em: {model_path}")
            raise FileNotFoundError(f"Modelo não encontrado: {model_path}")
        
        st.write("Modelo encontrado! Iniciando backtest...")
        
        with st.spinner("Executando backtest..."):
            # Usar a função importada para rodar o modelo
            resultados = rodar_modelo_backtest(model_path)
            
            if resultados:
                st.success("Backtest executado com sucesso!")
                return resultados
            else:
                st.error("Falha ao executar o backtest. Usando valores de exemplo.")
    except ImportError as e:
        st.error(f"Erro ao importar o módulo: {e}")
        st.write("Detalhes técnicos:", str(e))
    except Exception as e:
        st.error(f"Erro ao executar o backtest: {e}")
        import traceback
        st.write("Detalhes técnicos:", traceback.format_exc())
    
    # Se houver falha, retornar valores de exemplo
    st.info("Usando valores de exemplo para demonstração.")
    return {
        'valor_inicial': 100000.00,
        'valor_final': 124488.52,
        'lucro_total': 24488.52,
        'total_trades': 250,
        'vencedoras': 137,
        'perdedoras': 113,
        'win_rate': 54.80,
        'sharpe_ratio': 1.765,
        'dados_grafico': {
            'steps': list(range(80)),
            'patrimonio': list(np.linspace(100000, 124488, 80) + np.random.normal(0, 2000, 80).cumsum() * 0.1)
        }
    }

# Sidebar para controles
st.sidebar.title("Controles")
if st.sidebar.button("Executar Backtest"):
    resultados = executar_backtest()
    # Salvar resultados na sessão para persistir entre reloads
    st.session_state['resultados'] = resultados
    st.experimental_rerun()
elif 'resultados' not in st.session_state:
    # Na primeira execução ou se não houver resultados salvos
    st.session_state['resultados'] = executar_backtest()

# Obter resultados da sessão
resultados = st.session_state['resultados']

# Mostrar as métricas principais em um estilo de painel
col1, col2, col3 = st.columns(3)
col1.metric("Início do teste", f"R$ {resultados['valor_inicial']:.2f}")
col1.metric("Fim do teste", f"R$ {resultados['valor_final']:.2f}")
col1.metric("Lucro total", f"R$ {resultados['lucro_total']:.2f}")

col2.metric("Total trades", f"{resultados['total_trades']}")
col2.metric("Vencedoras", f"{resultados['vencedoras']}")
col2.metric("Perdedoras", f"{resultados['perdedoras']}, Win rate: {resultados['win_rate']:.2f}%")

col3.metric("Sharpe ratio", f"{resultados['sharpe_ratio']:.3f}")

# Separador
st.markdown("---")

# Gráficos de visualização
st.header("Gráficos de visualização")

# Criar DataFrame para o gráfico
dados = resultados['dados_grafico']
df = pd.DataFrame({
    'step': dados['steps'],
    'patrimonio': dados['patrimonio']
})

# Plotar gráfico de evolução do patrimônio
fig = px.line(df, x='step', y='patrimonio', title=f'Lucro total: R$ {resultados["lucro_total"]:.2f}')

# Adicionar pontos de compra e venda, se disponíveis
if 'acoes' in dados:
    acoes = dados['acoes']
    patrimonio = dados['patrimonio']
    compras = []
    vendas = []
    
    for i in range(1, len(acoes)):
        if acoes[i] > 0:  # Compra
            compras.append((i, patrimonio[i]))
        elif acoes[i] < 0:  # Venda
            vendas.append((i, patrimonio[i]))
    
    # Criar DataFrames para pontos de compra e venda
    df_compras = pd.DataFrame(compras, columns=['step', 'patrimonio']) if compras else pd.DataFrame(columns=['step', 'patrimonio'])
    df_vendas = pd.DataFrame(vendas, columns=['step', 'patrimonio']) if vendas else pd.DataFrame(columns=['step', 'patrimonio'])
    
    if not df_compras.empty:
        fig.add_scatter(x=df_compras['step'], y=df_compras['patrimonio'], 
                        mode='markers', marker=dict(color='blue', size=12),
                        name='Compra')
    
    if not df_vendas.empty:
        fig.add_scatter(x=df_vendas['step'], y=df_vendas['patrimonio'], 
                        mode='markers', marker=dict(color='red', size=12),
                        name='Venda')

fig.update_layout(
    xaxis_title="Steps",
    yaxis_title="Patrimônio",
    legend_title="Operações",
    width=800,
    height=500
)

st.plotly_chart(fig)

# Adicionar filtro para mostrar apenas operações específicas
st.subheader("Filtro de Operações")
mostrar_apenas = st.radio(
    "Mostrar apenas:",
    ("Todas", "Compras", "Vendas"),
    horizontal=True
)

if mostrar_apenas != "Todas" and 'acoes' in dados:
    acoes = dados['acoes']
    patrimonio = dados['patrimonio']
    operacoes = []
    
    for i in range(1, len(acoes)):
        if mostrar_apenas == "Compras" and acoes[i] > 0:
            operacoes.append((i, patrimonio[i]))
        elif mostrar_apenas == "Vendas" and acoes[i] < 0:
            operacoes.append((i, patrimonio[i]))
    
    # Criar DataFrame para as operações filtradas
    df_operacoes = pd.DataFrame(operacoes, columns=['step', 'patrimonio']) if operacoes else pd.DataFrame(columns=['step', 'patrimonio'])
    
    # Criar gráfico filtrado
    if not df_operacoes.empty:
        fig_filtrado = px.line(df, x='step', y='patrimonio', title=f'Operações de {mostrar_apenas.lower()}')
        
        color = 'blue' if mostrar_apenas == "Compras" else 'red'
        fig_filtrado.add_scatter(
            x=df_operacoes['step'], 
            y=df_operacoes['patrimonio'],
            mode='markers', 
            marker=dict(color=color, size=15),
            name=mostrar_apenas
        )
        
        fig_filtrado.update_layout(
            xaxis_title="Steps",
            yaxis_title="Patrimônio",
            width=800,
            height=400
        )
        
        st.plotly_chart(fig_filtrado)
    else:
        st.info(f"Não há operações de {mostrar_apenas.lower()} para exibir.")

# Informações adicionais
st.sidebar.title("Sobre o projeto")
st.sidebar.info("""
Este aplicativo apresenta os resultados do backtest do modelo DeepQLearning InvesteAI.
O modelo foi treinado para tomar decisões de compra e venda no mercado financeiro.

O backtest é executado importando o ambiente e o modelo treinado diretamente do
arquivo deepqlearning_investeai.py.
""")

# Rodapé
st.markdown("---")
st.markdown("**InvesteAI** - Sistema de recomendação de investimentos baseado em Deep Q-Learning")
