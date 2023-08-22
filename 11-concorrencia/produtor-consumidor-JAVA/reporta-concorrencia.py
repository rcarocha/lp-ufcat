'''
Exemplo de entrada:
------------------
1-produtor;2-produtor;3-produtor;4-produtor
1-produtor;X
1-produtor;X
1-produtor;X
2-produtor;Y
3-produtor;Z
4-produtor;X
1-produtor;X

A entrada deve ser pela entrada padrão (stdin)

'''


from colorama import init, Fore, Style
import csv
import sys

c = csv.reader(sys.stdin, delimiter=';')

ids = c.__next__()

id_to_col = {}
col = 0
for id in ids:
    id_to_col[id] = col
    col = col + 1
    
init()

COLUNAS = 80

cores = {
    'B': Fore.BLACK,
    'R': Fore.RED,
    'G': Fore.GREEN,
    'Y': Fore.YELLOW,
    'L': Fore.BLUE,
    'M': Fore.MAGENTA,
    'C': Fore.CYAN,
    'W': Fore.WHITE
}

id = ids

total_len = 0
for i in id:
    total_len = total_len + len(i)
    
pos_colunas = []
anterior = 0
for pos in range(len(id)):
    pos_colunas.append(anterior + int(len(id[pos])/2))
    anterior = anterior + len(id[pos]) + 1
    
#print(pos_colunas)
    
def printcol(i, valor):
    print(pos_colunas[i]*' ' + Fore.RED + valor + Style.RESET_ALL)
    
execucoes = []
print(' Identificadores de tarefas: ' + str(id_to_col))

print('-------------------------------------------------------')
for i in ids:
    print(i + ' ', end='')
print()

nextExecucao = c.__next__()

while nextExecucao:
    e = nextExecucao

    id_processo = e[0]
    exec_processo = e[1]
    col = id_to_col[id_processo]

    printcol(col, exec_processo)

    nextExecucao = c.__next__()
 

print('-------------------------------------------------------')
