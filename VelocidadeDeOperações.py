import random
import time
import datetime
import shelve


def mostra_a_cola():
    """
    Procedimento para mostrar uma cola talvez ajude na memorização.
    """
    for c in ordered_list:
        print(c, "=", eval(c))


# Área shelve

def guardar_records(tempo_feito):
    """
    Guarda no objeto shelve o novo record
    """
    if chave not in d:
        d[chave] = [tempo_feito]
    else:
        data = d[chave]
        data.append(tempo_feito)
        d[chave] = data


def clear_all_records():
    """Apagar todos os records"""
    d.clear()


def clear_day_records():
    del d[chave]


def verificar_todos_os_tempo():
    try:
        print("\nResultados de tempo!!")
        for c in d.keys():
            print(f"Dia {c}")
            for x in d[c]:
                print('\t\t', x)

    except KeyError:
        print("Nenhum registro!")


d = shelve.open("registro")
chave = str(datetime.datetime.now().strftime("%d-%m"))
lista = []

for n1 in range(7, 7 + 1):
    for n2 in range(1, 10 + 1):
        expression = f"{n1}+{n2}"
        lista.append(expression)

ordered_list = lista[:]

while True:
    flag = input("""
Continuar:                  Qualquer Tecla
Sair                        'x'
Verificar tempos            'v'
Resetar Tudo                'f'
Resetar Dia                 'd'
-------------------------
Escolha: """)

    match flag:
        case 'x':
            break
        case 'v':
            verificar_todos_os_tempo()
            continue
        case 'f':
            clear_all_records()
            continue
        case 'd':
            clear_day_records()
            continue
    print("Iniciando... ")

    mostra_a_cola()

    time.sleep(3)
    print("\n" * 40)

    random.shuffle(lista)

    acertos = 0
    erros = 0
    start = time.time()

    for num in lista:
        # Em caso de digitar alguma coisa que não seja número repete o trecho indefinidamente
        resultado = ''
        while True:
            try:
                resultado = input(f"{num} = ")
                int(resultado)
            except ValueError:
                continue
            else:
                break

        # incrementa erro ou acerto
        if int(resultado) == eval(num):
            acertos += 1
        else:
            erros += 1

    end = time.time()

    time_record = f"{end - start:.2f}"

    print("\n" * 40)

    print(f"Acertos: {acertos}\nErros: {erros}\nTempo: {time_record}\n\n")

    if erros == 0:
        op = input("Salvar, Qualquer tecla para continuar / n [não]: ")
        if op != 'n':
            guardar_records(time_record)
    else:
        print("Com erros sem tempo salvo!")
d.close()
