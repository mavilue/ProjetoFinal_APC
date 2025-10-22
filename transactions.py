import streamlit as st

def init_session():
    if 'transactions' not in st.session_state:
        st.session_state['transactions'] = {
            "categoria_select": [],
            "tipo_movimentacao": [],
            "valor_insert": [],
            "descricao_f": [],
            "data_inscrita": []
        }
        
def add_transaction(categoria, tipo, valor, descricao, data):
    tr = st.session_state['transactions']
    
    tr['categoria_select'].append(categoria)
    tr['tipo_movimentacao'].append(tipo)
    tr['valor_insert'].append(valor)
    tr['descricao_f'].append(descricao)
    tr['data_inscrita'].append(data)
    
