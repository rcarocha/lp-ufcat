# Laboratório 11.2: Primitivas de Sincronização em Python

Nesta tarefa você irá verificar o funcionamento de algumas primitivas de sincronização simples em Python. Todos os códigos aqui discutidos estão em [`produtor-consumidor-PYTHON`](produtor-consumidor-PYTHON/)

### Funcionamento Sequencial do Código

1. Verifique e execute o código de `produtor-consumidor-1.py` que é sequencial e não há controle do limite de itens entre produtor e consumidor.
2. Verifique o funcionamento do código `produtor-consumidor-2.py`, que **possui threads**. O código é, de fato, multithread ou o seu funcionamento é sequencial?

3. O que ocorre se `Fila` possui menos espaço que o necessário para produtores? O que ocorre na execução do código? O que deveria ocorrer na execução do código, supondo uma solução correta para o problema de produtor-consumidor?

4. Mude os atrasos em produtor e consumidor, realizando modificações no código `time.sleep(random.uniform(ATRASO_MENOR, ATRASO_MAIOR))`, que estão variando entre 1ms e 10ms. Veja o efeito na concorrência do código.
5. Aumente o tamanho máximo da fila, deixando-a muito maior que o número de elemento produzidos. Qual é o efeito na concorrência? Qual seria o efeito esperado, supondo uma solução correta para o problema de produtor-consumidor?
6. Acrescente atrasos na fila no depósito e/ou consumo na seção de código

   ```Python
   while len(self.fila) == self.tamanho:
      # fila esta no tamanho máximo => esperar que alguem consuma
      # SINCRONIZACAO: quem invocou DEPOSITA precisa ficar esperando
      #print(f'd{len(self.fila)}')
      #time.sleep(0.01)
      pass
   ```

   Qual é o efeito final? O que este código (condição e funcionamento do laço) indicam sobre o efeito na concorrência? Como gostaríamos que o código funcionasse, em termos de efeito na concorrência?

7. Inspecione e execute o código `produtor-consumidor-3.py`. Retire o tempo de atraso no consumo e verifique o efeito na concorrência dos códigos. Retire o tempo de atraso no produção e verifique o efeito na concorrência nos códigos.
8. Inspecione e execute o código `produtor-consumidor-4.py`. Remova completamente todos os atrasos nas implementações `produtor-consumidor-3.py` e `produtor-consumidor-4.py`. Meça o tempo de execução usando `time` (conforme indicado pelo professor) e **sem** utilizar a indicação da concorrência (programa `reporta-concorrencia.py`.
9. Aumente o numero de dados produzidos e consumidos (exemplo: 50000), meça novamente o tempo e compare as duas soluções. Qual funciona melhor?

## Problema de Sincronização entre Tarefas

1. Abra o código `problema-sincronizacao.py`. Investigue o código e veja a saída e concorrência entre os processos.
2. Utilizando as mesmas construções de sincronização baseadas em `Lock` (e suas primitivas `acquire` e `release`) do código anterior e em semáforos, incluia uma sincronização entre as tarefas de maneira que, independentemente de qualquer condição, ordem no código ou temporização entre as tarefas, as seguintes condições sejam satisfeitas:

   1. A primeira tarefa a iniciar, gerando "I" na saída, seja a tarefa `t2`.

      Copie a classe `Tarefa` em `Tarefa1` e `Tarefa2` para facilitar a modificação individual de cada tarefa. Coloque temporizações no código de maneira a garantir que o seu código está correto.

3. Faça modificações no código, de maneira que haja **três** tarefas (crie uma terceira) e as seguintes condições sejam atendidas:

   1. A primeira tarefa a iniciar, gerando "I" na saída, seja a tarefa `t3`.
   2. Todas as tarefas devem executar a última ação ("F" na saída) uma após a outra, considerando em qualquer ordem.

   Documentação de `Lock`: https://docs.python.org/3/library/threading.html#lock-objects
