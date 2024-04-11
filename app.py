from datetime import datetime as dt
import verifica_fora_risco as fora
import verifica_risco as risco


def add_banco(dados):

    #conv_str = '-'.join([str(i) for i in dados])
    with open('C:/Users/MIDIA/Desktop/t/aulas_python/verifica_idade/banco.txt','a') as banco:
        banco.write(str(f"\n {dados}"))


def cria_cadastro():
    while True:
        """
        Verifica os dados de cadastro do usuário e os envia para o banco de dados
        """
        nome = input("digite o nome completo: ")
        email = input("Digite o seu email: ")
        cpf = (input("Digite o seu CPF: "))
        rg = (input("Digite o seu RG: "))
        telefone = (input("Digite o seu telefone: "))
        nascimento = (input("Digite a sua data de nascimento: dd/mm/aa "))
        

        # Calculo para verificar a idade da pessoa cadastrada
        nascimento_formatado = dt.strptime(nascimento, "%d/%m/%Y")
        nasc_ano = nascimento_formatado.year
        data_agora = dt.today()
        ano_atual = data_agora.year
        idade = ano_atual - nasc_ano

        print("-"*30)
        print(f"""
        Nome: {nome}
        email: {email})
        CPF: {cpf}
        RG: {rg}
        Telefone: {telefone}
        Data de Nascimento: {nascimento}""")
        print("-"*30)
        
        verifica_dados = input("Os dados acima estão corretos? ")
        if verifica_dados.lower() in ['sim', 's']:
            dados_clientes = ",",nome,email,cpf,rg,telefone,nascimento,idade,","
            add_banco(dados_clientes)
            break
        elif verifica_dados.lower() in ['nao','n']:
            print("Recomeçando coleta de dados!")
            cria_cadastro()
        else:
            verifica_dados= input("escolha inválida, digite s/n")
            if verifica_dados.lower() in ['sim', 's']:
                dados_clientes = ",",nome,email,cpf,rg,telefone,nascimento,idade,","
                add_banco(dados_clientes)
                break
            elif verifica_dados.lower() in ['nao','n']:
                print("Recomeçando coleta de dados!")
                cria_cadastro()



while True:

    print("""
        Escolha o que deseja fazer: 
        
        1 - Adicionar cliente
        2 - Risco
        3 - Fora de Risco

        4 - Sair  """)

    escolha = int(input("Digite o departamento desejado: "))

    if escolha == 1:
        cria_cadastro()  
    elif escolha == 2:
        print('-'*30)
        print()
        risco.verifica_risco()
        
        verifica_continua = input("Deseja voltar para a tela inicial? ")
        if verifica_continua.lower() in ['sim','s']:
            pass
        else:
            print("Fechando o sistema...")
            break
        print('-'*30)
    elif escolha == 3:
        print('-'*30)
        fora.fora_risco()
        verifica_continua = input("Deseja voltar para a tela inicial? ")
        if verifica_continua.lower() in ['sim','s']:
            pass
        else:
            print("Fechando Sistema...")
            break
        print('-'*30)
    elif escolha == 4:
        print("Fechando o sistema...")
        break
    else:
        print("Escolha uma opção válida")
        pass
    
