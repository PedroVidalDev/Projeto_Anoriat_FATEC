import os
import datetime
import sqlite3
import pytz
import functions
import time

logged = False

while True:
    
    prin = str("\033" + functions.color()[0])
    
    # MENU DE OPCOES PARA O USUARIO OU ADM #
    print(f''' {prin}
  _____           _      _                                    _       _   
 |  __ \         (_)    | |            /\                    (_)     | |  
 | |__) | __ ___  _  ___| |_ ___      /  \   _ __   ___  _ __ _  __ _| |_ 
 |  ___/ '__/ _ \| |/ _ \ __/ _ \    / /\ \ | '_ \ / _ \| '__| |/ _` | __|
 | |   | | | (_) | |  __/ || (_) |  / ____ \| | | | (_) | |  | | (_| | |_ 
 |_|   |_|  \___/| |\___|\__\___/  /_/    \_\_| |_|\___/|_|  |_|\__,_|\__|
                _/ |                                                      
               |__/                                                  {prin}''')
    # CASO ELE NAO ESTEJA LOGADO #
    if logged == False:
        print('''
        [E] Entrar no sistema
        [R] Registrar no sistema
        [S] Sair do programa
        ''')

    # CASO ELE ESTIVER LOGADO NO SISTEMA #
    else:

        # SE ELE FOR O ADMINISTRADOR #
        if user[0] == 1:
            print(f'''
            Você está logado como: \033[1;32mADMINISTRADOR{prin}

            [C] Consultar e relatório de produtos
            [A] Adicionar produtos
            [X] Remover produtos
            [Q] Atualizar estoque
            [T] Temas Personalizados
            [L] Logoff
            [U] Excluir conta
            [S] Sair do programa
            ''') 
        
# SE ELE FOR USUARIO COMUM #
        else:
            print(f'''
            Você está logado como: \033[1;32mUSUÁRIO{prin} 

            [C] Consultar e relatório de produtos
            [T] Temas Personalizados
            [L] Logoff
            [S] Sair do programa
            ''')     

    try:
        esc = input("Digite a opção desejada: \033[1;32m").upper()

    except:
        print("Escolha invalida...")
        break
        
# MOSTRANDO UM RELATÓRIO DOS PRODUTOS PARA O USUARIO #

    match esc:
        case "C":
            if logged == True:
                data_atual = datetime.date.today() #bigas esteve aq
                hora_h = datetime.datetime.now(pytz.utc)
                hora_atual = hora_h.astimezone(pytz.timezone('America/Sao_Paulo'))
                hora_atual = hora_atual.strftime("%H:%M:%S")
                
                while True:
                    print(f'\n{prin}-------------------------Relatório de produtos adicionados-------------------------')
                    print(f"Gerado em:\033[1;32m {data_atual}")
                    print(f"{prin}Horário:\033[1;32m {hora_atual}{prin}\n")

                    print(f"{'=-' * 20}")
                    
                    relatorio = functions.relatorio()
                    for i in range(len(relatorio)):
                        print(f"ID: \033[1;32m {relatorio[i][0]}")
                        print(f"{prin}Nome: \033[1;32m {relatorio[i][1]}")
                        print(f"{prin}Preço: \033[1;32mR$ {relatorio[i][2]}")
                        print(f"{prin}Quantidade: \033[1;32m {relatorio[i][3]} unidade(s)")
                        print(f"{prin}=-"*20)

                    print('''
        [1] Mostrar novamente
        [2] Voltar ao menu principal\n''')
                    esc2 = int(input("Digite a opcao desejada: \033[1;32m"))
                        
                    if esc2 == 1:
                        print("\n...\n")
                        
                    elif esc == 2:
                        break 
                    else:
                        print("Opção inválida. Voltando ao início.")
                        break
            else:
                print(f"\n \033[1;31m Logue no sistema para realizar tal operacao. {prin}")
    
