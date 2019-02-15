#OpenFiles 2#
import os
import time 
from datetime import datetime

try:
    arquivo = open('Data.txt', 'a')
except FileNotFoundError:
    arquivo = open(nome_arquivo, 'w+')
    arquivo.writelines('Arquivo criado pois nao existia')

now = datetime.now()
hora = now.strftime('%d/%m/%Y %H:%M:%S')

texto=(input('insira o Nome: '))
arquivo.writelines(texto)
arquivo.writelines(" " + hora +"\n")


arquivo.flush()


#faca o que quiser
arquivo.close()