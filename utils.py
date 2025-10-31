def calcular_saldo(tr):
    valor_total = 0
    
    for i in range(len(tr['TIPO'])):
        tipo = tr['TIPO'][i]
        valor = tr['VALOR'][i]
        
        if tipo == 'Receita':
            valor_total += valor
        elif tipo == 'Despesa':
            valor_total -= valor
    
    return valor_total