# SISTEMA DE LOGIN PARA O USUARIO #
        case "E":
            while True:  

                if logged == True:
                    print("Usuario já logado no sistema.")
                    break

                else:      
                    print(f"{prin}\nPerfeito, entao agora digite os seguintes dados...\n")
                    email = input("Email: \033[1;32m")
                    password = input(f"{prin}Senha: \033[1;32m")
                    
                    user = functions.login(email, password)

                    if user is None:
                        
                        print(f'''\033[31m \nUsuario nao encontrado, gostaria de tentar novamente? {prin} \n
                        [1] Tentar novamente
                        [2] Voltar ao menu principal''')
                        try:
                            esc2 = int(input("\nDigite a opcao desejada:\033[1;32m "))
                        except:
                            print(f"{prin}\033[1;31m\nOpção inválida\n\n...Voltando para o menu inicial")
                            break
                        else:
                            if esc2 == 1:
                                print("\n...")
                        
                            elif esc2 == 2:
                                break
                            else:
                                print(f"{prin}\033[1;31m\nOpção inválida\n\n...Voltando para o menu inicial")
                                break

                    else:
                        if user[3] == password:
                            logged = True
                            print("Voce foi logado no sistema!")
                            break
                        else:
                            print(f"{prin}\033[1;31mSenha incorreta...")
        
# SISTEMA DE REGISTRO PARA O USUARIO #
        case "R":
            while True:

                if logged == True:
                    print("Usuario ja logado..")
                    break

                else:
                    print(f"{prin}\nOk! Entao agora digite os seguintes dados para registro...\n")
                    name = input("Digite seu nome:\033[1;32m ")
                    email = input(f"{prin}Digite seu email:\033[1;32m ")
                    password = input(f"{prin}Digite a senha desejada:\033[1;32m ")
                    confirm_password = input(f"{prin}Confirme a senha anterior:\033[1;32m ")
                            
                    if password == confirm_password:

                        functions.register(name, email, password)

                        print("\nUsuario registrado com sucesso!")
                        break
                            
                    else:
                        print(f'''\n \033[1;31m Ocorreu algum erro na confirmacao dos dados... Gostaria de tentar novamente? {prin} \n
                    [1] Tentar novamente
                    [2] Voltar ao menu principal''')
                        esc2 = int(input("\nDigite a opcao desejada:\033[1;32m "))
                                
                        
                        if esc2 == 1:
                            print("\n...")
                                
                        else:
                            break
                
# SISTEMA DE ADICIONAR PRODUTO PARA O ADMIN #
        case "A":   
            while True:
                if logged == True:
                    if user[0] == 1:
                        try:
                            name = input(f"\n{prin}Digite o nome do produto:\033[1;32m ")
                            price = float(input(f"{prin}Digite o preço do produto: R$ \033[1;32m "))
                            qnt = int(input(f"{prin}Digite a quantidade de produtos disponíveis: \033[1;32m"))
                        except:
                            print(f'''\033[1;31mOcorreu algum erro na confirmacao dos dados... Gostaria de tentar novamente? {prin}
                            [1] Tentar novamente
                            [2] Voltar ao menu principal''')

                            try: 
                                esc2 = int(input("Digite a opcao desejada:\033[1;32m "))
                            except:
                                print(f"{prin}\033[1;31m Opção inválida")
                            if esc2 == 1:
                                print("...")
                                
                            else:
                                break
                        else:
                            
                            functions.product_add(name, price, qnt)

                            print("\nProduto registrado com sucesso!")
                            break
                    else:
                        print("...")
                else:
                    print(f"\033[1;31m\nVoce não tem permissão para tal função...{prin}")
                    break

# ALTERAR QUANTIDADE DE PRODUTO   
        case "Q":
            while True:
                if user[0] == 1:
                    relatorio = functions.relatorio()
                    for i in range(len(relatorio)):
                        print(f"{prin}ID: \033[1;32m {relatorio[i][0]}")
                        print(f"{prin}Nome: \033[1;32m {relatorio[i][1]}")
                        print(f"{prin}Preço: \033[1;32mR$ {relatorio[i][2]}")
                        print(f"{prin}Quantidade: \033[1;32m {relatorio[i][3]} unidade(s)")
                        print(f"{prin}=-"*20)
                    try:
                        id = int(input(f"{prin}Digite o ID do produto que deseja realizar a alteração de estoque: \033[1;32m"))
                        qnt = int(input(f"{prin}Agora diga para qual qnt. será alterada: \033[1;32m"))
                    except:
                        print(f"\n\033[1;31mErro na inserção de dados.. Voltando ao menu inicial...{prin}")
                        break
                    else:
                        res = functions.actualize(id, qnt)
                        print(f"{prin}{res}")
                        break
                else:
                    print(f"\033[1;31mVoce não tem permissão para tal função.. {prin}")
    
