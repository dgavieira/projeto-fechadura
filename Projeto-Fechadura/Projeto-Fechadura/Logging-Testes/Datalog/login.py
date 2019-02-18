import logging
logging.basicConfig(filename = 'datalog.txt', format = '%(asctime)s  %(levelname)s:  %(message)s',
                    datefmt = '%d/%m/%Y %H:%M:%S', level=logging.DEBUG)

def login(name, lista):
    lista.append(name) #acrescenta nome digitado na lista vazia
    logging.info("Nome: %s \tTipo: %s", name, 'entrada') #log de entrada
    return
