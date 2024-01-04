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
        print(c, "=", eval(c))


# Área shelve

def clear():
    if platform.system() == "Linux":
        os.system("clear")
    else:
        os.system("cls")


def guardar_records(tempo_feito):
    """
    Guarda no objeto shelve o novo record
    """

    def salvar(key, info):
        data_shell = d[key]
        data_shell.append(info)
        d[key] = data_shell

    d = shelve.open("registro")
    if 'tudo' not in d:
        d['tudo'] = [tempo_feito]

    if chave not in d:
        d[chave] = [tempo_feito]
    else:
        if tempo_feito not in d[chave]:  # evita tempos repetidos
            salvar(chave, tempo_feito)
            salvar('tudo', tempo_feito)

    d.close()


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
        for c in d.keys():
            if c != 'tudo':
                print(f"Dia {c}")
                for x in d[c]:
                    print('\t\t', x)
    except KeyError:
        print("Nenhum registro!")

    input("\nPressione Qualquer Tecla Para Continuar")
    clear()

    d.close()


def verificar_records():
    clear()
    d = shelve.open("registro")

    if 'tudo' in d:
        records = [float(x) for x in d['tudo']]

        print(f"Menor Tempo: {min(records)}")
        print(f"Maior Tempo: {max(records)}")

        input("Pressione Qualquer Tecla Para Continuar")
    else:
        print("Nothing!")
        input("Pressione Qualquer Tecla Para Continuar")

    d.close()

    clear()


# noinspection PyUnboundLocalVariable
def normal_game():
    print("Iniciando...\n")
    mostra_a_cola()
    time.sleep(2.5)
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
                guardar_records(time_record)
            clear()
        else:
            print("Com erros sem tempo salvo!")


def endlessMode():
    print("""
Tentando melhorar a precisão
Para 'sair' do modo digite sair ou 'Sair'
    """)

    flag = ''
    while flag != 'sair' or flag != "Sair":
        random.shuffle(lista)

        resultado = True
        for num in lista:
            while True:
                try:
                    resultado = input(f"{num} = ")
                    if int(resultado) == eval(num):
                        break
                except ValueError:
                    continue

            clear()


chave = str(datetime.datetime.now().strftime("%d-%m"))
lista = []

for n1 in range(7, 7 + 1):
    for n2 in range(1, 10 + 1):
        expression = f"{n1}+{n2}"
        lista.append(expression)

ordered_list = lista[:]

while True:
    resultado = ''
    flag = input(f"""
Continuar:                  Qualquer Tecla [normal game]
Endless Mode                1
Sair                        2
Verificar tempos            3
Resetar Tudo                4
Resetar Dia                 5
Verificar records           6
-------------------------
Escolha: """)

    clear()
    match flag:
        case '1':
            endlessMode()
            break
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
            verificar_records()
            continue
        case _:
            normal_game()
            break
