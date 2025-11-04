import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import time

from data_handler import formatar_valor, salvar_dados, carregar_dados
from transactions import init_session, add_transaction
from utils import calcular_saldo

# Configura a aparência e informações da página
st.set_page_config(page_title="Controle de Gastos", page_icon="💰", layout="centered")

# Título da aplicação
st.title("💰 CONTROLE DE GASTOS PESSOAIS")
# Inicializa a sessão (cria as variáveis se ainda não existirem)
init_session()
# Cabeçalho da seção de entrada de dados
st.subheader("➕ Adicionar nova movimentação")
# Campo de seleção para categoria da movimentação
categoria = st.selectbox(
    "Categoria",
    ["Selecione", "Alimentação", "Transporte", "Moradia", "Saúde", "Educação",
     "Salário", "Renda extra", "Investimento", "Serviços digitais", "Lazer", "Cuidados pessoais", "Outros"]
)
# Escolha entre Receita ou Despesa
tipo_mov = st.radio("Tipo de movimentação", ["Receita", "Despesa"])
# Campo numérico para o valor da movimentação
valor = st.number_input("Valor (R$)", min_value=0.0, format="%.2f")
# Campo de texto para descrição opcional
descricao = st.text_area("Descrição")
# Campo de data (por padrão usa a data atual)
data = st.date_input("Data", value=date.today())
data_format = data.strftime("%d/%m/%Y")  # Formata a data no padrão brasileiro

# Quando o botão é pressionado
if st.button("Adicionar"):
    # Verifica se todos os campos foram preenchidos corretamente
    if categoria == "Selecione" or valor <= 0:
        st.warning("⚠️ Preencha todos os campos corretamente antes de adicionar.")
    else:
        # Adiciona os dados à sessão
        add_transaction(categoria, tipo_mov, valor, descricao, data_format)
        st.success("✅ Movimentação adicionada com sucesso!")

        # Salva os dados no arquivo CSV automaticamente
        df = pd.DataFrame(st.session_state['transactions'])
        salvar_dados(df)

        time.sleep(1)
        st.rerun()
        
# Cria um DataFrame com as transações salvas na sessão
df = pd.DataFrame(st.session_state['transactions'])

# Exibe o saldo atual se houver movimentações registradas
if not df.empty:
    saldo = calcular_saldo(st.session_state['transactions'])
    st.header(f"💸 Saldo Atual: R$ {saldo:.2f}")

# Exibe a tabela com todas as movimentações
st.subheader("Histórico de Movimentações")

# Ajusta o índice da tabela para começar em 1
df.index = df.index + 1

# Formata a coluna de valores com R$ e separadores de milhar
df_estilizado = df.style.format({"VALOR": formatar_valor})

# Exibe a tabela estilizada
st.dataframe(df_estilizado)

# Se houver despesas, gera o gráfico de pizza por categoria
if not df.empty and "Despesa" in df["TIPO"].values:
    st.subheader("📊 Gastos por Categoria")
    despesas = df[df["TIPO"] == "Despesa"]  # Filtra apenas despesas
    categorias = despesas.groupby("CATEGORIA")["VALOR"].sum()  # Soma por categoria

    # Cria o gráfico de pizza
    fig, ax = plt.subplots()
    ax.pie(categorias, labels=categorias.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Deixa o gráfico circular
    ax.legend(categorias.index, title="Despesas", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    st.pyplot(fig)

# Botão para carregar dados salvos do arquivo CSV
if st.button("📂 Carregar dados salvos"):
    novo_df = carregar_dados()
    if novo_df is not None:
        st.rerun()