import logging

def shutdown():
    logging.info("Fim de execução de Programa")
    for handler in logging.root.handlers[:]: 
        logging.root.removeHandler(handler)
    
    logging.basicConfig(filename = 'datalog.txt', format = '%(message)s', level=logging.DEBUG)
    str = '======================================================================='
    logging.info("%s", str)
    return