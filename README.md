# Documentação Técnica – Projeto Controle de Gastos

## Descrição Geral

O **Controle de Gastos** é um aplicativo desenvolvido em **Python** com o framework **Streamlit**, criado para auxiliar o usuário a registrar e acompanhar suas movimentações financeiras pessoais.  

O sistema permite o cadastro de **receitas e despesas**, armazenando as informações em um arquivo CSV e exibindo um **saldo total atualizado automaticamente**.

---

## Objetivos do Projeto

- Proporcionar uma interface simples e intuitiva para controle financeiro pessoal.  
- Demonstrar conhecimentos em Python, manipulação de dados e interface web.  
- Servir como projeto de encerramento de período da disciplina de **Algoritimos e Programação de Computadores**.  

---

## Requisitos Funcionais

| Requisito | Descrição |
|------------|-----------|
| Adicionar transações | O usuário pode registrar receitas ou despesas. |
| Calcular saldo total | O sistema exibe o saldo com base nas movimentações registradas. |
| Persistência dos dados | As informações são armazenadas automaticamente em arquivo CSV. |
| Carregamento automático | Ao iniciar o app, os dados previamente salvos são carregados. |
| Interface interativa | O usuário interage por meio de botões, formulários e tabelas. |

> Funcionalidades de **edição e remoção** (CRUD completo) estão previstas como **melhorias futuras**.

---

## Estrutura do Projeto
```
controle_gastos/
│
├── app.py            # Arquivo principal do Streamlit (interface)
├── data_handler.py   # Funções para carregar e salvar dados CSV
├── transactions.py   # Funções para adicionar transações
├── utils.py          # Funções auxiliares (ex: cálculo do saldo)
├── requirements.txt  # Lista de dependências do projeto
└── data.csv          # Arquivo gerado automaticamente com os dados (não versionado)
```


---

## Descrição dos Arquivos

### **1. app.py**
Arquivo principal do aplicativo.  
- Responsável pela interface com o usuário.  
- Lida com a coleta dos dados via Streamlit.  
- Exibe as transações e o saldo total.  

### **2. data_handler.py**
Gerencia a persistência de dados.  
- `carregar_dados()`: lê o arquivo `data.csv` e retorna um DataFrame.  
- `salvar_dados(df)`: grava o DataFrame no arquivo CSV.  

### **3. transactions.py**
Contém as funções relacionadas às operações nas transações.  
- `adicionar_transacao()`  
 

### **4. utils.py**
Contém funções auxiliares e de cálculo.  
- `calcular_saldo(df)`: retorna o saldo total considerando receitas e despesas.  

### **5. requirements.txt**
Arquivo com as dependências necessárias para execução do projeto.  
Conteúdo:

- streamlit
- pandas
- matplotlib

---

## Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/mavilue/ProjetoFinal_APC.git
cd ProjetoFinal_APC
```
### 2. Criar e ativar ambiente virtual (opcional)
``` bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
### 3. Instalar dependências
``` bash
pip install -r requirements.txt
```
### 4. Executar o aplicativo
``` bash
streamlit run app.py
```
---

## Funcionamento do Sistema

- O usuário insere os dados da transação (categoria, tipo, valor, descrição, data).
- O app salva automaticamente no arquivo data.csv.
- O saldo total é atualizado dinamicamente.
- As transações são exibidas em formato de tabela interativa.
- Ao reiniciar o app, os dados anteriores são carregados automaticamente.

## Considerações sobre o Arquivo data.csv

- O arquivo é gerado automaticamente.
- Não deve ser versionado no GitHub (adicionar ao .gitignore).
- Caso o arquivo não exista, o sistema cria um novo automaticamente.

## Melhorias Futuras

- Implementar edição e remoção de transações (CRUD completo).
- Criar filtros por categoria e intervalo de datas.
- Adicionar gráficos interativos com receitas x despesas.
- Utilizar SQLite para persistência mais robusta.
- Implementar autenticação de usuários.
