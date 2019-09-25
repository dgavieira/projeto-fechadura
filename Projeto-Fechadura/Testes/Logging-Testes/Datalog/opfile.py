import os

def opfile():
    with open('datalog.txt') as f:
        for line in f:
            print(line.strip())
    return
