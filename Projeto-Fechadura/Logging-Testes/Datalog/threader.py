import threading
import time, datalog, sys, logging, sched, time, login, logout, semcadastro, temporizacao, opfile, timing

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        #Sincroniza as threads
        datalog.datalog()
        #Libera para a próxima thread
        timing.timerlogger()
        timing.runtimer()
        

threadLock = threading.Lock()
threads = []

#Cria novas threads
thread1 = myThread(1, "Thread-1", 1)


#Inicia novas threads
thread1.start()


#Adiciona threads à lista

threads.append(thread1)


#Espera as threads se completarem e reinicia
for t in threads:
    t.join()
    
