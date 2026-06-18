from lib.organizacao import *
from lib.interface import *
import os

cabeçalho('BEM VINDO AO PORTARIA ORGANIZADA')
nome_Edificio = leiaStr('Digite o nome do Edificio: ')
if not os.path.exists('dados'):
    os.mkdir('dados')
arq = os.path.join('dados',f'{nome_Edificio.replace(" ", "_")}.json')
if not arquivoExiste(arq):
    criarArquivo(arq)
edificio = lerArquivo(arq)
cabeçalho(nome_Edificio)
while True:
    opcao = menu(['CADASTRAR MORADOR','LISTAR MORADORES','CADASTRAR ENCOMENDAS','LISTAR ENCOMENDAS', 'REGISTRAR RETIRADA', 'SAIR'])
    if opcao == 1:
        cadastrar_morador(edificio, arq)
    elif opcao == 2:
        listar_moradores(edificio)
    elif opcao == 3:
        criar_encomenda(edificio, arq)
    if opcao == 4:
        listar_encomendas(edificio)
    if opcao == 5:
        registrar_retirada(edificio, arq)
    if opcao == 6:
        cabeçalho('Saindo do Sistema...')
        break

