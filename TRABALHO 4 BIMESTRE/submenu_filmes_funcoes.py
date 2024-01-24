from auxiliar import *
#FUNÇÕES
def existe_filme(dic,chave):
    if chave in dic.keys():
        return True
    else:
        return False
#FILMES
###########################
#INCLUIR
###########################
def IncluirNovoFilme(armazenamento):
    i=0
    print("\n Incluindo novo filme:\n")
    codigo=input("Digite o código: ")
    while codigo == "":
        print("Código não digitado.")
        codigo=input("Digite o código: ")
    if codigo in armazenamento:
        print("\n Filme já cadastrado \n")
    elif codigo == "":
        print("Nenhum código digitado.")
    else:
        #criar uma lista vazia
        elementos=[]
        print("Tecle <enter> caso queira terminar o cadastro.")
        nome=input("Nome:")
        anodelancamento=input("Ano de Lançamento:")
        genero=input("Gênero:")
        listadeatores=[]
        atores=input(f"Ator {i+1}(Digite <enter> para terminar a digitação de atores):")
        while atores != "":
            i=i+1
            listadeatores.append(atores)
            atores=input(f"Ator {i+1}(Digite <enter> para terminar a digitação de atores):")
        listadeatores=tuple(listadeatores)
        #se nada for digitado em nenhum dos elementos    
        if (nome == "") and (anodelancamento == "") and (genero == "") and(len(listadeatores) < 1):
            print("\n Nada digitado \n")
        else:
            elementos.append(nome)
            elementos.append(anodelancamento)
            elementos.append(genero)
            elementos.append(listadeatores)
        #garantindo que foi digitado algo
            if len(elementos)!=0:
                
                armazenamento[codigo]=elementos
                print("\n Inclusão realizada.")
            else:
                print("nada digitado.")
##################################################################
def consultarFilme(armazenamento, codigo):
    print("\n*** Consultar filme:\n")
    # Ver se o codigo existe no dicionário:
    if ( codigo in armazenamento ):
        listaFilme = armazenamento[codigo]
        print("Dados do filme ", codigo)
        if listaFilme[0] == "":
            print('NOME: Nenhum nome cadastrado.')
        else:
            print("NOME: ",listaFilme[0])
        if listaFilme[1] == "":
            print('ANO DE LANÇAMENTO: Nenhum ano de lançamento cadastrado.')
        else:
            print("ANO DE LANÇAMENTO: ",listaFilme[1])
        if listaFilme[2] == "":
            print('GÊNERO: Nenhum gênero cadastrado.')
        else:
            print("GÊNERO: ",listaFilme[2])
        if len(listaFilme[3]) == 0:
            print('ATORES: Nenhum ator cadastrado.')
        else:
            atores = ", ".join(listaFilme[3])
            print('ATORES: ', atores)
    
    else:
        print(f"{codigo} - Filme não cadastrado")
        input("Aperte ENTER para continuar")
###########################################################
###########################
def excluirFilme(armazenamento, codigo):
    # Vamos verificar se o codigo existe no dicionário:
    if ( codigo in armazenamento ):
        consultarFilme(armazenamento, codigo)
    # Vamos pedir confirmação antes de excluir:
        opc = input("\nConfirma a exclusão do filme? (S/N)?")
        if ( opc.upper() == 'S'):
            del armazenamento[codigo]
            print("Filme Removido!")
    else:
        print(f"\n{codigo} não existe!")

        input("Aperte ENTER para continuar")
###############################################################
###########################
def exibirFilmeS(armazenamento):
    print("\n*** Exibindo todos os filmes:\n")
    # Vamos percorrer todos os codigos do dicionário:
    for codigo in armazenamento:
        consultarFilme(armazenamento,codigo)
        print("--------------------")
    input("Aperte ENTER para continuar")
