import logging
logging.basicConfig(filename = 'datalog.txt', format = '%(asctime)s  %(levelname)s:  %(message)s',
                    datefmt = '%d/%m/%Y %H:%M:%S', filemode = 'w', level=logging.DEBUG)

def semcadastro(str):
    "Nome não cadastrado"
    print(str)
    logging.error("Usuário não cadastrado") #sinaliza log de erro para entrada de usuário sem cadastro na lista 'db'
    return
