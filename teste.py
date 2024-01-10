import shelve

def salvar_progresso(tempo_feito):
    d = shelve.open("aba")

    match operador:
        case '+':
            nome_operador = 'Adição'
        case '-':
            nome_operador = 'Subtração'
        case '*':
            nome_operador = 'Multiplicação'

    info = d['melhores']
    if info[nome_operador][numero_operado] is None:
        info[nome_operador][numero_operado] = tempo_feito
        d['melhores'] = info
    elif tempo_feito < d['melhores'][nome_operador][numero_operado]:
        info[nome_operador][numero_operado] = tempo_feito
        d['melhores'] = info

    d.close()

d = shelve.open("aba")

if 'melhores' not in d:
    d['melhores'] = {
        'Multiplicação': {1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None,10:None},
        'Subtração': {1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None,10:None},
        'Adição': {1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None,10:None}
    }
d.close()

d = shelve.open("aba")

info = d['melhores']
info['Multiplicação'][1] = 22
d['melhores'] = info

melhores = d['melhores']
for operacoes in melhores:
    print(operacoes)
    for num_operado in melhores[operacoes]:
        if melhores[operacoes][num_operado] is None:
            record = "Sem Registro!"
        else:
            record = melhores[operacoes][num_operado]
        print(f"\ttabela: {num_operado} Melhor Tempo: {record}")

d.clear()
d.close()

