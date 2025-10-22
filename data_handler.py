import pandas as pd
import streamlit as st

def salvar_dados(df, nome_arquivo="data.csv"):
    """Salva o DataFrame em um arquivo CSV."""
    df.to_csv(nome_arquivo, index=False)
    st.success("💾 Dados salvos com sucesso!")

def carregar_dados(nome_arquivo="data.csv"):
    """Carrega dados salvos do arquivo CSV, se existir."""
    try:
        df = pd.read_csv(nome_arquivo)
        st.session_state['transactions'] = df.to_dict(orient="list")
        st.success("📂 Dados carregados com sucesso!")
        return df
    except FileNotFoundError:
        st.warning("⚠️ Nenhum arquivo salvo encontrado.")
        return None
