from lib.arquivo import *
from lib.interface import *
from rich.panel import Panel
from rich import print
from datetime import datetime
data = datetime.now()

def cadastrar_morador(lista_edificio, arquivo):
    morador = {}
    apartamento = leiaInt('Digite o número do apartamento: ')
    for m in lista_edificio:
        if apartamento == m['Apartamento']:
            print('Erro! Apartamento já cadastrado')
            break
    else:
        morador['Nome'] = leiaStr(f'Digite o nome do morador: ')
        morador['Apartamento'] = apartamento
        morador['Encomendas'] = []
        lista_edificio.append(morador)
        salvarArquivo(arquivo, lista_edificio)
        print(f'[blue] Morador [red on white] {morador["Nome"]} [/] cadastrado com sucesso.[/]')


def listar_moradores(lista):
    if not lista:
        print(f'[red] ERRO! Não há moradores cadastrados. [/]')
        return

    for morador in lista:
        conteudo = f'Morador: {morador["Nome"]}'
        ficha = Panel(conteudo, title=f" Apartamento {morador['Apartamento']} ", width=30)
        print(ficha)


def criar_encomenda(lista_edificio, arquivo):
    nova_encomenda = {}
    apartamento = leiaInt('Digite o número do apartamento: ')
    for m in lista_edificio:
        if apartamento == m['Apartamento']:
            print(f'[blue] Morador [red on white] {m["Nome"]} [/] encontrado. [/]')
            num_encomenda = leiaInt('Digite o número da encomenda: ')
            for e in m['Encomendas']:
                if e['Numero'] == num_encomenda:
                    print(f'[red] ERRO! Encomenda já cadasrtrada. [/]')
                    break
            else:
                nova_encomenda['Transportadora'] = leiaStr('Transportadora: ')
                nova_encomenda['Numero'] = num_encomenda
                nova_encomenda['Status'] = 'PENDENTE'
                nova_encomenda['Recebida'] = data.strftime("%d/%m/%Y %H:%M")
                nova_encomenda['Retirada'] = None
                nova_encomenda['Observação'] = None
                m['Encomendas'].append(nova_encomenda)
                salvarArquivo(arquivo, lista_edificio)
                print(f'[blue on white] Encomenda [yellow on white] {num_encomenda} [/] cadastrada. [/]')
            break
    else:
        print('ERRO! Apartamento não encontrado.')

def listar_encomendas(lista_edificio):
    opcao = menu(['LISTAR TODAS ENCOMENDAS', 'LISTAR ENCOMENDAS POR APARTAMENTO', 'VOLTAR'])
    if opcao == 1:
        for m in lista_edificio:
                if len(m['Encomendas']) > 0:
                    for e in m['Encomendas']:
                        print(f'AP: {m["Apartamento"]} {m["Nome"]} | Nº {e["Numero"]} | {e["Status"]}')
                else:
                    print(f'Apartamento: {m["Apartamento"]} | SEM ENCOMENDAS')
    elif opcao == 2:
        apartamento = leiaInt('Número do Apartamento: ')
        for m in lista_edificio:
            if apartamento == m['Apartamento']:
                print(f'ENCOMENDAS DE {m["Nome"]} REGISTRADAS')
                if len(m['Encomendas']) > 0:
                    for v in m['Encomendas']:
                        conteudo = f'Transportadora: {v["Transportadora"]} \nNº da encomenda {v["Numero"]} \nRecebida em: {v["Recebida"]} \nStatus: {v["Status"]}'
                        if v['Status'] == 'RETIRADA':
                            conteudo += f'\n{v["Retirada"]} \nObservação: {v["Observação"]}'
                        ficha = Panel(conteudo, title=f' Encomenda {v["Numero"]} ', width=50)
                        print(ficha, end=' ')
                else:
                    ficha = Panel(f'SEM ENCOMENDAS', title=f' APARTAMENTO {m["Apartamento"]} ', width=30)
                    print(ficha)
                break
        else:
            print('ERRO! Apartamento não encontrado.')

    elif opcao == 3:
        print('Voltando...')
        return



def registrar_retirada(lista_edificio, arquivo):
    apartamento = leiaInt('Digite o número do apartamento: ')
    for m in lista_edificio:
        if apartamento == m['Apartamento']:
            num_encomenda = leiaInt('Digite o número da encomenda: ')
            for e in m['Encomendas']:
                if num_encomenda == e['Numero']:
                    if e['Status'] == 'RETIRADA':
                        print('ERRO! Encomenda já retirada.')
                        break
                    else:
                        e['Status'] = 'RETIRADA'
                        e['Retirada'] = f'Retirada em {data.strftime("%d/%m/%Y %H:%M")}'
                        e['Observação'] = leiaStr(f'Retirada por/Obs: ')
                        salvarArquivo(arquivo, lista_edificio)
                        print(f'[blue] Encomenda [red on yellow] {e["Numero"]} [/]retirada em {data.strftime("%d/%m/%Y %H:%M")}.[/]')
                        break
            else:
                print('[red] ERRO! Encomenda não encontrada. [/]')
            break
    else:
        print('[red] ERRO! Apartamento não encontrado.[/]')
