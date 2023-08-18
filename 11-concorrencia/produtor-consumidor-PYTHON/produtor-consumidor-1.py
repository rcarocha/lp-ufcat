# Fila sem limitacao de tamanho e monotarefa

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


# producao de itens
f = Fila(3)

f.deposita('*')
f.deposita('**')
f.deposita('***')
f.deposita('****')
f.deposita('*****')
f.deposita('*** ***')
f.deposita('*** *** ***')
f.deposita('*** *** *** ***')

for i in range(10):
    print(f'Retirado item[{f.retira()}]')
