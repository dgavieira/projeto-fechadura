import sys, logging, sched, time, login, logout, semcadastro, opfile

def datalog():
    #configuração do logging
    logging.basicConfig(filename = 'datalog.txt', format = '%(asctime)s  %(levelname)s:  %(message)s',
                        datefmt = '%d/%m/%Y %H:%M:%S',level=logging.DEBUG)

    #ent recebe do teclado e name recebe o valor sempre em minusculas
    #lista vazia para receber a entrada do teclado
    ent = '' #garante que não tem lixo no espaço de memória
    name = '' #idem
    lista = [] #lista vazia que receberá a entrada de teclado
    db = ['diego','leonardo','sair','wolfeschlegelsteinhausenbergerdorff'] #base de dados cadastral

    while (ent != 'sair'): #loop com flag de saida
        ent = input("Digite o Nome ou 'sair' para encerrar o programa: ")
        name = ent.casefold() #transforma entrada do usuário para minusculas
        if name in db: #compara se o nome está cadastrado
            if name in lista: #se o nome estiver sido digitado anteriormente, dá log de saida
                logout.logout(name,lista)
            elif name == 'sair': 
                    continue
            else: #se o nome não tiver sido digitado anteriormente, dá log de entrada
                    login.login(name,lista)
        else: #se o nome não tiver na base de dados dá log de erro
            semcadastro.semcadastro("Usuário não cadastrado")
            continue
    else: #se a entrada for a string sair, para o programa
        opfile.opfile()
    return
