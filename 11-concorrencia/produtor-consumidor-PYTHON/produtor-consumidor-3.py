# Fila com produtor, consumidor em thread,
# com comportamento aleatório
#
# limitando o tamanho da fila e usando semáforos/locks para controle de acesso
#
# QUESTAO: por que colocar um simples teste no loop não resolve o problema?
# Codigo para mostrar problemas nessa visao ingenua

import threading
import time
import random


ATRASO_MENOR = 0.001 # 1ms
ATRASO_MAIOR = 0.01  # 10ms

class Fila:

    def __init__(self, tamanho):
        self.fila = []
        self.tamanho = tamanho

    def deposita(self, item):
        while len(self.fila) == self.tamanho:
            # fila esta no tamanho máximo => esperar que alguem consuma
            # SINCRONIZACAO: quem invocou DEPOSITA precisa ficar esperando
            #print(f'd{len(self.fila)}')
            #time.sleep(0.01)
            pass

        self.fila.append(item)

    def retira(self):
        while len(self.fila) == 0:
            # fila nao possui elementos => esperar que alguem produza
            # SINCRONIZACAO: quem invocou RETIRA precisa ficar esperando
            #print(f'r{len(self.fila)}')
            #time.sleep(0.01)
            pass

        return self.fila.pop(0)


class Produtor(threading.Thread) :

    def __init__(self, nome, fila):
        threading.Thread.__init__(self)

        self.nome = nome
        self.fila = fila

    def run(self):
        print(f'{self.nome};I')
        for i in range(50):
            time.sleep(random.uniform(ATRASO_MENOR, ATRASO_MAIOR))
            self.fila.deposita(self.nome + '-(' + str(i) + ')')
            print(f'{self.nome};D')
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
            self.fila.retira()
            print(f'{self.nome};C')
        print(f'{self.nome};F')


# producao de itens
f = Fila(10)

print('1-produtor;2-consumidor')

p1 = Produtor('1-produtor', f)
c1 = Consumidor('2-consumidor', f)
p1.start()
c1.start()

