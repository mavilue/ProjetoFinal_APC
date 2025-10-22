
def calcular_saldo(tr):
    
    valor_total = 0
    
    for i in range(len(tr['tipo_movimentacao'])):
        tipo = tr['tipo_movimentacao'][i]
        valor = tr['valor_insert'][i]
        
        if tipo == 'Receita':
            valor_total += valor
        elif tipo == 'Despesa':
            valor_total -= valor
    
    return valor_total