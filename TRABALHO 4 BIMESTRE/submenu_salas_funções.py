from auxiliar import *
#FUNÇÕES
def existe_sala(dic,chave):
    if chave in dic.keys():
        return True
    else:
        return False
#SALA
###########################
#INCLUIR
###########################
def IncluirNovaSala(armazenamento):
#a função cria uma nova sala usando o dicionário como parâmetro
#sendo assim, será criado um novo par no dicionário, sendo:
#CHAVE: CÓDIGO
#ELEMENTO: lista com Nome, capacidade, Tipo de exibição, Acessibilidade
    print("\n Incluindo nova sala:\n")
    codigo=input("Digite o código: ")
    while codigo == "":
        print("Código não digitado.")
        codigo=input("Digite o código: ")
    #caso o código já esteja no dicionário, então não será cadastrado.
    if existe_sala(armazenamento, codigo):
        print("Sala já cadastrada!")
        pausa()   
    else:
        #criar uma lista vazia
        elementos=[]
        print("Tecle <enter> caso queira terminar o cadastro.")
        nome=input("Nome:")
        capacidade=input("Capacidade:")
        tipo=input("Tipo de exibição:")
        acessibilidade=input("Acessibilidade:")
        #se nada for digitado em nenhum dos elementos
        if (nome or capacidade or tipo or acessibilidade) == "":
            print("Nada digitado")
        else:
            elementos.append(nome)
            elementos.append(capacidade)
            elementos.append(tipo)
            elementos.append(acessibilidade)

        #garantindo que foi digitado algo
            if len(elementos)!=0:
                armazenamento[codigo]=elementos
                print("\n Inclusão realizada.")
            else:
                print("nada digitado.")
###########################################################
###########################
#CONSULTAR SALA
###########################
def consultarSala(armazenamento, codigo):
    print("\n*** Consultar sala:\n")
    # Ver se o codigo existe no dicionário:
    if (codigo in armazenamento):
        listaSala = armazenamento[codigo]
        print("Dados da sala ", codigo)
        if listaSala[0] == "":
            print('NOME: Nenhum nome cadastrado.')
        else:
            print("NOME: ",listaSala[0])
        if listaSala[1] == "":
            print('CAPACIDADE: Nenhuma capacidade cadastrada.')
        else:
            print("CAPACIDADE: ",listaSala[1])
        if listaSala[2] == "":
            print('TIPO DE EXIBIÇÃO: Nenhum tipo de exibição cadastrado.')
        else:
            print("TIPO DE EXIBIÇÃO: ",listaSala[2])
        if listaSala[3] == "":
            print('ACESSIBILIDADE: Nenhuma acessibilidade cadastrada.')
        else:
            print("ACESSIBILIDADE: ",listaSala[3])

    else:
        print(f"{codigo} - Sala não cadastrada")
        input("Aperte ENTER para continuar")
###########################################################
###########################
#EXCLUIR SALA
###########################
def excluirSala(armazenamento, codigo):
    # Vamos verificar se o codigo existe no dicionário:
    if ( codigo in armazenamento ):
        consultarSala(armazenamento, codigo)
    # Vamos pedir confirmação antes de excluir:
        opc = input("\nConfirma a exclusão da sala (S/N)?")
        if ( opc.upper() == 'S'):
            del armazenamento[codigo]
            print("Sala Removida!")
        else:
            print("Remoção cancelada!")
    else:
        print(f"\n{codigo} não existe!")

    input("Aperte ENTER para continuar")
###############################################################
###########################
#EXIBIR SALAS
###########################
def exibirSalaS(armazenamento):
    print("\n*** Exibindo todas as salas:\n")
    # Vamos percorrer todos os codigos do dicionário:
    for codigo in armazenamento:
        consultarSala(armazenamento,codigo)
        print("--------------------")
    input("Aperte ENTER para continuar")