################################################################
###########################
def alterarFilme(armazenamento, codigo):
    if ( codigo in armazenamento):
        FilmeParaAlterar=armazenamento.get(codigo)
        opcao=""
        print("\n       ELEMENTOS: \n")
        print("     1 - NOME")
        print("     2 - ANO DE LANÇAMENTO")
        print("     3 - GÊNERO")
        print("     4 - ATORES")
        opcao=input("O que você deseja alterar?")
        while ( opcao not in "1234" or len(opcao)!=1 ):
                 print("ERRO!!! opção inválida!!")
                 opcao = input("\nDigite a opção desejada:")
        if ( opcao == "1" ):
            elemento=FilmeParaAlterar[0]
            del elemento
            novoelemento=input("    Digite o novo NOME: ")
            if (novoelemento) == "":
                print("Nada digitado")
            else:
                FilmeParaAlterar[0]=novoelemento
                print("Nome alterado!")

        if ( opcao == "2" ):
            elemento=FilmeParaAlterar[1]
            del elemento
            novoelemento=input("    Digite o novo ANO DE LANÇAMENTO: ")
            if (novoelemento) == "":
                print("Nada digitado")
            else:
                FilmeParaAlterar[1]=novoelemento
                print("Ano de lançamento alterado!")
                
        if ( opcao == "3" ):
            elemento=FilmeParaAlterar[2]
            del elemento
            novoelemento=input("    Digite o novo GÊNERO: ")
            if (novoelemento) == "":
                print("Nada digitado")
            else:
                FilmeParaAlterar[2]=novoelemento
                print("Gênero alterado!")
                
        if ( opcao == "4" ):
            elemento=FilmeParaAlterar[3]
            del elemento
            i=0
            listadeatores=[]
            novoelemento=input(f"Ator {i+1}(Digite <enter> para terminar a digitação de atores):")
            while novoelemento != "":
                i=i+1
                listadeatores.append(novoelemento)
                novoelemento=input(f"Ator {i+1}(Digite <enter> para terminar a digitação de atores):")
            listadeatores=tuple(listadeatores)
            if len(listadeatores) == 0:
                print("Nada digitado")
            else:
                FilmeParaAlterar[3]=listadeatores
                print("ATORES alterados!")
    else:
        print(f"\n{codigo} - Filme não cadastrado")
    input("Aperte ENTER para continuar")
########################################################################
def grava_filmes(armazenamento):

    arq = open("filmes.txt", "w")
    
    for codigo in armazenamento:

        tupla = armazenamento[codigo]

        atores = "#".join(tupla[3])

        linha = codigo + ";" + tupla[0] + ";" + tupla[1] + ";" + tupla[2] + ";" + atores + "\n"

        arq.write(linha)

    arq.close()

##########################################################
def recupera_filmes(armazenamento):

    if ( existe_arquivo("filmes.txt") ):

        arq = open("filmes.txt", "r")

        for linha in arq:

            linha = linha[:len(linha)-1]

            lista = linha.split(";")

            
            codigo = lista[0]
            nome = lista[1]
            ano = lista[2]
            genero = lista[3]
            atores = lista[4]

            listatores = atores.split("#")

            armazenamento[codigo] = (nome, ano, genero, listatores)

########################################################################
def menuFilmes(dicFilmes):
    opcao = ""
    # Laço para exibição do menu de opções:
    while ( opcao != "6" ):
        print("\nSubmenu Filmes\n")
        print("1 - Inserir filme")
        print("2 - Apagar filme")
        print("3 - Consultar filme")
        print("4 - Listar todos os filmes")
        print("5 - Alterar")
        print("6 - Finalizar")
        opcao = input("\nDigite a opção desejada:")
        while ( opcao not in "123456" or len(opcao)!=1 ):
            print("ERRO!!! opção inválida!!")
            opcao = input("\nDigite a opção desejada:")
        if ( opcao == "1" ):
            IncluirNovoFilme(dicFilmes)
        elif ( opcao == "2" ):
            COD=input("Digite o código do filme para apagar: ")
            excluirFilme(dicFilmes, COD)
        elif ( opcao == "3" ):
            COD=input("Digite o código do filme para consultar: ")
            consultarFilme(dicFilmes, COD)
        elif ( opcao == "4" ):
            exibirFilmeS(dicFilmes)
        elif ( opcao == "5" ):
            COD=input("Digite o código do filme para alterar: ")
            alterarFilme(dicFilmes, COD)
        elif ( opcao == "6" ):
            grava_filmes(dicFilmes)

