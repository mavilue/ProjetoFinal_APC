import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

from transactions import init_session, add_transaction
from utils import calcular_saldo
from data_handler import salvar_dados, carregar_dados

st.set_page_config(page_title="Controle de Gastos", page_icon="💰", layout="centered")
st.title("💰 CONTROLE DE GASTOS PESSOAIS")

# Inicializa a sessão
init_session()

# Formulário de entrada
st.subheader("➕ Adicionar nova movimentação")

categoria = st.selectbox(
    "Categoria",
    ["Selecione", "Alimentação", "Transporte", "Moradia", "Saúde", "Educação",
     "Salário", "Renda extra", "Investimento", "Serviços digitais", "Lazer", "Cuidados pessoais", "Outros"]
)

tipo_mov = st.radio("Tipo de movimentação", ["Receita", "Despesa"])
valor = st.number_input("Valor (R$)", min_value=0.0, format="%.2f")
descricao = st.text_area("Descrição")
data = st.date_input("Data", value=date.today())
data_format = data.strftime("%d/%m/%Y")

if st.button("Adicionar"):
    if categoria == "Selecione" or valor <= 0:
        st.warning("⚠️ Preencha todos os campos corretamente antes de adicionar.")
    else:
        add_transaction(categoria, tipo_mov, valor, descricao, data_format)
        st.success("✅ Movimentação adicionada com sucesso!")

# Criar DataFrame
df = pd.DataFrame(st.session_state['transactions'])

# Mostrar saldo
if not df.empty:
    saldo = calcular_saldo(st.session_state['transactions'])
    st.header(f"💸 Saldo Atual: R$ {saldo:.2f}")

# Mostrar tabela
st.subheader("📋 Histórico de Movimentações")
st.dataframe(df)

# Mostrar gráfico
if not df.empty and "Despesa" in df["tipo_movimentacao"].values:
    st.subheader("📊 Gastos por Categoria")
    despesas = df[df["tipo_movimentacao"] == "Despesa"]
    categorias = despesas.groupby("categoria_select")["valor_insert"].sum()

# grafico de pizza
    fig, ax = plt.subplots()
    ax.pie(categorias, labels=categorias.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.legend(categorias.index, title="Despesas", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    st.pyplot(fig)

# Botões de salvar e carregar
col1, col2 = st.columns(2)
with col1:
    if st.button("💾 Salvar dados"):
        salvar_dados(df)

with col2:
    if st.button("📂 Carregar dados salvos"):
        novo_df = carregar_dados()
        if novo_df is not None:
            df = novo_df
