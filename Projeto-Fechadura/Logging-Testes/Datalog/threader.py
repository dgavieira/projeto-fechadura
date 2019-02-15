import threading
import time, datalog, sys, logging, sched, time, login, logout, semcadastro, opfile, timing

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        #Sincroniza as threads
        threadLock.acquire()
        threadexec(self.name, self.counter, 3)
        #Libera para a próxima thread
        treadLock.release()
        
def threadexec(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        datalog.datalog()
        time.sleep(delay)
        timing.runtimer()
        counter -= 1

threadLock = threading.Lock()
threads = []

#Cria novas threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)


#Inicia novas threads
thread1.start()
thread2.start()


#Adiciona threads à lista

threads.append(thread1)
threads.append(thread2)

#Espera as threads se completarem e reinicia
for t in threads:
    t.join()
    
