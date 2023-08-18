import asyncio
import time

print('1-executa_corrotina;2-executa_corrotina')

async def executa_corrotina_1():
    print("1-executa_corrotina;I")
    print("1-executa_corrotina;M")
    print("1-executa_corrotina;F")



async def executa_corrotina_2():
    print("2-executa_corrotina;I")
    print("2-executa_corrotina;M")
    print("2-executa_corrotina;F")


async def main():
   await executa_corrotina_1()
   await executa_corrotina_2()

   # await asyncio.gather(executa_corrotina_1(), executa_corrotina_2())


asyncio.run(main())

