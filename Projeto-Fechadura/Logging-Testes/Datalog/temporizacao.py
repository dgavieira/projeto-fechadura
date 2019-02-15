import time, sched, logging
s = sched.scheduler(time.time, time.sleep)
def fimexecucao():
    logging.info("Fim de execução de Programa")
    for handler in logging.root.handlers[:]: #muda o logging config para desenhar a linha que marca o fim do dia do log
        logging.root.removeHandler(handler)
    
    logging.basicConfig(filename = 'datalog.txt', format = '%(message)s', level=logging.DEBUG)
    logging.info("====================================================================================================")   
    return


