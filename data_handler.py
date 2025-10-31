import pandas as pd
import streamlit as st
import time
import locale

# Define o formato local para moeda brasileira (R$, separador de milhar com ponto)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def formatar_valor(x):
    # Converte número em formato monetário (R$ 1.000,00)
    return locale.currency(x, grouping=True)

def salvar_dados(df, nome_arquivo="data.csv"):
    # Salva o DataFrame em arquivo CSV sem índice
    df.to_csv(nome_arquivo, index=False)

def carregar_dados(nome_arquivo="data.csv"):
    # Lê os dados do arquivo CSV e retorna como DataFrame
    try:
        df = pd.read_csv(nome_arquivo)

        # Verifica se o arquivo está vazio
        if df.empty:
            st.warning("⚠️ O arquivo está vazio. Nenhum dado foi carregado.")
            return None
        
        # Garante que a coluna de descrição não tenha valores nulos
        if "DESCRIÇÃO" in df.columns:
            df["DESCRIÇÃO"] = df["DESCRIÇÃO"].fillna("").replace({None: ""})

        # Atualiza o estado da sessão com os dados carregados
        st.session_state['transactions'] = df.to_dict(orient="list")

        st.success("📂 Dados carregados com sucesso!")
        time.sleep(1)
        return df

    # Caso o arquivo não exista
    except FileNotFoundError:
        st.warning("⚠️ Nenhum arquivo salvo encontrado.")
        return None

    # Caso o arquivo exista, mas esteja completamente vazio
    except pd.errors.EmptyDataError:
        st.warning("⚠️ O arquivo existe, mas está vazio. Nenhum dado foi carregado.")
        return None