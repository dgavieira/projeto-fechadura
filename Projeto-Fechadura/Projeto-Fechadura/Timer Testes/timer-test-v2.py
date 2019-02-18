#tá funcionando - solucao mais provavel a ser implementada
#12 de fevereiro 2019 diego

import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    str = '======================================================================='
    print(str)
    s.enter(5,1, do_something, (sc,))

s.enter(3,1, do_something, (s,))
s.run()
