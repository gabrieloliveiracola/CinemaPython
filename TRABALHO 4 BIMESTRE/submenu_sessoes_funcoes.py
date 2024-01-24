from submenu_salas_funções import*
from submenu_filmes_funcoes import*
from auxiliar import*
from datetime import*

################################################################################

def existe_sessao(dic,chave):
    if chave in dic.keys():
        return True
    else:
        return False

################################################################################

def IncluirNovaSessao(armazenamentoSalas, armazenamentoFilmes, armazenamentoSessoes):
    print("\n Incluindo nova sessão:\n")
    data=input("Digite a data (DD/MM/AAAA): ")
    horario=input("Digite o horário (HH:MM): ")
    codigoFilme=input("Digite o código do filme: ")
    if existe_filme(armazenamentoFilmes, codigoFilme):
        codigoSala=input("Digite o código da sala: ")
        if existe_sala(armazenamentoSalas, codigoSala):
            chave=(codigoFilme, codigoSala, data, horario)
            if existe_sessao(armazenamentoSessoes, chave):
                print("Essa sessão já existe.")
                pausa()
            else:
                preco = str(input("Digite o preço (R$): "))
                armazenamentoSessoes[chave]=preco
                print("Dados inseridos.")
                pausa()
        else:
            print("A sala não existe.")
            pausa()
    else:
        print("O filme não existe.")
        pausa()
################################################################################
def consultarSessao(codigoFilme, codigoSala, armazenamentoSalas, armazenamentoFilmes, armazenamentoSessoes, data, hora):
    if existe_filme(armazenamentoFilmes, codigoFilme):
        if existe_sala(armazenamentoSalas, codigoSala):

            chave = (codigoFilme, codigoSala, data, hora)
    
            if existe_sessao(armazenamentoSessoes,chave):
        
                dados = armazenamentoSessoes[chave]

                print("Dados da sessão:")
                print("-----------------\n")

                # Mostrando os dados da sala:
                print("Sala:")
                print("-------")
                consultarSala(armazenamentoSalas, codigoSala)
                print()

                # Mostrando os dados do filme:
                print("Filme:")
                print("-------------")
                consultarFilme(armazenamentoFilmes, codigoFilme)
                print()

                # Exibindo os dados da sessão:
                print("Sessão:")
                print("-------------")
                print(f"Data: {chave[2]}")
                print(f"Horário: {chave[3]}")
                print(f"Preço: {dados}")
                print()
        
            else:

                # A sessão informada não existe!!
                print("A sessão informada não existe")
        else:
            print("A sala não existe.")
            pausa()
    else:
        print("O filme não existe.")
        pausa()
######################################################################
def excluirSessao(codigoFilme, codigoSala, armazenamentoSalas, armazenamentoFilmes, armazenamentoSessoes, data, hora):
    if existe_filme(armazenamentoFilmes, codigoFilme):
        if existe_sala(armazenamentoSalas, codigoSala):
            chave = (codigoFilme, codigoSala, data, hora)   
    
    # Verifica se a chave informada existe no dicionário:
    
            if existe_sessao(armazenamentoSessoes,chave):

                # Exibe os dados relativos a essa sessão:
                consultarSessao(codigoFilme, codigoSala, armazenamentoSalas, armazenamentoFilmes, armazenamentoSessoes, data, hora)

                # Pede confirmação para permitir alteração:
                confirma = input("Tem certeza que deseja apagar? (S/N): ").upper()
        
                if confirma == 'S':

                    # Apaga esta chave no dicionário:
                    del armazenamentoSessoes[chave]
       
                    print("Dados apagados com sucesso!")
                    pausa()
            
                else:

                    # Usuário desistiu de apagar dados:
                    print("Exclusão cancelada!")
                    pausa()

            else:

                # A sessao informada não existe!
                print("Esta sessão não está cadastrada!")
                pausa()
        else:
            print("A sala não existe.")
            pausa()
    else:
        print("O filme não existe.")
        pausa()

#########################################################################
def alteraSessao(codigoFilme, codigoSala, armazenamentoSalas, armazenamentoFilmes, armazenamentoSessoes, data, hora):
    if existe_filme(armazenamentoFilmes, codigoFilme):
        if existe_sala(armazenamentoSalas, codigoSala):
            chave = (codigoFilme, codigoSala, data, hora)   

            if existe_sessao(armazenamentoSessoes, chave):
                consultarSessao(codigoFilme, codigoSala, armazenamentoSalas, armazenamentoFilmes, armazenamentoSessoes, data, hora)
                confirma = input("Tem certeza que deseja alterá-la? (S/N): ").upper()
                if confirma == 'S':
                    preco = input("Digite o novo preço da sessão (R$):")                     
                    armazenamentoSessoes[ chave ] = preco
                    print("Dados alterados com sucesso!")
                    pausa()
                    
                else:
                    print("Alteração cancelada!")
                    pausa()

            else:
                print("Esta sessão não está cadastrada!")
                pausa()
        else:
            print("A sala não existe.")
            pausa()
    else:
        print("O filme não existe.")
        pausa()
