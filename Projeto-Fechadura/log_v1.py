#arquivo exemplo de datalog
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

nome = (input('insira o Nome: '))
f = open('Data.txt', 'r')
conteudo = f.readlines()
nomes = conteudo.split(" ") 



if nomes[0] == str(nome):
    arquivo.write(nome+ " " + hora + " Saida" +"\n")

else:
    arquivo.write(nome+ " " + hora + " Entrada" + "\n")

arquivo.flush()

#faca o que quiser
arquivo.close()
