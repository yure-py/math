import random

num_range = 20
qtd_de_termos = 2
operadores = ["+", "-", "*", "/"]
op_operadores = 3
flag_para_negativos = 1


def gerar_numeros():
    termos = []
    for _ in range(qtd_de_termos):
        num = random.randint(0, num_range)

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

        operador = random.randint(0, op_operadores)
        expr += f'{operadores[operador]}'

    return expr


def main():
    for c in range(100):
        print(criar_expressao())

main()