# CASO O ADM QUEIRA RETIRAR PRODUTOS #
        case "X":
            while True:
                if logged == True:
                    if user[0] == 1:
                        relatorio = functions.relatorio()
                        for i in range(len(relatorio)):
                            print(f"{prin}ID: \033[1;32m {relatorio[i][0]}")
                            print(f"{prin}Nome: \033[1;32m {relatorio[i][1]}")
                            print(f"{prin}Preço: \033[1;32mR$ {relatorio[i][2]}")
                            print(f"{prin}Quantidade: \033[1;32m {relatorio[i][3]} unidade(s)")
                            print(f"{prin}=-"*20)
                            
                        product_removed = input(f"{prin}\n Digite o ID do produto para ser removido:\033[1;32m ")

                        product = functions.finder(product_removed)

                        if product is None:
                            print(f'''\033[1;31mO produto nao foi encontrado... Gostaria de tentar novamente? {prin}
                                [1] Tentar novamente
                                [2] Voltar ao menu principal''')

                            esc2 = int(input("Digite a opcao desejada:\033[1;32m "))
                            if esc2 == 1:
                                print("...")
                                    
                            elif esc2 == 2:
                                break
                        else:
                            
                            functions.product_remove(product_removed)

                            print(f"\033[1;32mProduto deletado com sucesso!{prin}")
                            break

                    else:
                        print("...")
                else:
                    print(f"\033[1;31mVoce nao tem permissao para tal funcao...{prin}")
                    break
                    
# CASO O ADM QUERIA MUDAR O LAYOUT DO SITE #
        case "T":
            
            while True:                        
                    print(f''' {prin}
                    [1] Ciano
                    [2] Branco
                    [3] Amarelo
                    [4] Vermelho
                    [5] Rosa
                    ''')
                                
                    esc3 = int(input("Digite a opcao desejada: \033[1;32m"))
                        
                    if esc3 == 1:
                        functions.layout("Cyan", "[36m")
                        print ('\n \033[1;37;46m'+'Tema Ciano\033[0m\n'+'\033[1;36m')
                        break
                    elif esc3 == 2:
                        functions.layout("White", "[0m")
                        print ('\n \033[00m \033[40m' +'Tema Branco'+'\033[0m\n')
                        break
                    elif esc3 == 3:
                        functions.layout("Yellow", "[33m")
                        print ('\n \033[1;37;43m' +'Tema Amarelo'+'\033[0m\n'+'\033[33m')
                        break
                    elif esc3 == 4:
                        functions.layout("Red", "[31m")
                        print ('\n \033[1;37;41m' +'Tema Vermelho'+'\033[0m\n'+'\033[31m')
                        break
                    elif esc3 == 5:
                        functions.layout("Pink", "[35m")
                        print ('\n \033[1;37;45m' +'Tema Rosa'+'\033[0m\n'+'\033[1;35m')
                        break
                    else:
                        print("Escolha invalida.")
                    time.sleep(1)

# CASO O USUARIO QUEIRA SE DESLOGAR DA CONTA ATUAL #
        case "L": 
            print(f'\n \033[1;33m'+'Realizando logoff...'+'\n')
            logged = False
        
        case "U":
            if logged == True and user[0] == 1:
                users = functions.list_user()
                for i in range(len(users)):
                    print(f"{prin}ID: \033[1;32m {users[i][0]}")
                    print(f"{prin}Nome: \033[1;32m {users[i][1]}")
                    print(f"{prin}Email: \033[1;32mR$ {users[i][2]}")
                    print(f"{prin}=-"*20)

                try:
                    user_removed = int(input(f"Digite o ID da conta que deseja excluir ou digite 0 para cancelar a operação:\033[32m "))
                except:
                    print(f"\n\033[1;31mValor inserido invalido...{prin}")
                else:
                    if user_removed == 0:
                        print(f"\n{prin}Voltando ao menu inicial...")
                    elif user_removed == 1:
                        print(f"\n{prin}Não é possível excluir a conta de ADM.")
                    else:
                        functions.account_remove(user_removed)
                        print(f"\n{prin}Usuario excluído com sucesso.")
                
            else:
                print(f"\n\033[1;31mVocê não tem permissão.{prin}")

# CASO O USUARIO QUEIRA SAIR #
        case "S":
            print("\n\033[1;36;40m Até logo :D\033[0m")
            exit()

# CASO DE ESCOLHA INVALIDA #
        case _:
            print(f"\n\033[1;31m Opcao invalida, por favor tente novamente...{prin}\n")
    
