import random

num_range_upperbound = 9999
num_range_lowerbound = 2
qtd_de_termos = 2
operadores = ["+"]
flag_para_negativos = 0
qtd_exercicios = 5


op_operadores = len(operadores) - 1

def gerar_numeros():
    termos = []
    for _ in range(qtd_de_termos):
        num = random.randint(num_range_lowerbound, num_range_upperbound)

        if random.randint(0, 3) == 2 and flag_para_negativos == 1:
            if _ == 0:
                num = -num
            else:
                num = f"(-{num})"

        termos.append(num)

    return termos


def criar_expressao():
    termos = gerar_numeros()
    expr = ""

    while termos:
        expr += f"{termos[0]}"
        termos.pop(0)

        if not termos:
            break

        if op_operadores > 2:
            operador = random.randint(1, op_operadores)
        else:
            operador = random.randint(0, op_operadores)

        expr += f'{operadores[operador]}'

    return expr


def main():
    tudo = []
    for _ in range(qtd_exercicios):
        expr = criar_expressao()
        tudo.append(expr)
        print(expr)
        
    print("\n", end="")
    input()
    for idx in range(len(tudo)):
        print(eval(tudo[idx]))

main()
