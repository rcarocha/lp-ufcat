import asyncio
import time


# codigo sem corrotina

print('1-executa_corrotina;2-executa_corrotina')

def executa_corrotina_1():
    time.sleep(1)
    print("1-executa_corrotina;I")
    time.sleep(1)
    print("1-executa_corrotina;M")
    time.sleep(1)
    print("1-executa_corrotina;F")
    time.sleep(1)



def executa_corrotina_2():
    time.sleep(1)
    print("2-executa_corrotina;I")
    time.sleep(1)
    print("2-executa_corrotina;M")
    time.sleep(1)
    print("2-executa_corrotina;F")
    time.sleep(1)


executa_corrotina_1()
executa_corrotina_2()

