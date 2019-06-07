import logging, time

logging.basicConfig(filename = 'datalog.txt', format = '%(asctime)s  %(levelname)s:  %(message)s', datefmt = '%d/%m/%Y %H:%M:%S',level=logging.DEBUG)
name = 'diego'
logging.info('Nome: %s \tTipo: %s', name, 'entrada')
time.sleep(10)
logging.info('Nome: %s \tTipo: %s', name, 'saída')