################################################################
###########################
#ALTERARSALA
###########################
def alterarSala(armazenamento, codigo):
    if ( codigo in armazenamento):
        SalaParaAlterar=armazenamento.get(codigo)
        opcao=""
        print("\n       ELEMENTOS: \n")
        print("     1 - NOME")
        print("     2 - CAPACIDADE")
        print("     3 - TIPO DE EXIBIÇÃO")
        print("     4 - ACESSIBILIDADE:")
        opcao=input("O que você deseja alterar?")
        while ( opcao not in "1234" or len(opcao)!=1 ):
                 print("ERRO!!! opção inválida!!")
                 opcao = input("\nDigite a opção desejada:")
        if ( opcao == "1" ):
            elemento=SalaParaAlterar[0]
            del elemento
            novoelemento=input("    Digite o novo NOME: ")
            if (novoelemento) == "":
                print("Nada digitado")
            else:
                SalaParaAlterar[0]=novoelemento
                print("Nome alterado!")

        if ( opcao == "2" ):
            elemento=SalaParaAlterar[1]
            del elemento
            novoelemento=input("    Digite a nova CAPACIDADE: ")
            if (novoelemento) == "":
                print("Nada digitado")
            else:
                SalaParaAlterar[1]=novoelemento
                print("Capacidade alterada!")
                
        if ( opcao == "3" ):
            elemento=SalaParaAlterar[2]
            del elemento
            novoelemento=input("    Digite o novo TIPO DE EXIBIÇÃO: ")
            if (novoelemento) == "":
                print("Nada digitado")
            else:
                SalaParaAlterar[2]=novoelemento
                print("Tipo de exibição alterado!")
                
        if ( opcao == "4" ):
            elemento=SalaParaAlterar[3]
            del elemento
            novoelemento=input("    Digite a nova ACESSIBILIDADE: ")
            if (novoelemento) == "":
                print("Nada digitado")
            else:
                SalaParaAlterar[3]=novoelemento
                print("Acessibilidade alterada!")
    else:
        print(f"\n{codigo} - Sala não cadastrada")
    input("Aperte ENTER para continuar")
########################################################################
def grava_salas(armazenamento):

    arq = open("salas.txt", "w")
    
    for codigo in armazenamento:

        tupla = armazenamento[codigo]

        linha = codigo+";"+tupla[0]+";"+tupla[1]+";"+tupla[2]+";"+tupla[3]+"\n"

        arq.write(linha)

    arq.close()

###########################################################################
def recupera_salas(armazenamento):

    # Verificando se o arquivo existe:
    if ( existe_arquivo("salas.txt") ):

        # Existe! Abrindo arquivo para leitura:
        arq = open("salas.txt", "r")

        # Percorrendo as linhas do arquivo:
        for linha in arq:

            # a linha é:
            # cpf;nome;datanasc;salario
            
            # Tirando o \n do final:
            linha = linha[:len(linha)-1]

            # Vamos quebrar por ;
            lista = linha.split(";")

            # cpf esta em lista[0]
            # nome está em lista[1]
            # endereço está em lista[2]
            # datanasc está em lista[3]
            # salario esta em lista[4]
            codigo = lista[0]
            nome = lista[1]
            capacidade = lista[2]
            tipoexibicao = lista[3]
            acessibilidade = lista[4]

            # Colocando os dados no dicionario:
            armazenamento[codigo] = (nome, capacidade, tipoexibicao, acessibilidade)

        ##fim do for
####################################################################################
def menuSalas(dicSalas):
    opcao = ""
    # Laço para exibição do menu de opções:
    while ( opcao != "6" ):
        print("\nSubmenu Salas\n")
        print("1 - Inserir sala")
        print("2 - Apagar sala")
        print("3 - Consultar sala")
        print("4 - Listar todas as salas")
        print("5 - Alterar")
        print("6 - Finalizar")
        opcao = input("\nDigite a opção desejada:")
        while ( opcao not in "123456" or len(opcao)!=1 ):
            print("ERRO!!! opção inválida!!")
            opcao = input("\nDigite a opção desejada:")
        if ( opcao == "1" ):
            IncluirNovaSala(dicSalas)
        elif ( opcao == "2" ):
            COD=input("Digite o código da sala para apagar: ")
            excluirSala(dicSalas, COD)
        elif ( opcao == "3" ):
            COD=input("Digite o código da sala para consultar: ")
            consultarSala(dicSalas, COD)
        elif ( opcao == "4" ):
            exibirSalaS(dicSalas)
        elif ( opcao == "5" ):
            COD=input("Digite o código da sala para alterar: ")
            alterarSala(dicSalas, COD)
        elif ( opcao == "6"):
            grava_salas(dicSalas)
