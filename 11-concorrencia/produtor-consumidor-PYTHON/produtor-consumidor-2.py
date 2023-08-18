# Fila com produtor em thread, usando join para esperar o termino

import threading
import time

class Fila:

    def __init__(self, tamanho):
        self.fila = []
        self.tamanho = tamanho

    def deposita(self, item):
        if len(self.fila) == self.tamanho:
            # espere
            pass
        else:
            self.fila.append(item)

    def retira(self):
        if len(self.fila) == 0:
            # espere
            pass
        else:
            return self.fila.pop(0)


class Produtor(threading.Thread) :

    def __init__(self, nome, fila):
        threading.Thread.__init__(self)

        self.nome = nome
        self.fila = fila

    def run(self):

        print(f'{self.nome};I')

        for i in range(50):
            time.sleep(0.01)
            self.fila.deposita(self.nome + '-(' + str(i) + ')')
            print(f'{self.nome};D')

        print(f'{self.nome};F')

NUM_ITENS = 10

# producao de itens
f = Fila(NUM_ITENS)

print('1-produtor;2-consumidor')

p1 = Produtor('1-produtor', f)
p1.start()
# time.sleep(1)
p1.join()


for i in range(NUM_ITENS):
    # print(f'Retirado item[{f.retira()}]')
    print(f'2-consumidor;R')
