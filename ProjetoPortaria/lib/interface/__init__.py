from rich import print


def linha(tam=30):
    print(''*tam)

def cabeçalho(txt):
    tamanholinha = len(txt) + 4
    print('-'*tamanholinha)
    print(f'{txt.center(tamanholinha)}')
    print('-'*tamanholinha)


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\33[0;31m ERRO! Digite um número inteiro válido.\33[m')
            continue
        except KeyboardInterrupt:
            print('\n\33[31mO usuário preferiu encerrar o programa.\33[m')
            return 0
        else:
            return n


def leiaStr(msg):
    while True:
        try:
            while True:
                s = str(input(msg)).strip().upper()
                if s.isnumeric():
                    print('\33[1;31mERRO! Digite um nome válido.\33[m')
                if s == '':
                    return f'\033[31mSEM INQUILNO\33[m'
                if not s.isnumeric():
                    break
        except KeyboardInterrupt:
            print('\n\33[1;31m PROGRAMA ENCERRADO.\33[m')
            break
        else:
            return s


def title1(msg):
    linha()
    print(msg.center(30))
    linha()


def menu(lista):
    c = 1
    for item in lista:
        print(f'\33[1;33m{c}\33[m - \33[31m{item}\33[m')
        c += 1
    linha()
    opc = leiaInt('Digite sua opção: ')
    return opc
