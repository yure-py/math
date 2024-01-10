import platform
import random
import time
import datetime
import shelve
import os

def mostra_a_cola():
    """
    Procedimento para mostrar uma cola talvez ajude na memorização.
    """
    for c in ordered_list:
        print('\t', c, "=", eval(c))

def criar_tabela():
    global lista, operador, numero_operado, ordered_list

    lista = []
    ordered_list = []

    while True:
        try:
            numero_operado = int(input("Qual número você gostaria de usar? "))

            operador = ''
            print(f"""
Escolha o operador
    [0]  +  Adição
    [1]  -  Subtração
    [2]  *  Multiplicação
--------------------------
""")
            while True:
                try:
                    operador = int(input("Escolha: "))

                    match operador:
                        case 0:
                            operador = '+'
                        case 1:
                            operador = '-'
                        case 2:
                            operador = '*'
                        case _:
                            print("\nErro!, Escolha um operador adequado!\n")
                            operador = False
                            continue

                    break
                except ValueError:
                    continue

        except ValueError:
            continue
        else:
            break

    for n1 in range(numero_operado, numero_operado+1):
        for n2 in range(1, 10 + 1):
            expression = f"{n1}{operador}{n2}"
            lista.append(expression)

    ordered_list = lista[:]
    clear()

def verifica_numero_e_operador():
    if not numero_operado:
        criar_tabela()

# Área shelve
def clear():
    if platform.system() == "Linux":
        os.system("clear")
    else:
        os.system("cls")

def clear_all_records():
    d = shelve.open("registro")

    """Apagar todos os records"""
    d.clear()
    d.close()

def clear_day_records():
    d = shelve.open("registro")
    try:
        del d[chave]
    except KeyError:
        pass
    d.close()

def verificar_todos_os_tempo():
    d = shelve.open("registro")

    try:
        print("\nResultados de tempo!!")
        d[chave]
        for c in d.keys():
            if c != 'melhores':
                print(f"Dia {c}")
                for x in d[c]:
                    print('\t\t', x)
    except KeyError:
        print("Nenhum registro!")

    input("\nPressione Qualquer Tecla Para Continuar")
    clear()

    d.close()

def salvar_progresso(tempo_feito):
    d = shelve.open("registro")
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

def guardar_historico(tempo_feito):
    tempo_feito = float(tempo_feito)

    d = shelve.open("registro")

    if 'melhores' not in d:
        d['melhores'] = {
            'Multiplicação': {1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None,10:None},
            'Subtração': {1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None,10:None},
            'Adição': {1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None,10:None}
        }

    if chave not in d:
        d[chave] = [f"Tempo: {tempo_feito} Operador: {operador} Tabela do: {numero_operado} "]
    else:
        if tempo_feito not in d[chave]:  # evita tempos repetidos
            data_shell = d[chave]
            data_shell.append(f"Tempo: {tempo_feito}    Operador: {operador}   Tabela do: {numero_operado} ")
            d[chave] = data_shell
    d.close()

def progresso_normal_game():
    d = shelve.open("registro")

    if 'melhores' not in d:
        d['melhores'] = {
            'Multiplicação': {1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None,10:None},
            'Subtração': {1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None,10:None},
            'Adição': {1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None,10:None}
        }

    print("Progresso No Normal game:\n")
    print("A medida que se joga os melhores resultados são salvos,\nComplete tudo no melhor Tempo possivel!")
    print("-----------------------------------------------------------------")

    melhores = d['melhores']
    for operacoes in melhores:
        print(operacoes)
        for num_operado in melhores[operacoes]:
            if melhores[operacoes][num_operado] is not None:
                print(f"\ttabela: {num_operado} Melhor Tempo: {melhores[operacoes][num_operado]}")

    print("-----------------------------------------------------------------")
    input("\nDigite qualquer tecla para continuar!")

    d.close()

# game mode
def normal_game():
    print("Objetivo do normal game!")
    print("Resolver a tabela de operações em 10 segundos\n")
    mostra_a_cola()

    input("\nDigite qualquer tecla para continuar!")
    clear()

    acertos = 0
    erros = 0
    random.shuffle(lista)
    start = time.time()
    for num in lista:
        # Em caso de digitar alguma coisa que não seja número repete o trecho indefinidamente
        while True:
            try:
                resultado = input(f"{num} = ")
                int(resultado)
                clear()
            except ValueError:
                continue
            else:
                break

        # Possibilidade de sair
        if resultado == '0':
            clear()
            break

        # incrementa erro ou acerto
        if int(resultado) == eval(num):
            acertos += 1
        else:
            erros += 1

    if resultado != '0':
        end = time.time()

        time_record = f"{end - start:.2f}"

        clear()

        print(f"Acertos: {acertos}\nErros: {erros}\nTempo: {time_record}\n\n")

        if erros == 0:
            op = input("Salvar, Qualquer tecla para continuar / 0 [não]: ")
            if op != '0':
                guardar_historico(time_record)
                salvar_progresso(time_record)
            clear()
        else:
            print("Com erros sem tempo salvo!")
            input("\nDigite qualquer tecla para continuar!")

def endlessMode():
    print("""
Modo para melhorar a precisão dos cálculos antes de entrar no normal game!
Para 'sair' do modo digite sair ou 'Sair'
    """)

    acertos = 0
    resposta = True

    while resposta:
        random.shuffle(lista)

        for num in lista:
            print(f"Win Streak: {acertos}")
            while resposta:
                try:
                    resposta = input(f"{num} = ")

                    if int(resposta) == eval(num):
                        acertos += 1
                        break
                    else:
                        acertos = -1

                except ValueError:
                    if resposta == 'sair' or resposta == "Sair":
                        resposta = False
                        break
                    else:
                        resposta = True
                        continue
            clear()

        if resposta == 'sair' or resposta == "Sair":
            break

chave = str(datetime.datetime.now().strftime("%d-%m"))
lista = []
ordered_list = []
numero_operado = ''
operador = ''

# main
while True:
    clear()
    resultado = ''
    flag = input(f"""
Continuar                   Qualquer Tecla [normal game]
Endless Mode                1
Sair                        2
Historico de partidas       3 [normal game]
Resetar Tudo                4
Resetar Dia                 5
Configurar operações        6
Progresso normal game       7
-------------------------
Escolha: """)

    clear()
    match flag:
        case '1':
            verifica_numero_e_operador()
            endlessMode()
            continue
        case '2':
            break
        case '3':
            verificar_todos_os_tempo()
            continue
        case '4':
            clear_all_records()
            continue
        case '5':
            clear_day_records()
            continue
        case '6':
            criar_tabela()
            continue
        case '7':
            progresso_normal_game()
            continue
        case _:
            verifica_numero_e_operador()
            normal_game()
            continue
