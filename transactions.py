import streamlit as st

def init_session():
    # Cria estrutura inicial na sessão para armazenar as transações
    if 'transactions' not in st.session_state:
        st.session_state['transactions'] = {
            "CATEGORIA": [],  
            "TIPO": [],        
            "VALOR": [],       
            "DESCRIÇÃO": [],   
            "DATA": []         
        }
        
def add_transaction(categoria, tipo, valor, descricao, data):
    # Adiciona uma nova linha de movimentação ao dicionário da sessão
    tr = st.session_state['transactions']
    tr['CATEGORIA'].append(categoria)
    tr['TIPO'].append(tipo)
    tr['VALOR'].append(valor)
    tr['DESCRIÇÃO'].append(descricao)
    tr['DATA'].append(data)
