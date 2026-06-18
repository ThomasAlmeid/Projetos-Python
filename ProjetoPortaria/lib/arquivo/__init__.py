import json
from rich import print

def arquivoExiste(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        with open (nome, 'w+') as arquivo:
            json.dump([], arquivo)
    except:
        print('Houve Erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerArquivo(nome):
    try:
        with open(nome, 'r') as arquivo:
            dados = json.load(arquivo)
            return dados
    except:
        return []


def salvarArquivo(nome, dados):
    try:
        with open(nome, 'w') as arquivo:
            json.dump(dados, arquivo)
    except:
        print("Erro ao salvar arquivo")
    else:
        print('Aqruivo salvo com sucesso')

print(f"[red] teste [/]")