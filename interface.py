from PySimpleGUI import PySimpleGUI as sg
from datetime import datetime, timedelta

    ## Função para automatizar o dia
def dia():

    date = datetime.today()
    data = date.strftime("%d_%m_%Y")
    dia = date.strftime("%d")
    mes = date.strftime("%m")
    ano = date.strftime("%Y")
    return data,dia,mes,ano
    ## Função para gerar a tela inicial
def abrir_janela_inicial():
    ## LAYOUT
    sg.theme('Reddit')
    tela_inicial = [[sg.Button('Despesas', size = (20,1)), sg.Button('Cadastrar Despesa', size = (22,1))],
                    [sg.Button('Estoque', size = (20,1)), sg.Button('Cadastrar Entrada de Produto', size = (22,1))],
                    [sg.Button('Sobrando', size = (20,1)), sg.Button('Cadastrar Saida de Produto', size = (22,1))]]

    ## Inicial
    janela_inicial = sg.Window('INICAL', tela_inicial)
    ## Janela INICIAL
    while True:
        eventos, valores = janela_inicial.read()
        if eventos == "Exit" or eventos == sg.WIN_CLOSED:
            break
        if eventos == 'Cadastrar Entrada de Produto':
            abrir_janela_cadastrar_entrda_de_produto()
        if eventos == 'Cadastrar Despesa':
            abrir_janela_cadastrar_despesa()
        if eventos == 'Cadastrar Saida de Produto':
            abrir_janela_cadastrar_saida_de_produto()
    ## Função para gerar a tela entrada de produtos
def abrir_janela_cadastrar_entrda_de_produto():
    data,d,m,a = dia()
    cadastro_produto = [
                        [sg.Text('Produto'), sg.Input(key = 'produto', size = (20,1))],
                        [sg.Text('Quantidade'), sg.Input(key = 'quantidade', size = (20,1))],
                        [sg.Text('Data'),sg.Input(d,key = 'dia', size = (3,1)),sg.Text('/'),sg.Input(m,key = 'mes', size = (3,1)),sg.Text('/'),sg.Input(a,key = 'ano', size = (5,1))],
                        [sg.Button('Gravar')]
                       ]
    ## Cadastrar Produto
    janela_cadastrar_produto = sg.Window('Tela de gravar produto', cadastro_produto)
    while True:
        eventos,valores = janela_cadastrar_produto.read()
        if eventos == "Exit" or eventos == sg.WIN_CLOSED:
            break
        if eventos == 'Gravar':
            if valores['produto'] == "":
                print("Insira o nome do produto")
            elif valores['quantidade'] == "":
                print("Insira a quantidade")
            elif valores['quantidade'].isdigit() == False:
                print("Valor quantidade invalido: "+valores['quantidade'])
            elif valores['dia'].isdigit() == False == False  or valores['mes'].isdigit() ==False  or valores['ano'].isdigit() == False:
                print('valor da data invalido')
            elif int(valores['dia']) > 31 or int(valores['dia']) < 0  or int(valores['mes']) > 12 or int(valores['mes']) < 0  or int(valores['ano']) < 0:
                print('valor da data invalido')
            else:
                print('Cadastrar Produto')
                print('Produto cadastrado')
                janela_cadastrar_produto.close()
    ## Função para gerar a tela entrada de despesas
    ## Função para gerar a tela entrada de despesas
def abrir_janela_cadastrar_despesa():
    data,d,m,a = dia()
    cadastro_despesa = [
                        [sg.Text('Despesa'), sg.Input(key = 'despesa', size = (20,1))],
                        [sg.Text('Valor'), sg.Input(key = 'valor', size = (20,1))],
                        [sg.Text('Data'),sg.Input(d,key = 'dia', size = (3,1)),sg.Text('/'),sg.Input(m,key = 'mes', size = (3,1)),sg.Text('/'),sg.Input(a,key = 'ano', size = (5,1))],
                        [sg.Button('Gravar')]
                       ]
    ## Cadastrar Produto
    janela_cadastrar_despesa = sg.Window('Cadastrar Despesa', cadastro_despesa)
    while True:
        eventos,valores = janela_cadastrar_despesa.read()
        if eventos == "Exit" or eventos == sg.WIN_CLOSED:
            break
        if eventos == 'Gravar':
            if valores['despesa'] == "":
                print("Insira o nome da Despesa")
            elif valores['valor'] == "":
                print("Insira a valor")
            elif valores['valor'].isdigit() == False:
                print("Valor quantidade invalido: "+valores['valor'])
            elif valores['dia'].isdigit() == False == False  or valores['mes'].isdigit() ==False  or valores['ano'].isdigit() == False:
                print('valor da data invalido')
            elif int(valores['dia']) > 31 or int(valores['dia']) < 0  or int(valores['mes']) > 12 or int(valores['mes']) < 0  or int(valores['ano']) < 0:
                print('valor da data invalido')
            else:
                print('Cadastrar Despesa')
                print('Despesa cadastrada')
                janela_cadastrar_despesa.close()
#def abrir_janela_cadastrar_saida_de_produto():
abrir_janela_inicial()