#########################################################################
def exibirSessoeS(armazenamentoSalas, armazenamentoFilmes, armazenamentoSessoes):

    # Exibe cabecalho do relatório:
    print("Exibindo todas as sessões:")
    print("----------------------------\n")
    
    # Vamos percorrer todas as chaves no dicionário:
    
    for chave in armazenamentoSessoes:

        # Pega os dados dessa chave:
        codigoFilme = chave[0]
        codigoSala = chave[1]
        data = chave[2]
        hora = chave[3]

        # Exibe os dados da sessão:
        consultarSessao(codigoFilme, codigoSala, armazenamentoSalas, armazenamentoFilmes, armazenamentoSessoes, data, hora)

        print("----------------------------\n")

    ##fim do for

    print("")
    pausa()
############################################################################
def grava_sessoes(armazenamentoSessoes):

    # Abre o arquivo para gravação:
    arq = open("sessoes.txt", "w")

    for chave in armazenamentoSessoes:

        codigoFilme = chave[0]
        codigoSala = chave[1]
        data = chave[2]
        hora = chave[3]

        value = armazenamentoSessoes[chave]


        preco = str( value )

        linha = codigoFilme+";"+codigoSala+";"+data+";"+hora+";"+preco+"\n"

        arq.write(linha)


    arq.close()

###########################################################################
def recupera_sessoes(armazenamentoSessoes):

    if ( existe_arquivo("sessoes.txt") ):

        arq = open("sessoes.txt", "r")

        for linha in arq:


            linha = linha[:len(linha)-1]


            lista = linha.split(";")


            codigoFilme = lista[0]
            codigoSala = lista[1]
            data = lista[2]
            hora = lista[3]
            preco = lista[4]


            chave = (codigoFilme, codigoSala, data, hora)

            armazenamentoSessoes[chave] = preco

########################################################################
def relatorio(armazenamentoSalas, armazenamentoFilmes, armazenamentoSessoes, X, Y):

    # Exibe cabecalho do relatório:
    print("Relatório: Sessões entre", X, " e ", Y)
    print("---------------------------------------------\n")
    
    # Vamos percorrer todas as chaves no dicionário:

    for chave in armazenamentoSessoes:


        data = str(chave[2])
        datatime = datetime.strptime(data, '%d/%m/%Y')


        # Verifica se o ano de ingresso está entre X e Y:

        if ( datatime >= X and datatime <= Y ):

            # Esta lotação está nos limites pedidos.
            # Exibe os dados.

            # Pega os dados dessa chave:
            codigoFilme = chave[0]
            codigoSala = chave[1]
            data = chave[2]
            hora = chave[3]

            # Exibe os dados da lotação:
            consultarSessao(codigoFilme, codigoSala, armazenamentoSalas, armazenamentoFilmes, armazenamentoSessoes, data, hora)

            print("----------------------------\n")

        ##fim do if, se não se enquadra nos limites, não faz nada!

    ##fim do for

    print("")
    pausa()

############################################################################

def menuSessoes(armazenamentoSalas, armazenamentoFilmes, armazenamentoSessoes):
    opcao = ""
    # Laço para exibição do menu de opções:
    while ( opcao != "6" ):
        print("\nSubmenu Sessões\n")
        print("1 - Inserir sessão")
        print("2 - Apagar sessão")
        print("3 - Consultar sessão")
        print("4 - Listar todas as sessões")
        print("5 - Alterar")
        print("6 - Finalizar")
        opcao = input("\nDigite a opção desejada:")
        while ( opcao not in "123456" or len(opcao)!=1 ):
            print("ERRO!!! opção inválida!!")
            opcao = input("\nDigite a opção desejada:")
        if ( opcao == "1" ):
            IncluirNovaSessao(armazenamentoSalas, armazenamentoFilmes, armazenamentoSessoes)

        elif opcao == "2":
            print("Remover sessão:")
            codigoF = input("Digite o código do filme: ")
            codigoS = input("Digite o código da sala: ")
            data = input("Digite a data (DD/MM/AAAA): ")
            hora = input("Digite o horário (HH:MM)")
            excluirSessao(codigoF, codigoS, armazenamentoSalas, armazenamentoFilmes, armazenamentoSessoes, data, hora)
        elif opcao == "3":
            print("Consultar sessão:")
            codigoF = input("Digite o código do filme: ")
            codigoS = input("Digite o código da sala: ")
            data = input("Digite a data (DD/MM/AAAA): ")
            hora = input("Digite o horário (HH:MM): ")
            consultarSessao(codigoF, codigoS, armazenamentoSalas, armazenamentoFilmes, armazenamentoSessoes, data, hora)
            pausa()
        elif opcao == "4":
            exibirSessoeS(armazenamentoSalas, armazenamentoFilmes, armazenamentoSessoes)
        elif opcao == "5":
            print("Alterar sessão:")
            codigoF = input("Digite o código do filme: ")
            codigoS = input("Digite o código da sala: ")
            data = input("Digite a data (DD/MM/AAAA): ")
            hora = input("Digite o horário(HH:MM): ")
            alteraSessao(codigoF, codigoS, armazenamentoSalas, armazenamentoFilmes, armazenamentoSessoes, data, hora)
        elif opcao == "6":
            # Se escolheu sair, grava os dados no arquivo.
            grava_sessoes(armazenamentoSessoes)
            

