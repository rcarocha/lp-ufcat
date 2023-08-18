# Problema de sincronização entre tarefas

import threading
import time
import random


ATRASO_MENOR = 0.001 # 1ms
ATRASO_MAIOR = 0.01  # 20ms



class Tarefa(threading.Thread) :

    def __init__(self, nome):
        threading.Thread.__init__(self)

        self.nome = nome

    def run(self):
        print(f'{self.nome};I')
        print(f'{self.nome};M')
        print(f'{self.nome};F')


print('1-tarefa;2-tarefa')

t1 = Tarefa('1-tarefa')
t2 = Tarefa('2-tarefa')
#t3 = Tarefa('3-tarefa')
t1.start()
t2.start()
#t3.start()


