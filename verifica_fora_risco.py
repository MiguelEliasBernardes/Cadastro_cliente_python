

def fora_risco():
    contador_clientes= 0
    with open('C:/Users/MIDIA/Desktop/t/aulas_python/verifica_idade/banco.txt', 'r') as banco:
        print("Clientes fora de risco")
        for lista in banco.readlines():
            l = lista.split(',')
            nome_cliente = ("Nome: ",l[2])
            email_cliente = ("Email: ",l[3])
            telefone_cliente =("Telefone: ",l[6])
            idade_cliente = (int(l[8]))
            contador_clientes += 1
            if idade_cliente < 65:
                print(f"ID: {contador_clientes} - ", "".join(nome_cliente).replace("'",""), "|" ,
                    "".join(email_cliente).replace("'",""), "|", "".join(telefone_cliente).replace("'",""),"|",
                    "Idade:","".join(str(idade_cliente)).replace("'",""))
            else:
                pass
