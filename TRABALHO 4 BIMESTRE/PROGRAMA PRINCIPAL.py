from submenu_salas_funções import*
from submenu_filmes_funcoes import*
from submenu_sessoes_funcoes import*
from datetime import*

dic_salas = {}
dic_filmes={}
dic_sessoes={}

recupera_salas(dic_salas)
recupera_filmes(dic_filmes)
recupera_sessoes(dic_sessoes)

opc = 0
# Enquanto o usuário não escolher a opção sair

while ( opc != 5 ):

    # Exibe o menu:
        
    print("1 - Submenu de Salas")
    print("2 - Submenu de Filmes")
    print("3 - Submenu de Sessões")
    print("4 - Relatório")
    print("5 - Sair")

    # Recebe a opção do usuário:
    opc = int( input("Digite uma opção: ") )

    # Chama função, conforme opção escolhida:
    if opc == 1:
        menuSalas(dic_salas)
        print("\n\n\n\n")
    elif opc == 2:
        menuFilmes(dic_filmes)
        print("\n\n\n\n")
    elif opc == 3:
        menuSessoes(dic_salas, dic_filmes, dic_sessoes)
        print("\n\n\n\n")
    elif opc == 4:
        x = str( input("Digite a data inicial(DD/MM/AAAA):") )
        X = datetime.strptime(x, '%d/%m/%Y')
        y = str( input("Digite a data final(DD/MM/AAAA):") )
        Y = datetime.strptime(y, '%d/%m/%Y')
        relatorio(dic_salas, dic_filmes, dic_sessoes, X, Y)
        print("\n\n\n\n")
