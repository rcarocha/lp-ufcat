# Laboratório 11.1: Corrotinas em Python

Nesta tarefa você irá verificar o funcionamento de corrotinas em Python. Todos os códigos aqui discutidos estão em [`corrotinas`](corrotinas/)

Execute o código `corrotina-exemplo-1.py` e observe a saída conforme indicado pelo professor. O programa `reporta-concorrencia.py` deve ser utilizado para ilustrar melhor a existência de concorrência entre as tarefas, interpretando a saída padrão do código com as tarefas.

Exemplo de execução no terminal (Linux) do código

        python3 corrotina-exemplo-1.py | python3 reporta-concorrencia.py

**Atenção**: Não adicione nenhum `print` no seu código pois o programa `reporta-concorrencia.py` poderá indicar um erro na interpretação da saída.

Modifique as temporizações, se necessário, para garantir que os códigos sempre executem sequencialmente.

## Corrotinas em Python

O código `corrotina-exemplo-2.py` utiliza efetivamente corrotinas em Python, embora não esteja utilizando o conceito corretamente.  Siga as seguntes tarefas:

1. Instrumente o código com as saídas para serem exibidas pelo `reporta-concorrencia.py`, conforme feito no código anterior.
2. Executar os códigos com `async` separados. As tarefas executam como corrotinas? Qual seria o resultado esperado na execução do código adequadamente implementado?
3. Utilize `async gather` (veja [documentação](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather)) para iniciar as duas corrotinas. Inspecione o resultado em termos de concorrência.
4. Adicione vários `sleep` em ambas as corrotinas com o objetivo de permitir a execução da outra corrotina enquanto outra está esperando por um intervalo de tempo. O `sleep` deve ser invocado utilizando `await`, da seguinte maneira ([documentação](https://docs.python.org/3/library/asyncio-task.html#asyncio.sleep)):

   ```Python
   await asyncio.sleep(1)
   ```

   Inspecione a concorrência no código.

5. Retire toda a temporização nas tarefas e mude o código de maneira a controlar a ordem de execução das tarefas por corrotinas, de maneira que:

   * As tarefas executam a parte final juntas, independentemente da ordem em que as tarefas foram iniciadas. Insira uma execução no final de cada tarefa indicada por `F`.

## Relatório

Inclua o código com a sincronização solicitada no item **(5)** no arquivo 

* [relatorio/corrotina.py](relatorio/corrotina.py).

Procure não utilizar outro nove para esta resposta, pois este arquivo é que será procurado na correção.
