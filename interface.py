from PySimpleGUI import PySimpleGUI as sg

def abrir_janela_inicial():
    ## LAYOUT
    sg.theme('Reddit')
    tela_inicial = [[sg.Button('Despesas', size = (20,1)), sg.Button('Cadastrar Despesa', size = (20,1))],[sg.Button('Estoque', size = (20,1)), sg.Button('Cadastrar Produto', size = (20,1))]]
    ## Inicial
    janela_inicial = sg.Window('INICAL', tela_inicial)
    ## Janela INICIAL
    while True:
        eventos, valores = janela_inicial.read()
        if eventos == "Exit" or eventos == sg.WIN_CLOSED:
            break
        if eventos == 'Cadastrar Produto':
            abrir_janela_cadastrar_produto()
        if eventos == 'Cadastrar Despesa':
            abrir_janela_cadastrar_despesa()

def abrir_janela_cadastrar_produto():
    cadastro_produto = [
                        [sg.Text('Produto'), sg.Input(key = 'produto', size = (20,1))],
                        [sg.Text('Quantidade'), sg.Input(key = 'quantidade', size = (20,1))],
                        [sg.Button('Gravar')]
                       ]
    ## Cadastrar Produto
    janela_cadastrar_produto = sg.Window('Tela de gravar produto', cadastro_produto)
    while True:
        eventos,valores = janela_cadastrar_produto.read()
        if eventos == "Exit" or eventos == sg.WIN_CLOSED:
            break
        if eventos == 'Gravar':
            if valores['produto'] != "" and valores['quantidade'] != "":
                print("Cadastrar Produto")
                print('Produto cadastrado')
                janela_cadastrar_produto.close()
            elif valores['quantidade'] == "" and valores['produto'] == "":
                print("Insira o porduto")
            elif valores['produto'] == "":
                print("Insira o nome do produto")
            elif valores['quantidade'] == "":
                print("Insira a quantidade")
def abrir_janela_cadastrar_despesa():
    cadastro_despesa = [
                        [sg.Text('Despesa'), sg.Input(key = 'despesa', size = (20,1))],
                        [sg.Text('Valor'), sg.Input(key = 'valor', size = (20,1))],
                        [sg.Button('Gravar')]
                       ]
    ## Cadastrar Produto
    janela_cadastrar_despesa = sg.Window('Cadastrar Despesa', cadastro_despesa)
    while True:
        eventos,valores = janela_cadastrar_despesa.read()
        if eventos == "Exit" or eventos == sg.WIN_CLOSED:
            break
        if eventos == 'Gravar':
            if valores['despesa'] != "" and valores['valor'] != "":
                print("Cadastrar Despesa")
                print('Despesa cadastrado')
                janela_cadastrar_produto.close()
            elif valores['valor'] == "" and valores['Despesa'] == "":
                print("Insira a Despesa")
            elif valores['Despesa'] == "":
                print("Insira o nome da Despesa")
            elif valores['valor'] == "":
                print("Insira a valor")
abrir_janela_inicial()
