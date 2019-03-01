#multiprocessador principal do programa.
#Chama rotina de datalog e de runtimer
from multiprocessing import Process
import datalog

def process_input():
    p = input()
    while True:
        try:
            line = input()
        except EOFError:
            return
        a = line.find(p)             
        if a != -1:
            print(line)
        if line=='':
            return

def loop_a():
    while 1:
        datalog.datalog()
        
'''def loop_b():
    while 1:
        print("processo paralelo")'''
        
if __name__ == '__main__':
    Process(target = loop_a).start()
    #Process(target = loop_b).start()
            