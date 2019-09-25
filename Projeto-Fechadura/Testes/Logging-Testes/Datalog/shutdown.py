import logging

def shutdown():
    for handler in logging.root.handlers[:]: 
        logging.root.removeHandler(handler)
    logging.info("Fim de execução de Programa")
    
    logging.basicConfig(filename = 'datalog.txt', format = '%(message)s', level=logging.DEBUG)
    str = '======================================================================='
    logging.info("%s", str)
    return