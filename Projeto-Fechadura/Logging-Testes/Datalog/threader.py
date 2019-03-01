#aquivo principal
#deu pau

import threading
import queue
import time, datalog

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        #Sincroniza as threads
        #threadLock.acquire()
        process_data(self.name, self.q)
        #Libera para a próxima thread
        #treadLock.release()
        
def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workqueue.empty():
            data = q.get()
            queueLock.release()
            datalog.datalog()
        else:
            queueLock.release()
            time.sleep(1)

threadList = ["Thread-1", "Thread-2"]
nameList = ["One","Two"]
queueLock = threading.Lock()
workqueue = queue.Queue(10)
threads = []
threadID = 1

#Cria novas threads
for tName in threadList:
    thread = myThread(threadID, tName, workqueue)
    thread.start()
    threads.append(thread)
    threadID += 1

#Preenche a Fila
queueLock.acquire()
for word in nameList:
    workqueue.put(word)
queueLock.release()

#Espera a fila secar
while not workqueue.empty():
    pass

exitFlag = 1



#Espera as threads se completarem e reinicia
for t in threads:
    t.join()
    
