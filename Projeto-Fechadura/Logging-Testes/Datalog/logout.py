import logging
logging.basicConfig(filename = 'datalog.txt', format = '%(asctime)s  %(levelname)s:  %(message)s',
                    datefmt = '%d/%m/%Y %H:%M:%S', filemode = 'w', level=logging.DEBUG)

def logout(name, lista):
    lista.remove(name) #retira nome digitado da lista se já tiver sido digitado anteriormente
    logging.info("Nome: %s \tTipo: %s", name, 'saida') #registra log de saida
    return
