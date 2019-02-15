import sched, time, logging
s = sched.scheduler(time.time, time.sleep)
def timerlogger(sc):
    logging.info("Fim de execução de Programa")
    for handler in logging.root.handlers[:]: #muda o logging config para desenhar a linha que marca o fim do dia do log
        logging.root.removeHandler(handler)
    
    logging.basicConfig(filename = 'datalog.txt', format = '%(message)s', level=logging.DEBUG)
    str = '======================================================================='
    print(str)
    s.enter(2,1, timerlogger, (sc,))
    return

def runtimer(s):
    s.enter(3,1, timerlogger, (s,))
    s.run()
    return
