# Fila com produtor, consumidor em thread,
# com comportamento aleatório
#
# limitando o tamanho da fila e usando semáforos/locks para controle de acesso

import threading
import time
import random


ATRASO_MENOR = 0.001 # 1ms
ATRASO_MAIOR = 0.01  # 20ms

class Fila:

    def __init__(self, tamanho):
        self.fila = []
        self.tamanho = tamanho
        self.lock_produtor = threading.Lock()
        self.lock_consumidor = threading.Lock()
        self.lock_consumidor.acquire()

    def deposita(self, item):
        while len(self.fila) == self.tamanho:
            # fila esta no tamanho máximo => esperar que alguem consuma
            # SINCRONIZACAO: quem invocou DEPOSITA precisa ficar esperando
            #print(f'd{len(self.fila)}')
            #time.sleep(0.01)
            self.lock_produtor.acquire()

        self.fila.append(item)
        if self.lock_consumidor.locked():
           self.lock_consumidor.release()

    def retira(self):
        while len(self.fila) == 0:
            # fila nao possui elementos => esperar que alguem produza
            # SINCRONIZACAO: quem invocou RETIRA precisa ficar esperando
            self.lock_consumidor.acquire()

        item = self.fila.pop(0)
        if self.lock_produtor.locked():
           self.lock_produtor.release()


        return item


class Produtor(threading.Thread) :

    def __init__(self, nome, fila):
        threading.Thread.__init__(self)

        self.nome = nome
        self.fila = fila

    def run(self):
        print(f'{self.nome};I')
        for i in range(50):
            time.sleep(random.uniform(ATRASO_MENOR, ATRASO_MAIOR))
            self.fila.deposita(str(i))
            print(f'{self.nome};D({i})')
        print(f'{self.nome};F')

class Consumidor(threading.Thread) :

    def __init__(self, nome, fila):
        threading.Thread.__init__(self)

        self.nome = nome
        self.fila = fila

    def run(self):
        print(f'{self.nome};I')
        for i in range(50):
            time.sleep(random.uniform(ATRASO_MENOR, ATRASO_MAIOR))
            item = self.fila.retira()
            print(f'{self.nome};C({item})')
        print(f'{self.nome};F')


# producao de itens
f = Fila(10)

print('1-produtor;2-consumidor')

p1 = Produtor('1-produtor', f)
c1 = Consumidor('2-consumidor', f)
p1.start()
c1.start()
# time.sleep(1)
